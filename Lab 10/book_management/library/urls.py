from django.urls import path
from .views import home, add_author, add_publisher, add_book

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('add_author/', add_author, name='add_author'),  # Add author page
    path('add_publisher/', add_publisher, name='add_publisher'),  # Add publisher page
    path('add_book/', add_book, name='add_book'),  # Add book page
]