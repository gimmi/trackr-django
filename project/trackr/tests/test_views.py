from trackr.models import Item, Tag
from rest_framework.test import APITestCase
from rest_framework import status

class ItemsViewTest(APITestCase):
	def test_item_list(self):
		Item.objects.create(title='item 1', body='body')

		response = self.client.get('/items/')
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, [{
			'id': 1,
			'title': 'item 1',
			'body': 'body',
		}])

