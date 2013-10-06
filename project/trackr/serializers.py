from django.forms import widgets
from rest_framework import serializers

from trackr.models import Item

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'title')
