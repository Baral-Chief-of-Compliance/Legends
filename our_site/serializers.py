from rest_framework import serializers
from our_site.models import Legend_IVT


class Legend_IVT_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Legend_IVT
        fields = '__all__'
