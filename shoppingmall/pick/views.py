from django.shortcuts import render, redirect
from product.models import Product
from .models import Pick, PickItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from user.models import User


def _pick_id(request):
    pick = request.session.session_key
    # pick = request.User.uuid
    print(pick)
    if not pick:
        pick = request.session.create()
    return pick

def add_pick(request, product_id):
    product = Product.objects.get(id = product_id)
    # user_pick_id = User.objects.get(id = request.user.pk)
    pick_id = _pick_id(request)
    print("check:", pick_id)
    try:
        pick = Pick.objects.get(pick_id= _pick_id(request))
    except Pick.DoesNotExist:
        pick = Pick.objects.create(
            pick_id = _pick_id(request)
            # user_pick_id = user_pick_id
        )
        pick.save()

    try:
        pick_item = PickItem.objects.get(product=product, pick = pick)
        pick_item.quantity += 1
        pick_item.save()

    except PickItem.DoesNotExist:

        pick_item = PickItem.objects.create(

            product = product,
            quantity =1,
            pick = pick
        )
        pick_item.save()

    return redirect('pick:pick_detail')

def pick_detail(request, total =0, counter =0, pick_items = None):
    try:
        pick = Pick.objects.get(pick_id = _pick_id(request))
        pick_items = PickItem.objects.filter(pick = pick, active=True)
        for pick_item in pick_items:
            total += (pick_item.product.price * pick_item.quantity)
            counter += pick_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'pick/pick_list.html', dict(pick_items = pick_items, total =total, counter = counter))




