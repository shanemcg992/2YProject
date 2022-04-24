from .models import Watchlist, WatchlistItem
from .views import _watchlist_id, watchlist_detail

def counter(request):
    item_count2 = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            watchlist = Watchlist.objects.filter(watchlist_id=_watchlist_id(request))
            watchlist_items = WatchlistItem.objects.all().filter(watchlist=watchlist[:1])
            for watchlist_item in watchlist_items:
                item_count2 += watchlist_item.quantity
        except Watchlist.DoesNotExist:
            item_count2 = 0
    return dict(item_count2 = item_count2)