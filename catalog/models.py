from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1001, help_text='Enter a brief description of the book')

    # isbn = models.CharField('ISBN', max_length=11, help_text='11 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique id for the book")

    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    imprint = models.CharField(max_length=200)

    due_date = models.DateField(null=True, blank=True)

    loan_status = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=loan_status, blank=True, default='m', help_text="Book Availability")

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        # return f'{self.id} ({self.book.title})'
        return '{0} ({1})'.format(self.id, self.book.title)

class Author(models.Model):

    first_name = models.CharField(max_length=101)

    last_name = models.CharField(max_length=101)

    date_of_birth = models.DateField(null=True, blank=True)

    date_of_death = models.DateField('Died',null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Language(models.Model):

    language_name = models.CharField(max_length=52, help_text="Enter language (e.g., English, Hindi, French, German, Spanish etc.)")

    def __str__(self):
        return self.language_name