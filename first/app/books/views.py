from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


def get_books_list(request):
    book = Book.objects.get(pk=1)
    return HttpResponse(f'<h1>{book.book_name}</h1>')

