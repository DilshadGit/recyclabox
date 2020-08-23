from django.urls import re_path
from rest_framework import routers

from .views import ItemAPIView, ItemRudView # ItemPrice

app_name = 'products_api'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^items/$', ItemAPIView.as_view(), name='list_create_item_api'),
	re_path(r'^item/(?P<pk>\d+)/$', ItemRudView.as_view(), name='rud_item_api'),
	# re_path(r'^item/price/$', ItemPrice.as_view(), name='price'),
]