from django.contrib import admin
from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=100, verbose_name='Название книги')
    authors = models.ManyToManyField(
        'Author',
        related_name='books'
    )
    description = models.TextField(verbose_name='Описание книги', null=True, blank=True)
    id_publishing_house = models.ForeignKey(
        'PublishingHouse',
        on_delete=models.CASCADE,
        related_name='publishinghouse_books',
        verbose_name='ID издательства',
        null=True,
        blank=True
    )
    date_creation = models.DateField(verbose_name='Дата написания книги', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class PublishingHouse(models.Model):
    publishing_house_name = models.CharField(max_length=300, verbose_name='Название издательства')
    address = models.CharField(max_length=1500, verbose_name='Адрес компании')
    contact_phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    website_linc = models.URLField(max_length=200, verbose_name='Ссылка на сайт', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return self.publishing_house_name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Author(models.Model):
    first_name = models.CharField(max_length=300, verbose_name='Имя')
    last_name = models.CharField(max_length=300, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=300, verbose_name='Отчество', null=True, blank=True)
    country = models.CharField(max_length=300, verbose_name='Страна')
    birthday = models.DateField(verbose_name='Дата рождения')
    languages = models.JSONField(verbose_name='Языки на которых писал автор', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class BooksInAuthor(admin.TabularInline):
    model = Book.authors.through
