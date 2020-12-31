from django.shortcuts import render, redirect

from .models import *

def index(request):
    context = {
        "authors": Author.objects.all(),
        "books": Book.objects.all()
    }
    return render(request, 'index.html', context)

def add_book(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
        return redirect('/')

def book_details(request, number):
    book = Book.objects.get(id=number)
    context = {
        "authors": Author.objects.all(),
        "book": Book.objects.get(id=number),
        "book_authors": book.authors.all()
    }
    return render(request, 'book_details.html', context)

def add_author_to_book(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        book = Book.objects.get(id=int(request.POST['book-id']))
        author = Author.objects.get(id=int(request.POST['author-id']))
        book.authors.add(author)
        return redirect('/')