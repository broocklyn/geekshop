from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=128, unique=True)