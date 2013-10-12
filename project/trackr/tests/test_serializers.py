from django.test import TestCase
from trackr.models import Item, Tag
from trackr.serializers import ItemSerializer

class ItemSerializerTest(TestCase):
	def test_serialize(self):
		tag1 = Tag.objects.create(name='tag1')
		tag2 = Tag.objects.create(name='tag2')
		item = Item.objects.create(title='a title', body='a body')
		item.tags.add(tag1, tag2)
		data = ItemSerializer(item).data

		self.assertEqual(data, {
			'id': 1, 
			'title': 'a title',
			'body': 'a body',
			'tags': [{
				'id': 1,
				'name': 'tag1'
			}, {
				'id': 2,
				'name': 'tag2'
			}]
		})
