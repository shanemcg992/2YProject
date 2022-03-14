from django.shortcuts import redirect, render, get_object_or_404
from movies.models import Film
from .models import Basket, BasketItem
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import stripe
from order.models import Order, OrderItem
from vouchers.models import Voucher
from vouchers.forms import VoucherApplyForm
from decimal import Decimal

def _basket_id(request):
    basket = request.session.session_key
    if not basket:
        basket = request.session.create()
    return basket


def add_basket(request, film_id):
    film = Film.objects.get(id=film_id)
    try:
        basket = Basket.objects.get(basket_id=_basket_id(request))
    except Basket.DoesNotExist:
        basket = Basket.objects.create(
            basket_id=_basket_id(request)
        )
        basket.save()
    try:
        basket_item = BasketItem.objects.get(film=film, basket=basket)
        if basket_item.quantity < basket_item.film.stock:
            basket_item.quantity += 1
        basket_item.save()
    except BasketItem.DoesNotExist:
        basket_item = BasketItem.objects.create(
            film=film,
            quantity=1,
            basket=basket
        )
        basket_item.save()
    return redirect('basket:basket_detail')


def basket_detail(request, total=0, counter=0, basket_items=None):
    discount =0
    voucher_id =0
    new_total =0
    voucher=None

    try:
        basket = Basket.objects.get(basket_id=_basket_id(request))
        basket_items = BasketItem.objects.filter(basket=basket, active=True)
        for basket_item in basket_items:
            total += (basket_item.film.price * basket_item.quantity)
            counter += basket_item.quantity
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'Online Shop - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    voucher_apply_form = VoucherApplyForm()

    try:
        voucher_id = request.session.get('voucher_id')
        voucher = Voucher.objects.get(id=voucher_id)
        if voucher !=None:
            discount = (total*(voucher.discount/Decimal('100')))
            new_total = (total - discount)
            stripe_total = int(new_total * 100)
    except:
        ObjectDoesNotExist
        pass

    if request.method == 'POST':
        print(request.POST)
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingcity = request.POST['stripeBillingAddressCity']
            billingCountry = request.POST['stripeBillingAddressCountryCode']
            shippingName = request.POST['stripeShippingName']
            shippingAddress1 = request.POST['stripeShippingAddressLine1']
            shippingcity = request.POST['stripeShippingAddressCity']
            shippingCountry = request.POST['stripeShippingAddressCountryCode']
            
            customer = stripe.Customer.create(
                        email=email,
                        source = token
            )
            stripe.Charge.create(
                    amount=stripe_total,
                    currency="eur",
                    description=description,
                    customer=customer.id
                )

            try:
                
                order_details = Order.objects.create(
                        token = token,
                        total = total,
                        emailAddress = email,
                        billingName = billingName,
                        billingAddress1 = billingAddress1,
                        billingCity = billingcity,
                        billingCountry = billingCountry,
                        shippingName = shippingName,
                        shippingAddress1 = shippingAddress1,
                        shippingCity = shippingcity,
                        shippingCountry = shippingCountry,
                    )
    
                order_details.save()
                if voucher != None:
                    order_details.total = new_total
                    order_details.voucher = voucher
                    order_details.discount = discount
                order_details.save()
                for order_item in basket_items:
                    oi = OrderItem.objects.create(
                        film = order_item.film.name,
                        quantity = order_item.quantity,
                        price = order_item.film.price,
                        order = order_details)
                    if voucher != None:
                        discount = (oi.price*(voucher.discount/Decimal('100')))
                        oi.price = (oi.price - discount)
                    else:
                        oi.price = oi.price*oi.quantity
                    oi.save()
                    '''Reduce stock when order is placed'''
                    films = Film.objects.get(id=order_item.film.id)
                    films.stock = int(order_item.film.stock - order_item.quantity)
                    films.save()
                    order_item.delete()

                    print('The order has been created')
                return redirect('order:thanks', order_details.id)
            except ObjectDoesNotExist:
                pass    

        except stripe.error.CardError as e:
            return e
    return render(request, 'basket.html', {'basket_items': basket_items, 'total': total, 'counter': counter,
                                        'data_key': data_key, 'stripe_total':stripe_total,
                                        'description': description, 'voucher_apply_form': voucher_apply_form,
                                        'new_total': new_total, 'voucher':voucher, 'discount':discount
                                        })


def basket_remove(request, film_id):
    basket = Basket.objects.get(basket_id=_basket_id(request))
    film = get_object_or_404(Film, id=film_id)
    basket_item = BasketItem.objects.get(film=film, basket=basket)
    if basket_item.quantity > 1:
        basket_item.quantity -= 1
        basket_item.save()
    else:
        basket_item.delete()
    return redirect('basket:basket_detail')


def full_remove(request, film_id):
    basket = Basket.objects.get(basket_id=_basket_id(request))
    film = get_object_or_404(Film, id=film_id)
    basket_item = BasketItem.objects.get(film=film, basket=basket)
    basket_item.delete()
    return redirect('basket:basket_detail')
