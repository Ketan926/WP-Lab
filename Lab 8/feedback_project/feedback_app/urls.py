from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_form, name='feedback_form'),
    path('process_feedback/', views.process_feedback, name='process_feedback'),
]
