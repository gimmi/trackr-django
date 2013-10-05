from django.forms import widgets
from rest_framework import serializers

from trackr.models import Item

class ItemSerializer(serializers.Serializer):
    title = serializers.Field()

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.title = attrs.get('title', instance.title)
            return instance

        return Item(**attrs)
