from .models import Basket, BasketItem
from .views import _basket_id, basket_detail

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            basket = Basket.objects.filter(basket_id=_basket_id(request))
            basket_items = BasketItem.objects.all().filter(basket=basket[:1])
            for basket_item in basket_items:
                item_count += basket_item.quantity
        except Basket.DoesNotExist:
            item_count = 0
    return dict(item_count = item_count)