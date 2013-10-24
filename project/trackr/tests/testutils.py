from django.contrib.auth.models import User
from trackr.models import Item, Tag, Comment

def create_valid_tag():
	return Tag.objects.create(name='tag name')

def create_valid_user():
	return User.objects.create_user('gimmi', 'gimmi@me.com', 'secret')

def create_valid_item():
	item = Item.objects.create(title='item title', body='item body')
	item.tags.add(create_valid_tag())
	item.save()
	return item