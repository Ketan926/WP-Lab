from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page with form
    path('products/', views.product_list, name='product_list'),  # Product list page
]