from django.urls import path
from .views import get_books_list

urlpatterns = [
    path('', get_books_list),
]