from django.shortcuts import render, redirect
from .models import Human
from .forms import HumanForm

def home(request):
    humans = Human.objects.all()
    return render(request, 'humans/home.html', {'humans': humans})

def get_human_details(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        human = Human.objects.filter(first_name=first_name).first()
        if human:
            return render(request, 'humans/home.html', {
                'humans': Human.objects.all(),
                'selected_human': human
            })
    return redirect('home')

def update_human(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        human = Human.objects.filter(first_name=first_name).first()
        if human:
            human.last_name = request.POST.get('last_name')
            human.phone = request.POST.get('phone')
            human.address = request.POST.get('address')
            human.city = request.POST.get('city')
            human.save()
    return redirect('home')

def delete_human(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        Human.objects.filter(first_name=first_name).delete()
    return redirect('home')