import random

from django.db.models.aggregates import Count
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Genes
from .py import get_genes


def index(request):
    return render(request, 'main/index.html')


@csrf_exempt
def genes(request):
    if request.method == 'POST':
        if 'search' in request.POST:
            genes_request = request.POST['search'].replace(' ', '').split(',')
            genes_db = Genes.objects.filter(original_request__in=genes_request).distinct('original_request')
            if len(genes_db) > 5:
                genes_json = get_genes(genes_db)
                return render(request, 'main/genes.html', {'genes': genes_json[0], 'labels': genes_json[1]})
        elif 'randomSearch' in request.POST:
            random_value = int(request.POST['randomSearch'])
            if random_value > 5:
                random_genes = get_random_genes(random_value)
                genes_json = get_genes(random_genes)
                return render(request, 'main/genes.html', {'genes': genes_json[0], 'labels': genes_json[1]})
    return render(request, 'main/errors/no-result.html')


def get_random_genes(random_value):
    count = Genes.objects.aggregate(count=Count('index'))['count']
    random_list = []
    for i in range(random_value):
        n = random.randint(0, count)
        random_list.append(n)
    return Genes.objects.filter(index__in=random_list)
