from django.urls import path  # Correct import
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Correct usage of path
]