from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import random
import string

# Store session attempts
attempts = {}

def generate_captcha():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

def captcha_view(request):
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    if session_id not in attempts:
        attempts[session_id] = 0

    captcha = generate_captcha()
    request.session['captcha'] = captcha  # Store in session

    return render(request, 'captcha_form.html', {'captcha': captcha, 'disabled': attempts[session_id] >= 3})

def verify_captcha(request):
    session_id = request.session.session_key
    if not session_id or session_id not in attempts:
        return JsonResponse({'message': 'Session expired! Refresh the page.', 'disable': True})

    if attempts[session_id] >= 3:
        return JsonResponse({'message': 'Too many attempts! Textbox disabled.', 'disable': True})

    user_input = request.POST.get('captcha_input', '')
    correct_captcha = request.session.get('captcha', '')

    if user_input == correct_captcha:
        attempts[session_id] = 0  # Reset attempts
        return JsonResponse({'message': 'Captcha Matched! ✅', 'disable': False})
    else:
        attempts[session_id] += 1
        if attempts[session_id] >= 3:
            return JsonResponse({'message': 'Too many failed attempts! ❌ Textbox disabled.', 'disable': True})
        return JsonResponse({'message': 'Incorrect! Try again.', 'disable': False})
