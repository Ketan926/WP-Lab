# studentapp/views.py
from django.shortcuts import render, redirect
from .forms import StudentForm

def first_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Save the form data in session
            request.session['name'] = form.cleaned_data['name']
            request.session['roll'] = form.cleaned_data['roll']
            request.session['subject'] = form.cleaned_data['subject']
            return redirect('second_page')
    else:
        form = StudentForm()

    return render(request, 'studentapp/firstPage.html', {'form': form})

def second_page(request):
    # Retrieve the session data
    name = request.session.get('name', None)
    roll = request.session.get('roll', None)
    subject = request.session.get('subject', None)

    return render(request, 'studentapp/secondPage.html', {
        'name': name,
        'roll': roll,
        'subject': subject
    })
