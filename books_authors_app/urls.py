from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<number>', views.book_details),
    path('books/<number>/add_author_to_book<book_number>', views.add_author_to_book),
]