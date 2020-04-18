
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('auth/login/', views.login),
    path('auth/logout/', views.logout),
    path('auth/register/', views.register),
]