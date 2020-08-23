from django.urls import re_path

from .views import item_list_view, item_detail_view

app_name = 'products'


urlpatterns = [
    re_path(r'^', item_list_view, name='item_list'),
    re_path(r'^detail/(?P<item_id>[0-9]+)/$', item_detail_view, name='item_detail'),
]
