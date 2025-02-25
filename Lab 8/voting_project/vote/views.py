# vote/views.py
from django.shortcuts import render
from .forms import VoteForm

def vote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.cleaned_data['vote']
            vote_counts = request.session.get('vote_counts', {'good': 0, 'satisfactory': 0, 'bad': 0})
            vote_counts[vote] += 1
            request.session['vote_counts'] = vote_counts

            return render(request, 'vote/result.html', {'vote_counts': vote_counts, 'form': form})
    else:
        form = VoteForm()

    return render(request, 'vote/vote.html', {'form': form})

def result(request):
    vote_counts = request.session.get('vote_counts', {'good': 0, 'satisfactory': 0, 'bad': 0})
    total_votes = sum(vote_counts.values())

    if total_votes > 0:
        good_percentage = (vote_counts['good'] / total_votes) * 100
        satisfactory_percentage = (vote_counts['satisfactory'] / total_votes) * 100
        bad_percentage = (vote_counts['bad'] / total_votes) * 100
    else:
        good_percentage = satisfactory_percentage = bad_percentage = 0

    return render(request, 'vote/result.html', {
        'vote_counts': vote_counts,
        'good_percentage': good_percentage,
        'satisfactory_percentage': satisfactory_percentage,
        'bad_percentage': bad_percentage,
    })
