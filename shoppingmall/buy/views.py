
from django.shortcuts import render, redirect
from django.views.generic import FormView

# Create your views here.
from pick.models import PickItem

from buy.models import Buy




def add_buy(request, product_id):


        product = PickItem.objects.get(id = product_id)


        buyitem = Buy.objects.create(
            product_buy = product

        )
        buyitem.save()


        return redirect('buy:buy_detail')





def buy_detail(request, form, pick_id, total_price=0):

    Buy_items = PickItem.objects.get(id = pick_id)
    for pick_item in Buy_items:
        product_buy = pick_item.product_id
        total_price += (pick_item.product.price * pick_item.quantity)

    buy = Buy(

        product_buy = product_buy,
        total_price= total_price
    )

    buy.save()


    return render(request, 'buy/view.html', dict(product_buy = product_buy,
        total_price= total_price))


# def ItemView(request):
#     products = Product.objects.all()
#     context = {'products' : products}
#
#     return render(request, "product/list.html", context)