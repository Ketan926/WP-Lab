# carapp/views.py
from django.shortcuts import render
from .forms import CarForm

def car_form(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            manufacturer = form.cleaned_data['manufacturer']
            model_name = form.cleaned_data['model_name']
            return render(request, 'carapp/car_results.html', {'manufacturer': manufacturer, 'model_name': model_name})
    else:
        form = CarForm()

    return render(request, 'carapp/car_form.html', {'form': form})

def car_results(request):
    # This view will display the results after the form is submitted
    return render(request, 'carapp/car_results.html')
