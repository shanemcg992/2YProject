from django.db import models
from movies.models import Film

class Watchlist(models.Model):
    watchlist_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Watchlist'
        ordering = ['date_added']

    def __str__(self):
        return self.watchlist_id

class WatchlistItem(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'WatchlistItem'

    def __str__(self):
        return self.film
