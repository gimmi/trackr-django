from trackr.models import Item, Tag
from django.contrib.auth.models import User
from trackr.serializers import ItemSerializer, TagSerializer, CommentSerializer, UserSerializer
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


class TagsView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        item_id = int(self.kwargs['item_id'])
        item = Item.objects.get(pk=item_id)
        return item.comment_set.all()


class CommentsView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    paginate_by = 2

    def get_item(self):
        item_id = int(self.kwargs['item_id'])
        return Item.objects.get(pk=item_id)

    def get_queryset(self):
        return self.get_item().comment_set.all()

    def pre_save(self, comment):
        comment.item = self.get_item()


class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
