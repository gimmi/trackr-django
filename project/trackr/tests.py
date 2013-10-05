from django.test import TestCase
from trackr.models import Item, Tag

class ItemTest(TestCase):
	def setUp(self):
		pass

	def test_create_and_retrieve_items(self):
		self.assertEqual(Item.objects.count(), 0)

		tag1 = Tag.objects.create(name='tag1')
		# tag2 = Tag.objects.create(name='tag2')

		item = Item()
		item.title = 'item 1'
		item.body = 'item 1 body'
		item.save()
		item.tags.add(tag1)
		item.tags.create(name='tag2')
		item.save()

		self.assertEqual(Item.objects.count(), 1)
		self.assertEqual(Tag.objects.count(), 2)

	def test_create_tag(self):
		self.assertEqual(Tag.objects.count(), 0)

		Tag.objects.create(name='tag1')

		tag2 = Tag(name='tag2')
		tag2.save()

		self.assertEqual(Tag.objects.count(), 2)

	def test_associate_tag_to_item(self):
		item = Item.objects.create(title='item 1')
		tag = Tag.objects.create(name='tag 1')

		item.tags.add(tag)
		item.save()

		item = Item.objects.get(id=item.id)
		tags = item.tags.all()
		self.assertEqual(len(tags), 1)
		self.assertEqual(tags[0].name, 'tag 1')
