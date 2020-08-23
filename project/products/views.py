from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
from django.http import Http404

from .models import Item


def item_list_view(request):
    template_name = 'index.html'
    queryset = Item.objects.all().order_by('-created')

    context = {'items': queryset}
    return render(request, template_name, context)


def item_detail_view(request, item_id):
    template_name = 'details.html'
    try:
        item_obj = get_object_or_404(Item, pk=item_id)
    except Item.DoesNotExist:
        raise Http404('Item does not exist')

    context = {
        'obj': item_obj,
    }
    return render(request, template_name, context)
