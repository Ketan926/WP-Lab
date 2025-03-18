from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from blog.models import BlogPost, BlogPostForm

def archive(request):
    posts = BlogPost.objects.all()[:10]  # Get the latest 10 posts
    return render(request, 'archive.html', {'posts': posts, 'form': BlogPostForm()})

def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()  # Set the timestamp
            post.save()
            return HttpResponseRedirect('/blog/')
    else:
        form = BlogPostForm()
    return render(request, 'create_blogpost.html', {'form': form})
