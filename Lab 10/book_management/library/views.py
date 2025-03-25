from django.shortcuts import render, redirect
from .forms import AuthorForm, PublisherForm, BookForm
from .models import Author, Publisher, Book

def home(request):
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    books = Book.objects.all()

    return render(request, 'library/home.html', {
        'authors': authors,
        'publishers': publishers,
        'books': books,
    })

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'library/add_author.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PublisherForm()
    return render(request, 'library/add_publisher.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})