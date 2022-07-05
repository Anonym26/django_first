from django.shortcuts import render
from .models import Book, Author, PublishingHouse


def get_books_list(request):

    books = Book.objects.all()

    context = {
        'books': books,
        'sale': False,
    }

    return render(request, 'books/index.html', context)


def get_book(request, id_book):

    books = Book.objects.get(pk=id_book)
    return books
