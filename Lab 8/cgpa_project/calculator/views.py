# calculator/views.py
from django.shortcuts import render
from .forms import CGPAForm

def calculate(request):
    if request.method == 'POST':
        form = CGPAForm(request.POST)
        if form.is_valid():
            # Retrieve form data
            name = form.cleaned_data['name']
            total_marks = form.cleaned_data['total_marks']

            # Calculate CGPA (total marks / 50)
            cgpa = total_marks / 50.0

            # Store data in session
            request.session['name'] = name
            request.session['cgpa'] = cgpa

            # Redirect to result page
            return render(request, 'calculator/result.html', {'name': name, 'cgpa': cgpa})

    else:
        form = CGPAForm()

    return render(request, 'calculator/calculate.html', {'form': form})
