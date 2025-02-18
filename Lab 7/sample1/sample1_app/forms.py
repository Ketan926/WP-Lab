from django import forms

class RegForm(forms.Form):
    # Add some example fields, such as:
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    age = forms.IntegerField(label='Your Age', min_value=18, max_value=100)