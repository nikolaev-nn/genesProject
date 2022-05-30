import json
import random

from django.db.models.aggregates import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Genes, Favorite, FavoriteGroup
from .py import get_genes


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
                genes_json = get_genes(genes_db)
                return render(request, 'main/genes.html', {'genes': genes_json[0], 'labels': genes_json[1]})

        elif 'randomSearch' in request.POST:
            random_value = int(request.POST['randomSearch'])
            if random_value > 5:
                random_genes = get_random_genes(random_value)
                genes_json = get_genes(random_genes)
                return render(request, 'main/genes.html', {'genes': genes_json[0], 'labels': genes_json[1]})

    return render(request, 'main/errors/no-result.html')


@csrf_exempt
def save_favourites(request):
    # if request.method == 'POST' and request.user.is_authenticated:
    if request.method == 'POST':
        save_json_to_database(list(request.POST.keys())[0], request.user)
        return JsonResponse({}, status=200)
    elif request.method == 'POST' and not request.user.is_authenticated:
        return JsonResponse({"name": "You need to log in"}, status=400)
    else:
        return JsonResponse({"name": "Error, try again later"}, status=400)


def get_random_genes(random_value):
    count = Genes.objects.aggregate(count=Count('index'))['count']
    random_list = []
    for i in range(random_value):
        n = random.randint(0, count)
        random_list.append(n)
    return Genes.objects.filter(index__in=random_list)


def save_json_to_database(request, user):
    json_requests = json.loads(request)
    favorite_group = FavoriteGroup.objects.create(user_id=user.id)
    genes_id = list(map(lambda gene: gene['gene_id'], json_requests))
    req_genes = Genes.objects.filter(index__in=genes_id)
    for req in json_requests:
        favorite = Favorite.objects.create(favorite_id=favorite_group,
                                           xcoord=req['xcoord'],
                                           ycoord=req['ycoord'],
                                           label=req['labels'],
                                           gene_id=req_genes[0])
