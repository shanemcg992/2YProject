import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='genre', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def get_absolute_url(self):
        return reverse('shop:films_by_genre', args=[self.id])
    
    def __str__(self):
        return self.name
    

class Film(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='film', blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'film'
        verbose_name_plural = 'films'

    def get_absolute_url(self):
        return reverse('shop:film_detail', args=[self.genre.id, self.id])
    
    def __str__(self):
        return self.name