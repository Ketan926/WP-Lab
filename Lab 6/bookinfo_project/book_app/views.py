# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'book_app/home.html')

def metadata(request):
    return render(request, 'book_app/metadata.html')

def reviews(request):
    return render(request, 'book_app/reviews.html')

def publisher(request):
    return render(request, 'book_app/publisher.html')

