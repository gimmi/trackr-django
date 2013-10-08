from django.forms import widgets
from rest_framework import serializers

from trackr.models import Item, Tag

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('id', 'name')

class ItemSerializer(serializers.ModelSerializer):
	tags = TagSerializer(many=True)
	class Meta:
		model = Item
		fields = ('id', 'title', 'body', 'tags')
