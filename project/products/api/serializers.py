from rest_framework import serializers
from products.models import Item

'''
Serializer does two things:
first convert the data to json object
second validate thoes data passed
'''


class ItemSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Item
        fields = ['url', 'name', 'qty', 'price', 'created', 'update', ]
        read_only_fields = ['user']

    def get_url(self, obj):
    	request = self.context.get('request')
    	return obj.get_url_api(request=request)

    def validate_name(self, value):
        new_item = Item.objects.filter(name__iexact=value)
        if self.instance:
            new_item = new_item.exclude(pk=self.instance.pk)
        if new_item.exists():
            raise serializers.ValidationError('The item exist')
        return value
