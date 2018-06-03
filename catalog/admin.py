from django.contrib import admin
from .models import Book, Genre, BookInstance, Author, Language

# Register your models here.

# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_date')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_date')
        }),
    )

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'language', 'display_genre')

    inlines = [BookInstanceInline]

admin.site.register(Genre)

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    
admin.site.register(Author, AuthorAdmin)

admin.site.register(Language)