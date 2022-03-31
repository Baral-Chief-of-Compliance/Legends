from django.shortcuts import render
from rest_framework import generics
from our_site.models import Legend_IVT
from our_site.serializers import Legend_IVT_Serializer


class OurSiteAPIView(generics.ListAPIView):
    queryset = Legend_IVT.objects.all()
    serializer_class = Legend_IVT_Serializer
