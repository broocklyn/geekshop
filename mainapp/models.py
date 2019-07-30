from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=128, unique=True)

    description = models.TextField(verbose_name='описание', blank=True, null=True)