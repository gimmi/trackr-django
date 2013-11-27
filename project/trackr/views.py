from trackr.models import Item, Tag
from django.contrib.auth.models import User
from trackr.serializers import ItemSerializer, TagSerializer, CommentSerializer, UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ItemView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemsView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    paginate_by = 2


class TagView(APIView):
    def get(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def delete(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagsView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TagSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentView(generics.RetrieveUpdateAPIView):
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
