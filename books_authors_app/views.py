from django.shortcuts import render

from .models import *

def index(request):
    context = {
        "authors": Author.objects.all(),
        "books": Book.objects.all()
    }
    return render(request, 'index.html', context)
