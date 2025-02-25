from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Store details in session or send to the success page
            username = form.cleaned_data['username']
            email = form.cleaned_data.get('email', '')
            contact = form.cleaned_data.get('contact', '')
            
            # Storing details in the session
            request.session['username'] = username
            request.session['email'] = email
            request.session['contact'] = contact

            return redirect('success')
    else:
        form = RegisterForm()

    return render(request, 'register/register.html', {'form': form})

def success(request):
    username = request.session.get('username')
    email = request.session.get('email')
    contact = request.session.get('contact')

    return render(request, 'register/success.html', {
        'username': username,
        'email': email,
        'contact': contact
    })
