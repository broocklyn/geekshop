from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse, reverse_lazy
from ordersapp.models import Order, OrderItem
from django.db import transaction
from django.forms import inlineformset_factory
from django.views.generic.detail import DetailView
from basketapp.models import Basket
from ordersapp.forms import OrderItemForm


# Create your views here.
class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)