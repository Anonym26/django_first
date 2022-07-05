from django.urls import path
from .views import get_books_list, get_book


urlpatterns = [
    path('', get_books_list),
    path('<int:id_book>', get_book),
]
