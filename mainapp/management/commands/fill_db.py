import os
import json

from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.contrib.auth.models import User
from django.conf import settings


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data with deleting old data'

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        [ProductCategory.objects.create(**category) for category in categories]

        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            product['category'] = ProductCategory.objects.get(name=product["category"])
            Product.objects.create(**product)

        # creating superuser with our model
        if not User.objects.filter(username="django").exists():
            super_user = User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
