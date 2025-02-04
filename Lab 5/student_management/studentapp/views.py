from django.shortcuts import render

# Create your views here.
# studentapp/views.py
from django.shortcuts import render

def student_form(request):
    student_details = {}
    total_percentage = 0

    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        english_marks = int(request.POST.get('english_marks', 0))
        physics_marks = int(request.POST.get('physics_marks', 0))
        chemistry_marks = int(request.POST.get('chemistry_marks', 0))

        # Calculate total percentage
        total_marks = english_marks + physics_marks + chemistry_marks
        total_percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100

        student_details = {
            'name': name,
            'dob': dob,
            'address': address,
            'contact_number': contact_number,
            'email': email,
            'english_marks': english_marks,
            'physics_marks': physics_marks,
            'chemistry_marks': chemistry_marks,
        }

    return render(request, 'studentapp/student_form.html', {
        'student_details': student_details,
        'total_percentage': total_percentage,
    })