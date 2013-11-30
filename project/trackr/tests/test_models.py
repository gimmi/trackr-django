from django.test import TestCase
from trackr.models import Item, Tag, Comment
from datetime import datetime
from django.utils.timezone import utc
from trackr.tests import testutils


class ItemTest(TestCase):
    def test_create_and_retrieve_items(self):
        self.assertEqual(Item.objects.count(), 0)

        item = Item()
        item.title = 'item 1'
        item.body = 'item 1 body'
        item.user = testutils.create_valid_user()
        item.save()

        self.assertEqual(Item.objects.count(), 1)
        item = Item.objects.get(id=item.id)
        self.assertIsInstance(item, Item)
        self.assertEqual(item.user.id, 1)

    def test_associate_tag_to_item(self):
        item = Item.objects.create(title='item 1', user=testutils.create_valid_user())
        tag = Tag.objects.create(name='tag 1')

        item.tags.add(tag)
        item.save()

        item = Item.objects.get(id=item.id)
        tags = item.tags.all()
        self.assertEqual(len(tags), 1)
        self.assertEqual(tags[0].name, 'tag 1')


class TagTest(TestCase):
    def test_create_tag(self):
        self.assertEqual(Tag.objects.count(), 0)

        Tag.objects.create(name='tag1')

        tag2 = Tag(name='tag2')
        tag2.save()

        self.assertEqual(Tag.objects.count(), 2)


class CommentTest(TestCase):
    def test_create_and_retrieve(self):
        self.assertEqual(Comment.objects.count(), 0)
        user = testutils.create_valid_user()
        item = testutils.create_valid_item(user=user)

        comment = Comment()
        comment.item = item
        comment.user = user
        comment.timestamp = datetime(2013, 12, 30, 20, 30, tzinfo=utc)
        comment.body = 'comment 1'
        comment.save()

        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(item.comments.count(), 1)

        comment = Comment.objects.get(pk=1)
        self.assertEqual(comment.body, 'comment 1')
        self.assertEqual(comment.timestamp, datetime(2013, 12, 30, 20, 30, tzinfo=utc))
        self.assertEqual(comment.item.id, 1)
