# studentapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_form, name='student_form'),  # Root URL for the student form
]