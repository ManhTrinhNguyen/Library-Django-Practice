from django.db import models

# Create your models here.

# Author model 
class Author(models.Model):
  name = models.CharField(max_length=100)
  bio = models.TextField(blank=True, null=True)
  
  def __str__(self):
    return self.name 

# Book model with a one-to-many relationship with Author
class Book(models.Model): # 1 Author can have many Book
  title = models.CharField(max_length=100)
  author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='book')
  publiccation_date = models.DateField()
  description = models.TextField(blank=True, null=True)

  def __str__(self):
    return f'{self.title} by {self.author}'
  

# Borrower model with a many-to-many relationship with Book
class Borrower(models.Model): # Book can borrow by many borrwers . 1 Borrower can borrow many book
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  borrowed_books = models.ManyToManyField(Book, related_name='borrowers')

  def __str__(self):
    return self.name 
  

