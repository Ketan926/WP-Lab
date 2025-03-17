from django.shortcuts import render
from .forms import FeedbackForm

def feedback_form(request):
    form = FeedbackForm()
    return render(request, 'feedback_app/feedback_form.html', {'form': form})

def process_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
            course = form.cleaned_data['course']

            return render(request, 'feedback_app/feedback_summary.html', {
                'name': name,
                'email': email,
                'feedback': feedback,
                'course': course,
            })
    
    return render(request, 'feedback_app/feedback_form.html', {'form': FeedbackForm()})
