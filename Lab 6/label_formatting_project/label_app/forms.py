# label_app/forms.py

from django import forms

class MessageForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    bold = forms.BooleanField(label='Bold', required=False)
    italic = forms.BooleanField(label='Italic', required=False)
    underline = forms.BooleanField(label='Underline', required=False)
    color = forms.ChoiceField(label='Text Color', choices=[
        ('black', 'Black'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    ], initial='black')
