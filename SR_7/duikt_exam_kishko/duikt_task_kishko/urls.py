from django.urls import path
from . import views

urlpatterns = [
    path('install', views.install, name='install'),
    path('duikt_page_kishko/', views.index, name='index'),
]