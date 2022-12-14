from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home/',home,name = "home"),
    path('register/',register,name = 'register'),
    path('login/',login,name = 'login'),
]
