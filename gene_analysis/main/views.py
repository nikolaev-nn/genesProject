import json
import pickle
import random

from django.core import serializers
from django.db.models.aggregates import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Genes
from .py import get_genes, test


def index(request):
    random_genes = [e.original_request for e in get_random_genes(10)]
    return render(request, 'main/index.html', {'genes': random_genes})


@csrf_exempt
def genes(request):
    if request.method == 'POST':
        if 'search' in request.POST:
            genes_request = request.POST['search'].replace(' ', '').split(',')
            genes_db = Genes.objects.filter(original_request__in=genes_request).distinct('original_request')
            if len(genes_db) > 5:
                genes_json = serializers.serialize("json", genes_db)
                task = get_genes.delay(genes_json)
                # task = test.delay(2, 2)
                return render(request, 'main/genes.html', {'task_id': task.task_id})

        elif 'randomSearch' in request.POST:
            random_value = int(request.POST['randomSearch'])
            if random_value > 5:
                random_genes = get_random_genes(random_value)
                genes_json = serializers.serialize("json", random_genes)
                task = get_genes.delay(genes_json)
                # result = get_genes.AsyncResult(task.task_id).get()
                return render(request, 'main/genes.html', {'task_id': task.task_id})

    return render(request, 'main/errors/no-result.html')


def check_execution(request):
    if request.method == 'POST':
        task_id = str(request.POST['task_id'])
        state = get_genes.AsyncResult(task_id).state
        if state == 'SUCCESS':
            return JsonResponse(json.dumps(get_genes.AsyncResult(task_id).get()))
        elif state == 'FAILURE':
            response = JsonResponse({"error": "task is failure"})
            response.status_code = 403
            return response
        else:
            return JsonResponse({"status": state})


# @csrf_exempt
# def save_favourites(request):
    # if request.method == 'POST' and request.user.is_authenticated:
    # if request.method == 'POST':
    #     save_json_to_database(list(request.POST.keys())[0], request.user)
    #     return JsonResponse({}, status=200)
    # elif request.method == 'POST' and not request.user.is_authenticated:
    #     return JsonResponse({"name": "You need to log in"}, status=400)
    # else:
    #     return JsonResponse({"name": "Error, try again later"}, status=400)


def get_random_genes(random_value):
    count = Genes.objects.aggregate(count=Count('index'))['count']
    random_list = []
    for i in range(random_value):
        n = random.randint(0, count)
        random_list.append(n)
    return Genes.objects.filter(index__in=random_list)


'''
def save_json_to_database(request, user):
    json_requests = json.loads(request)
    favorite_group = FavoriteGroup.objects.create(user_id=user.id)
    genes_id = list(map(lambda gene: gene['gene_id'], json_requests))
    req_genes = Genes.objects.filter(index__in=genes_id)
    for req in json_requests:
        favorite = FavoriteGenes.objects.create(favorite_id=favorite_group,
                                           xcoord=req['xcoord'],
                                           ycoord=req['ycoord'],
                                           label=req['labels'],
                                           gene_id=req_genes[0])
'''
