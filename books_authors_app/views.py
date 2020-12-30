from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "authors": Author.objects.all(),
        "books": Book.objects.all()
    }
    return render(request, 'index.html', context)
