from django.shortcuts import render, redirect
from .forms import BookForm, AuthorForm, BorrowerForm
from .models import Book, Author, Borrower
from django.http import HttpResponse

# Create your views here.

### BOOK ####
# Book list
def book_list(request):
  books = Book.objects.all()
  return render(request, 'books_list.html', {'books': books})

# Book detail 
def book_detail(request, pk):
  book = Book.objects.get(id = pk)
  return render(request, 'book_detail.html', {'book': book})

# Book form 
def add_book(request):
  form = BookForm()
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('books')

  return render(request, 'book_form.html', {'form': form})

# Update book 
def update_book(request, pk):
  book = Book.objects.get(id = pk)
  form = BookForm(instance=book)
  if request.method == 'POST':
    form = BookForm(request.POST, instance = book)
    if form.is_valid():
      form.save()
      return redirect('books')
    
  return render(request, 'book_form.html', {'form': form})

# Delete Book 
def delete_book(request, pk):
  book = Book.objects.get(id = pk)
  if request.method == 'POST':
    book.delete()
    return redirect('books')
  return render(request, 'delete_book.html', {'book': book})
### ## ## ## 

### BORROWERS ### 
def borrower_list(request):
  borrowers = Borrower.objects.prefetch_related('borrowed_books').all()
  
  return render(request, 'borrower_list.html', {'borrowers': borrowers})





 




