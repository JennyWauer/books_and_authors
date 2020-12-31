from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<number>', views.book_details),
    path('add_author_to_book', views.add_author_to_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('authors/<number>', views.author_details),
    path('add_book_to_author', views.add_book_to_author),
]