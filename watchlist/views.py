from django.shortcuts import redirect, render, get_object_or_404
from movies.models import Film
from .models import Watchlist, WatchlistItem
from django.core.exceptions import ObjectDoesNotExist


def _watchlist_id(request):
    watchlist = request.session.session_key
    if not watchlist:
        watchlist = request.session.create()
    return watchlist


def add_watchlist(request, film_id):
    film = Film.objects.get(id=film_id)
    try:
        watchlist = Watchlist.objects.get(watchlist_id=_watchlist_id(request))
    except Watchlist.DoesNotExist:
        watchlist = Watchlist.objects.create(
                watchlist_id=_watchlist_id(request)
            )
        watchlist.save()
    try:
        watchlist_item = WatchlistItem.objects.get(film=film, watchlist=watchlist)
        if watchlist_item.quantity < watchlist_item.film.stock:
            watchlist_item.quantity += 1
        watchlist_item.save()
    except WatchlistItem.DoesNotExist:
        watchlist_item = WatchlistItem.objects.create(
                        film = film,
                        quantity = 1,
                        watchlist = watchlist
        )
        watchlist_item.save()
    return redirect('watchlist:watchlist_detail')

def watchlist_detail(request, total = 0, counter=0, watchlist_items=None):
    try:
        watchlist = Watchlist.objects.get(watchlist_id=_watchlist_id(request))
        watchlist_items = WatchlistItem.objects.filter(watchlist=watchlist, active=True)
        for watchlist_item in watchlist_items:
            total += (watchlist_item.film.price * watchlist_item.quantity)
            counter += watchlist_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'watchlist.html', {'watchlist_items':watchlist_items, 'counter':counter})

def watchlist_remove(request, film_id):
    watchlist = Watchlist.objects.get(watchlist_id=_watchlist_id(request))
    film = get_object_or_404(Film, id=film_id)
    watchlist_item = WatchlistItem.objects.get(film=film, watchlist=watchlist)
    if watchlist_item.quantity > 1:
        watchlist_item.quantity -= 1
        watchlist_item.save()
    else:
        watchlist_item.delete()
    return redirect('watchlist:watchlist_detail')


def full_remove(request, film_id):
    watchlist = Watchlist.objects.get(watchlist_id=_watchlist_id(request))
    film = get_object_or_404(Film, id=film_id)
    watchlist_item = WatchlistItem.objects.get(film=film, watchlist=watchlist)
    watchlist_item.delete()
    return redirect('watchlist:watchlist_detail')
