from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genes', views.genes, name='genes'),
    path('check-execution', views.check_execution, name="check-execution")
    # path('save-to-favourites', views.save_favourites, name='save_favourites'),
]