from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/',views.BookListView.as_view(), name='books'),
    path('book/<pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/',views.AuthorListView.as_view(), name='authors'),
    path('author/<pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name = 'my-borrowed'),
    path('books-on-loan/', views.BooksOnLoan.as_view(), name = 'books-on-loan'),
    path('book/<pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]