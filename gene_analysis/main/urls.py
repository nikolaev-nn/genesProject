from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genes', views.genes, name='genes'),
    path('save-to-favourites', views.save_favourites, name='save_favourites'),
]