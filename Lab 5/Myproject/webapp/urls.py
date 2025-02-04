from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This will match the root URL (e.g., /)
    path('<int:year>/<int:month>/', views.index, name='index_with_params'),  # This will match /<year>/<month>/
]
