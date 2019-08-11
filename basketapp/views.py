from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product
from mainapp.views import get_basket


@login_required
def index(request):
    context = {
        'page_title': 'корзина',
        'basket': get_basket(request),

    }
    return render(request, 'basketapp/index.html', context)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('main:product',
                                            kwargs={
                                                'pk': pk
                                            }))

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


@login_required
def basket_delete(request, pk):
    get_object_or_404(Basket, pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_update(request, pk, quantity):
    if request.is_ajax():
        basket_obj = get_object_or_404(Basket, pk=pk)
        print(basket_obj, quantity)
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
