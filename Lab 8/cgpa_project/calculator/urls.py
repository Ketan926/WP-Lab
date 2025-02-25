# calculator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate, name='calculate'),  # Form to calculate CGPA
]
