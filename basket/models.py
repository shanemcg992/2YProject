from django.db import models
from movies.models import Film

class Basket(models.Model):
    basket_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Basket'
        ordering = ['date_added']

    def __str__(self):
        return self.basket_id

class BasketItem(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'BasketItem'

    def sub_total(self):
        return self.film.price * self.quantity

    def __str__(self):
        return self.film