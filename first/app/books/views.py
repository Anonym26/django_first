from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.shortcuts import render
from app.books.models import Book, Author, PublishingHouse
from app.books.forms import BookForm
from app.books.filters import BooksFilter


class BookList(FilterView):

    model = Book
    filterset_class = BooksFilter
    context_object_name = 'books'
    template_name = 'books/book_list.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['books'] = self.queryset
        context['title'] = 'Городская библиотека'
        return context


def add_book(request):

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            book_name = form.cleaned_data['book_name']
            authors = form.cleaned_data['authors']

    form = BookForm()

    context = {

        'form': form,
    }

    return render(request, 'books/add_book.html', context=context)


class BookDetail(DetailView):
    model = Book
    # template_name = 'book_detailfdsa.html'
    pk_url_kwarg = 'pk'