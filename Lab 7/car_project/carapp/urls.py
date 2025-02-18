# carapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_form, name='car_form'),
    path('results/', views.car_results, name='car_results'),
]
