# vote/forms.py
from django import forms

class VoteForm(forms.Form):
    VOTE_CHOICES = [
        ('good', 'Good'),
        ('satisfactory', 'Satisfactory'),
        ('bad', 'Bad')
    ]
    
    vote = forms.ChoiceField(choices=VOTE_CHOICES, widget=forms.RadioSelect, label="How is the book 'ASP.NET with C#' by Vipul Prakashan?")
