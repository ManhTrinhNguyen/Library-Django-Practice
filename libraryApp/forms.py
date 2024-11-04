from .models import Author, Book, Borrower
from django import forms 

class AuthorForm(forms.ModelForm):
  class Meta:
    model = Author 
    fields = ['name', 'bio']

class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = '__all__'

class BorrowerForm(forms.ModelForm):
  class Meta:
    model = Borrower
    fields = '__all__'
  