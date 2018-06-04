from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.

def genre_list():
    return ', '.join(Genre.objects.values_list('name', flat=True))

def index(request):
    num_books = Book.objects.all().count()

    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'genre_list': genre_list
        }
    )

class BookListView(generic.ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['user_data'] = 'Additional data through generic class based view - BookListView in catalog/views.py'
        return context

class BookDetailView(generic.DetailView):
    model = Book