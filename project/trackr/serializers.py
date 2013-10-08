from django.forms import widgets
from rest_framework import serializers

from trackr.models import Item, Tag

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'title', 'body', 'tags')

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('id', 'name')
