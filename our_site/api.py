from .models import Legend_IVT
from rest_framework import viewsets, permissions
from .serializers import Legend_IVT_Serializer


class Legend_IVT_ViewSet(viewsets.ModelViewSet):
    queryset = Legend_IVT.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = Legend_IVT_Serializer
