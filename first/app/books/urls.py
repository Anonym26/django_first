from django.urls import path
from .views import BookList, BookDetail, add_book


urlpatterns = [
    path('', BookList.as_view(), name='main'),
    path('<int:pk>', BookDetail.as_view(), name='detail_book'),
    path('add_book/', add_book, name='add_book')
]
