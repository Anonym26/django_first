from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


def get_books_list(request):
    book = Book.objects.get(id_publishing_house__publishing_house_name='Утро')
    print(book.book_name)
    return HttpResponse(f'<h1>ОК</h1>')

