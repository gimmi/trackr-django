from django.test import TestCase
from trackr.models import Item, Tag
from django.contrib.auth.models import User
from trackr.serializers import ItemSerializer, UserSerializer
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


class UserSerializerTest(TestCase):
    def test_serialize(self):
        user = testutils.create_valid_user()

        target = UserSerializer(user)

        self.assertEqual(target.data, {
            'id': 1,
            'username': 'gimmi',
        })

    def test_deserialize_into_existing_user(self):
        user = testutils.create_valid_user()

        target = UserSerializer(user, partial=True, data={
            'username': 'gimmi2'
        })

        self.assertTrue(target.is_valid())
        self.assertEqual(target.object.username, 'gimmi2')

        self.assertEqual(User.objects.get(pk=1).username, 'gimmi')
        target.save()
        self.assertEqual(User.objects.get(pk=1).username, 'gimmi2')
