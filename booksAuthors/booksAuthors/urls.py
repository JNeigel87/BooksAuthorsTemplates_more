# from django.contrib import admin
from django.urls import path, include
from booksAuthorsApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('create', views.create),
    path('books/<booksid>', views.info),
    path('addAuthor/<booksid>', views.addAuthor),
    path('editBook/<booksid>', views.bookEdit),
    path('edit/<booksid>', views.updateBook),
    path('delete/<booksid>', views.delete),
    path('deleteAuthor/<booksid>', views.deleteAuthor),
]
