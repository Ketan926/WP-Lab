from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/works/', views.insert_works, name='insert_works'),
    path('insert/lives/', views.insert_lives, name='insert_lives'),
    path('search/', views.search, name='search'),
]
