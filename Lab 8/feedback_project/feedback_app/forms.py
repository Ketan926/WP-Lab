from django import forms

class FeedbackForm(forms.Form):
    COURSE_CHOICES = [
        ('ASP-XML', 'ASP-XML'),
        ('DotNET', 'DotNET'),
        ('JavaPro', 'JavaPro'),
        ('Unix', 'Unix'),
        ('C', 'C'),
        ('C++', 'C++'),
    ]
    
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    feedback = forms.CharField(label="Feedback", widget=forms.Textarea)
    course = forms.ChoiceField(label="Course", choices=COURSE_CHOICES, widget=forms.Select)
