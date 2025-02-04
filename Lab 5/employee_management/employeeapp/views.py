# employeeapp/views.py
from django.shortcuts import render
from datetime import datetime

def promotion_eligibility(request):
    eligibility_message = ""
    employee_ids = ['E001', 'E002', 'E003', 'E004', 'E005']  # Sample employee IDs

    if request.method == 'POST':
        selected_employee_id = request.POST.get('employee_id')
        date_of_joining = request.POST.get('date_of_joining')

        if selected_employee_id and date_of_joining:
            # Calculate years of experience
            joining_date = datetime.strptime(date_of_joining, '%Y-%m-%d')
            experience_years = (datetime.now() - joining_date).days // 365

            if experience_years > 5:
                eligibility_message = "YES"
            else:
                eligibility_message = "NO"

    return render(request, 'employeeapp/promotion_eligibility.html', {
        'employee_ids': employee_ids,
        'eligibility_message': eligibility_message,
    })