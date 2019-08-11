from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from basketapp.models import Basket
from mainapp.models import Product


def index():
    pass


@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(user=request.user,
                                        product=product).first()
    if basket_item:
        basket_item.quantity += 1
        basket_item.save()
    else:
        Basket.objects.create(user=request.user,
                              product=product,
                              quantity=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
