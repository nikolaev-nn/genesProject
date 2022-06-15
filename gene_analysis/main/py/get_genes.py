import numpy as np
import pandas as pd
import torch
import json
from sklearn.cluster import DBSCAN
from tqdm.notebook import tqdm
from transformers import AutoTokenizer, AutoModel, PreTrainedTokenizerFast
from umap import UMAP
import logging

from gene_analysis.celery import app

import os

cwd = os.path.dirname(os.path.realpath(__file__))

tokenizer = AutoTokenizer.from_pretrained(cwd + "/tokenizer")
model = AutoModel.from_pretrained(cwd + "/model")

@app.task
def test(x, y):
    return x + y


@app.task(task_track_started=True, soft_time_limit=600, time_limit=900, worker_max_memory_per_child=500000)
def get_genes(genes):

    summary_genes = pd.DataFrame.from_records(json.loads(genes))
    # summary_genes = pd.DataFrame.from_dict(genes, orient="index")
    if 5 >= len(summary_genes) >= 0:
        return None

    text = summary_genes["function"].values.tolist()
    list_of_tensors = []

    for i in tqdm(text):
        tokens = tokenizer.encode_plus(i, add_special_tokens=False,
                                       return_tensors='pt')
        input_id_chunks = tokens['input_ids'][0].split(510)
        mask_chunks = tokens['attention_mask'][0].split(510)

        chunksize = 512
        input_id_chunks = list(input_id_chunks)
        mask_chunks = list(mask_chunks)


        for i in range(len(input_id_chunks)):
            input_id_chunks[i] = torch.cat([
                torch.Tensor([101]), input_id_chunks[i], torch.Tensor([102])
            ])
            mask_chunks[i] = torch.cat([
                torch.Tensor([1]), mask_chunks[i], torch.Tensor([1])
            ])

            pad_len = chunksize - input_id_chunks[i].shape[0]  # padding
            if pad_len > 0:
                input_id_chunks[i] = torch.cat([
                    input_id_chunks[i], torch.Tensor([0] * pad_len)
                ])
                mask_chunks[i] = torch.cat([
                    mask_chunks[i], torch.Tensor([0] * pad_len)
                ]) 

        input_ids = torch.stack(input_id_chunks)
        logging.warning('1')
        attention_mask = torch.stack(mask_chunks)
        logging.warning('2')
        input_dict = {
            'input_ids': input_ids.long(),
            'attention_mask': attention_mask.int()
        }
        logging.warning('3')
        output = model(input_ids.long(), attention_mask.int())
        logging.warning('4')
        temp = output[1].detach().numpy()
        logging.warning('5')
        list_of_tensors.append(temp)
        
    logging.warning('6')

    for i in tqdm(range(len(list_of_tensors))):
        a = np.empty(0)
        for j in range(len(list_of_tensors[i])):
            a = np.concatenate((a, list_of_tensors[i][j]), axis=None)
        list_of_tensors[i] = a

    df = pd.DataFrame(list_of_tensors).fillna(0)

    abbs = summary_genes['function'].str.findall('[a-z0-9]{0,3}[A-Z]{2,3}[a-z0-9]{0,3}').values
    abb = pd.DataFrame(abbs)
    flat_list = [item for sublist in abbs for item in sublist]
    lst = list(set(flat_list))
    dic = dict.fromkeys(lst, 0)

    for i in tqdm(range(len(abb[0]))):
        temp_dic = dic.copy()
        for j in abb[0][i]:
            if j in temp_dic:
                temp_dic[j] = 1
        abb[0][i] = list(temp_dic.values())

    df_abb = pd.DataFrame(abb[0].tolist())

    go_terms_list = summary_genes["go"].dropna().tolist()
    unique_go_terms = sorted(list(set(' '.join(go_terms_list).split(" "))))
    go_dic = dict.fromkeys(unique_go_terms, 0)
    go_terms = pd.DataFrame(summary_genes["go"]).fillna("pad")

    for i in tqdm(range(len(go_terms["go"]))):
        temp_dic = go_dic.copy()
        for j in go_terms["go"][i].split():
            if j in temp_dic:
                temp_dic[j] = 1
        go_terms['go'][i] = list(temp_dic.values())

    go_df = pd.DataFrame(go_terms['go'].tolist())

    reducer = UMAP(n_components=len(go_df) - 2, random_state=0)
    second_reducer = UMAP(n_components=2, random_state=0)

    go_reduced = pd.DataFrame(reducer.fit_transform(go_df))
    abb_reduced = pd.DataFrame(reducer.fit_transform(df_abb))
    emb_reduced = pd.DataFrame(reducer.fit_transform(df))

    final_df = pd.concat([emb_reduced, abb_reduced], axis=1)
    final_df = pd.concat([final_df, go_reduced], axis=1)

    coord = pd.DataFrame(second_reducer.fit_transform(final_df))

    clusterer = DBSCAN(min_samples=3)
    clusterer.fit(coord)
    coord_and_labels = pd.concat([coord, pd.DataFrame(clusterer.labels_, columns=['labels'])], axis=1)

    result_df = pd.concat([summary_genes, coord_and_labels], axis=1).rename(
        columns={0: 'xcoord', 1: 'ycoord', 'original_request': 'originalRequest',
                 'function': 'Function', 'index': 'gene_id'})
    result_df = result_df[['originalRequest', 'Function', 'xcoord', 'ycoord', 'labels', 'gene_id']]
    unique_labels = list(result_df['labels'].unique())
    return result_df.to_json(orient='records'), unique_labels
