from .models import Legend_IVT, Photo, Legend_on_photo, Comments
from rest_framework import viewsets, permissions
from .serializers import Legend_IVT_Serializer, CreatePostSerializer, Legend_on_photoSerializer, CommentSerializer


class Legend_IVT_ViewSet(viewsets.ModelViewSet):
    queryset = Legend_IVT.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = Legend_IVT_Serializer


class Post_ViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = CreatePostSerializer


class Legend_on_photo_ViewSet(viewsets.ModelViewSet):
    queryset = Legend_on_photo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = Legend_on_photoSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = CommentSerializer
