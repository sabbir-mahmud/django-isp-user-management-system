# imports
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('profile/login', views.client_login, name='client-login'),
    path('profile/logout', views.client_logout, name='client_logout'),
]
