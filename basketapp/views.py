from django.shortcuts import render, get_object_or_404


# Create your views here.
from mainapp.models import Product


def index():
    pass

def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)