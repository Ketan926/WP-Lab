# calculator/forms.py
from django import forms

class CGPAForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    total_marks = forms.IntegerField(label='Total Marks')
