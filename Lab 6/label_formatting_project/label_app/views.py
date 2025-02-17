# label_app/views.py

from django.shortcuts import render
from .forms import MessageForm

def home(request):
    formatted_message = ''
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            bold = 'font-weight: bold;' if form.cleaned_data['bold'] else ''
            italic = 'font-style: italic;' if form.cleaned_data['italic'] else ''
            underline = 'text-decoration: underline;' if form.cleaned_data['underline'] else ''
            color = f"color: {form.cleaned_data['color']};"

            # Combine styles
            styles = bold + italic + underline + color
            formatted_message = f'<span style="{styles}">{name}: {message}</span>'
    else:
        form = MessageForm()

    return render(request, 'label_app/home.html', {'form': form, 'formatted_message': formatted_message})
