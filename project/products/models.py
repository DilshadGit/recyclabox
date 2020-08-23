from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse

'''
https://stackoverflow.com/questions/2307674/in-django-what-is-a-sku
Stock keeping unit
'''


class Item(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name    = models.CharField(max_length=255)
    qty     = models.PositiveSmallIntegerField(default=0)
    price   = models.DecimalField(max_digits=5, decimal_places=2)
    # sku     = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True,)
    update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


    def get_url_api(self, request=None):
        return reverse('products_api:rud_item_api', kwargs={'pk': self.pk}, request=request)

    @property
    def in_stock(self):
        return int(self.qty > 0)

    @property
    def soled_item(self):
        return self.soled_item

    # Use for attribute owner in permission.py line 17
    @property
    def owner(self):
        return self.user
