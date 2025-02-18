# carapp/forms.py
from django import forms

class CarForm(forms.Form):
    manufacturer_choices = [
        ('toyota', 'Toyota'),
        ('ford', 'Ford'),
        ('honda', 'Honda'),
        ('bmw', 'BMW'),
        ('mercedes', 'Mercedes-Benz'),
    ]
    
    manufacturer = forms.ChoiceField(
        choices=manufacturer_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    model_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Model Name'})
    )
