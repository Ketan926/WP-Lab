from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'course_name', 'date_of_birth']
        widgets = {
            'student_name': forms.TextInput(attrs={'placeholder': 'Student Name'}),
            'course_name': forms.TextInput(attrs={'placeholder': 'Course Name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }