from django.shortcuts import render
from .models import Book, Author, PublishingHouse


def get_books_list(request):

    books = Book.objects.all()



    context = {
        'books': books,
        'sale': False,
    }

    return render(request, 'books/list_books.html', context)
