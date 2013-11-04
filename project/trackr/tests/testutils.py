from django.contrib.auth.models import User
from trackr.models import Item, Tag


def create_valid_tag():
    return Tag.objects.create(name='tag name')


def create_valid_user():
    return User.objects.create_user('gimmi', 'gimmi@me.com', 'secret')


def create_valid_item(user=None, tag=None):
    user = user or create_valid_user()
    tag = tag or create_valid_tag()

    item = Item(title='item title', body='item body')
    item.user = user
    item.save()
    item.tags.add(tag)
    item.save()
    return item
