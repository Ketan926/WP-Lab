# Create your views here.
from django.shortcuts import render

def calculate(request):
    result = None
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operation = request.POST.get('operation')

        if num1 and num2:
            try:
                num1 = int(num1)
                num2 = int(num2)

                if operation == 'add':
                    result = num1 + num2
                elif operation == 'subtract':
                    result = num1 - num2
                elif operation == 'multiply':
                    result = num1 * num2
                elif operation == 'divide':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        result = "Cannot divide by zero"

            except ValueError:
                result = "Please enter valid integers."

    return render(request, 'calculator_app/index.html', {'result': result})


