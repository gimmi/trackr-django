from trackr.models import Item, Tag
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime
from django.utils.timezone import utc

class ItemsViewTest(APITestCase):
    def test_item_list(self):
        Item.objects.create(title='item 1', body='body')

        response = self.client.get('/items/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{
                'id': 1,
                'title': 'item 1',
                'body': 'body',
                'tags': []
            }]
        })

class ItemViewTest(APITestCase):
    def test_get_item(self):
        Item.objects.create(title='item 1', body='body')

        response = self.client.get('/items/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'title': 'item 1',
            'body': 'body',
            'tags': []
        })


class CommentsViewTest(APITestCase):
    def test_get_comments(self):
        item = Item.objects.create()
        item.comment_set.create(
            timestamp=datetime(2013, 12, 30, 20, 30, tzinfo=utc),
            body='comment 1'
        )
        item.comment_set.create(
            timestamp=datetime(2013, 12, 30, 21, 30, tzinfo=utc),
            body='comment 2'
        )

        response = self.client.get('/items/1/comments/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'count': 2,
            'next': None,
            'previous': None,
            'results': [{
                'id': 1,
                'timestamp': datetime(2013, 12, 30, 20, 30, tzinfo=utc),
                'body': 'comment 1',
            }, {
                'id': 2,
                'timestamp': datetime(2013, 12, 30, 21, 30, tzinfo=utc),
                'body': 'comment 2',
            }]
        })
