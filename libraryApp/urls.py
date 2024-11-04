from django.urls import path
from . import views

urlpatterns =  [
  path('', views.book_list, name = 'books'),
  path('book/new', views.add_book, name = 'add_book'),
  path('book/detail/<int:pk>', views.book_detail, name= 'book_detail'),
  path('book/update/<int:pk>', views.update_book, name = 'update_book'),
  path('book/delete/<int:pk>', views.delete_book, name = 'delete_book'),
  path('borrower', views.borrower_list, name = 'borrower'),

]