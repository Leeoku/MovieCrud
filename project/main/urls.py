from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('create/', views.create, name = 'create'),
    path('edit/<int:pk>/', views.edit, name = 'edit')
]