from trackr.models import Item, Tag
from trackr.serializers import ItemSerializer
from rest_framework import generics

class ItemsView(generics.ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemView(generics.RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
