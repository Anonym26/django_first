import django_filters
from django import forms
from app.books.models import Book, Author


class BooksFilter(django_filters.FilterSet):
    author_query = Author.objects.all()

    book_name = django_filters.CharFilter()
    authors = django_filters.ModelChoiceFilter(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['book_name', 'authors']
        exclude = ['book_img']
