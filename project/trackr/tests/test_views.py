from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime
from django.utils.timezone import utc
from trackr.tests import testutils
from trackr.models import Tag, Comment


class ItemsViewTest(APITestCase):
    def test_item_list(self):
        testutils.create_valid_item()

        response = self.client.get('/items/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{
                'id': 1,
                'title': 'item title',
                'body': 'item body',
                'tags': [{'id': 1, 'name': 'tag name'}],
                'user': {'id': 1, 'username': 'gimmi'}
            }]
        })


class ItemViewTest(APITestCase):
    def test_get_item(self):
        testutils.create_valid_item()

        response = self.client.get('/items/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'title': 'item title',
            'body': 'item body',
            'tags': [{'id': 1, 'name': 'tag name'}],
            'user': {'id': 1, 'username': 'gimmi'}
        })


class CommentViewTest(APITestCase):
    def test_get_comment(self):
        item = testutils.create_valid_item()
        item.comment_set.create(
            user=User.objects.create_user('foo', 'foo@me.com', 'secret'),
            timestamp=datetime(2013, 12, 30, 20, 30, tzinfo=utc),
            body='comment 1'
        )

        response = self.client.get('/items/1/comments/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'user': 2,
            'timestamp': datetime(2013, 12, 30, 20, 30, tzinfo=utc),
            'body': 'comment 1',
        })

    def test_update_comment(self):
        item = testutils.create_valid_item()
        item.comment_set.create(
            user=User.objects.create_user('foo', 'foo@me.com', 'secret'),
            timestamp=datetime(2013, 12, 30, 20, 30, tzinfo=utc),
            body='comment 1'
        )

        response = self.client.put('/items/1/comments/1/', {
            'user': 1,
            'body': 'change',
            'timestamp': datetime(2013, 1, 1, 0, 0, tzinfo=utc)
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'user': 1,
            'body': 'change',
            'timestamp': datetime(2013, 1, 1, 0, 0, tzinfo=utc)
        })
        comment = Comment.objects.get(pk=1)
        self.assertEqual(comment.user.id, 1)
        self.assertEqual(comment.body, 'change')


class CommentsViewTest(APITestCase):
    def test_get_comments(self):
        item = testutils.create_valid_item()
        item.comment_set.create(
            user=User.objects.create_user('foo', 'foo@me.com', 'secret'),
            timestamp=datetime(2013, 12, 30, 20, 30, tzinfo=utc),
            body='comment 1'
        )
        item.comment_set.create(
            user=User.objects.create_user('bar', 'bar@me.com', 'secret'),
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
                'user': 2,
                'timestamp': datetime(2013, 12, 30, 20, 30, tzinfo=utc),
                'body': 'comment 1',
            }, {
                'id': 2,
                'user': 3,
                'timestamp': datetime(2013, 12, 30, 21, 30, tzinfo=utc),
                'body': 'comment 2',
            }]
        })

    def test_create_comment(self):
        testutils.create_valid_item()

        response = self.client.post('/items/1/comments/', {
            'user': 1,
            'timestamp': datetime(2013, 12, 30, 20, 30, tzinfo=utc),
            'body': 'comment 1'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        comment = Comment.objects.get(pk=1)
        self.assertEqual(comment.body, 'comment 1')
        self.assertEqual(comment.user.id, 1)
        self.assertEqual(comment.item.id, 1)
        self.assertEqual(comment.timestamp, datetime(2013, 12, 30, 20, 30, tzinfo=utc))

    def test_update_comment(self):
        item = testutils.create_valid_item()
        item.comment_set.create(
            user=User.objects.create_user('foo', 'foo@me.com', 'secret'),
            timestamp=datetime(2013, 12, 30, 20, 30, tzinfo=utc),
            body='comment 1'
        )

        response = self.client.put('/items/1/comments/1/', {
            'user': 1,
            'timestamp': datetime(2013, 12, 30, 20, 30, tzinfo=utc),
            'body': 'comment modified'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'user': 1,
            'timestamp': datetime(2013, 12, 30, 20, 30, tzinfo=utc),
            'body': 'comment modified'
        })


class UserViewTest(APITestCase):
    def test_get_user(self):
        User.objects.create_user('foo', 'foo@foo.com', 'secret')

        response = self.client.get('/users/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'username': 'foo'
        })


class TagsViewTest(APITestCase):
    def test_get(self):
        testutils.create_valid_tag()

        response = self.client.get('/tags/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{
            'id': 1,
            'name': 'tag name'
        }])

    def test_post(self):
        response = self.client.post('/tags/', {
            'name': 'a name'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id': 1,
            'name': 'a name'
        })

        tag = Tag.objects.get(pk=1)
        self.assertEqual(tag.name, 'a name')

    def test_delete(self):
        testutils.create_valid_tag()

        response = self.client.delete('/tags/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 0)
