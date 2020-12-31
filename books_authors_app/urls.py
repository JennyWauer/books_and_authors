from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<number>', views.book_details),
    path('add_author_to_book', views.add_author_to_book),
]