from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()  # Retrieve all students
    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new student
            return redirect('student_list')  # Redirect to the list view
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})