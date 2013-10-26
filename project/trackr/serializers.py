from rest_framework import serializers
from django.contrib.auth.models import User
from trackr.models import Item, Tag, Comment


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('id', 'name')


class ItemSerializer(serializers.ModelSerializer):
	tags = TagSerializer(many=True)
	user = UserSerializer()

	class Meta:
		model = Item
		fields = ('id', 'title', 'body', 'tags', 'user')


class CommentSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Comment
		fields = ('id', 'timestamp', 'body', 'user')
