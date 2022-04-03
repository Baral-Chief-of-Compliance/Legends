from django.shortcuts import render
from rest_framework import generics, status
from our_site.models import Legend_IVT, Photo, Comments, Legend_on_photo
from our_site.serializers import Legend_IVT_Serializer, CreatePostSerializer, Legend_on_photoSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class OurSiteAPIView(generics.ListAPIView):
    queryset = Legend_IVT.objects.all()
    serializer_class = Legend_IVT_Serializer


class PostAPIView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = CreatePostSerializer


class Legend_on_photoAPIView(generics.ListAPIView):
    queryset = Legend_on_photo.objects.all()
    serializer_class = Legend_on_photoSerializer


class CommentAPIView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
