from trackr.models import Item, Tag
from trackr.serializers import ItemSerializer, TagSerializer
from rest_framework import generics

class ItemView(generics.RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemsView(generics.ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	paginate_by = 2

class TagView(generics.RetrieveAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class TagsView(generics.ListAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
