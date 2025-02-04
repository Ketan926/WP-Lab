from django.shortcuts import render

def index(request):
    return render(request, 'basic.html')  # Ensure 'basic.html' exists in your templates directory