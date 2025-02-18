# studentapp/forms.py
from django import forms

SUBJECT_CHOICES = [
    ('math', 'Mathematics'),
    ('science', 'Science'),
    ('english', 'English'),
    ('history', 'History'),
]

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    roll = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
