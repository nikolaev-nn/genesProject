from django.urls import path

from . import views
from .views import LogoutView

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('registration', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
