from django.shortcuts import render
from .forms import RegForm

def home_view(request):
    context = {}
    form = RegForm(request.POST or None)
    
    # Check if the form is valid (i.e., all required fields are filled in properly)
    if form.is_valid():
        # Here, you can process the form data, such as saving it to the database
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        age = form.cleaned_data.get('age')
        
        # For now, we just send a success message to the context
        context['message'] = f"Thank you, {name}! Your registration is complete."

    context['form'] = form
    return render(request, "sample1_app/home.html", context)