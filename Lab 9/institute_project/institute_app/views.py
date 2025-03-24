from django.shortcuts import render, redirect
from .models import Institute
from .forms import InstituteForm

# Home Page: Displays all institutes
def home(request):
    institutes = Institute.objects.all()
    return render(request, 'institute_app/home.html', {'institutes': institutes})

# Form Page: Allows adding a new institute
def add_institute(request):
    if request.method == 'POST':
        form = InstituteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InstituteForm()
    return render(request, 'institute_app/add_institute.html', {'form': form})
