from django.db.models import Q
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter


from products.models import Item
from .permissions import IsOwnerOrReadOnly
from .serializers import ItemSerializer


'''
Endpoint 
Using mixins help to create, list update all in one
'''


class ItemAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    queryset = Item.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    # Search only for name of the item
    search_fields = ['name']


    # This help to create new item without adding username
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
    	return {'request': self.request}



class ItemRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Item.objects.all()


    def get_serializer_context(self, *args, **kwargs):
    	return {'request': self.request}

