from django.contrib import admin
from .models import Genre, Film

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Genre, GenreAdmin)

class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'genre', 'available']
    list_editable = ['price', 'genre', 'available']
    list_per_page = 20

admin.site.register(Film, FilmAdmin)