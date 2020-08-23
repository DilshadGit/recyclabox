from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse 

# test the authenticated user
from rest_framework_jwt.settings import api_settings
payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

from django.contrib.auth import get_user_model

from ..models import Item

User = get_user_model()


class ItemAPITestCase(APITestCase):
    def setUp(self):
        user_instance = User.objects.create(
            username='hellotest', email='hello@test.com')
        user_instance.set_password('somethingnews123')
        user_instance.save()
        new_item = Item.objects.create(user=user_instance,
            name='new mobile', qty=133, price=145.99)

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_item(self):
        item_count = Item.objects.count()
        self.assertEqual(item_count, 1)

    # testing list
    def test_get_list_api(self):
        #create empty dic to return the data as json
        data = {}
        url  = reverse('products_api:list_create_item_api')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)

    # test post as the user authorized
    # def test_post_item_api(self):
    #     data = {'name': 'OnePlus', 'qty': 25, 'price': '122.95'}
    #     url  = reverse('products_api:list_create_item_api')
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # test detail of the item
    def test_get_item_api(self):
        obj  = Item.objects.first()
        data = {}
        url  = obj.get_url_api()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test post as the user authorized
    def test_update_item_api(self):
        obj  = Item.objects.first()
        url  = obj.get_url_api()
        data = {'name': 'OnePlus', 'qty': 25, 'price': '122.95'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_item_user(self):
        obj  = Item.objects.first()
        url  = obj.get_url_api()
        data = {'name': 'OnePlus', 'qty': 25, 'price': '122.95'}
        user_instance = User.objects.first()
        payload = payload_handler(user_instance)
        token_response = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT' + token_response)

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
