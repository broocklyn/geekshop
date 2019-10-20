from django.db import models
from django.conf import settings

from mainapp.models import Product


class BasketQuerySet(models.QuerySet):
    def delete(self):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete()


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    @property
    def product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        "return total quantity for user"
        return sum([el.quantity for el in self.user.basket.all()])

    @property
    def total_cost(self):
        "return total cost for user"
        return sum([el.product_cost for el in self.user.basket.all()])

    def delete(self, using=None, keep_parents=False):
        self.product.quantity += self.quantity
        self.product.save()
        super(self.__class__, self).delete()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)

