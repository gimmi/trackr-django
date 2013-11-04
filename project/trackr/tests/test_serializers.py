from django.test import TestCase
from trackr.models import Item, Tag
from trackr.serializers import ItemSerializer
from trackr.tests import testutils


class ItemSerializerTest(TestCase):
    def test_serialize(self):
        tag1 = Tag.objects.create(name='tag1')
        tag2 = Tag.objects.create(name='tag2')
        item = Item.objects.create(title='a title', body='a body', user=testutils.create_valid_user())
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
            }],
            'user': {
                'id': 1,
                'username': 'gimmi'
            }
        })

    def test_deserialize(self):
        target = ItemSerializer(data={
            'id': 1,
            'title': 'a title',
            'body': 'a body',
            'tags': [{
                'id': 1,
                'name': 'tag1'
            }, {
                'id': 2,
                'name': 'tag2'
            }],
            'user': {
                'id': 1,
                'username': 'gimmi'
            }
        })

        self.assertTrue(target.is_valid())
        actual = target.object
        self.assertEqual(actual.title, 'a title')
        self.assertEqual(actual.body, 'a body')
