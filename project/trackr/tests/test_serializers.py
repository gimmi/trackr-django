from django.test import TestCase
from trackr.models import Item, Tag
from trackr.serializers import ItemSerializer

class ItemSerializerTest(TestCase):
	def test_serialize(self):
		item = Item.objects.create(title='a title', body='a body')
		data = ItemSerializer(item).data

		self.assertEqual(data, {
			'id': 1, 
			'title': 'a title',
			'body': 'a body',
		})
