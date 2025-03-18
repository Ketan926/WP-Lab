from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Works, Lives
from .forms import WorksForm, LivesForm
from django.db.models import Q

def index(request):
    return render(request, 'employee/index.html')

def insert_works(request):
    if request.method == 'POST':
        works_form = WorksForm(request.POST)
        if works_form.is_valid():
            works_form.save()
            return render(request, 'employee/success.html', {'message': 'Work data inserted successfully!'})
    else:
        works_form = WorksForm()
    return render(request, 'employee/insert_works.html', {'works_form': works_form})

def insert_lives(request):
    if request.method == 'POST':
        lives_form = LivesForm(request.POST)
        if lives_form.is_valid():
            lives_form.save()
            return render(request, 'employee/success.html', {'message': 'Lives data inserted successfully!'})
    else:
        lives_form = LivesForm()
    return render(request, 'employee/insert_lives.html', {'lives_form': lives_form})

def search(request):
    people_in_company = None
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        people_in_company = Works.objects.filter(company_name=company_name)
        people_details = []
        for person in people_in_company:
            city = Lives.objects.filter(person_name=person.person_name).first().city
            people_details.append((person.person_name, person.company_name, city))
        return render(request, 'employee/search_results.html', {'people_details': people_details})
    return render(request, 'employee/search.html')
