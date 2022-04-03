from rest_framework import serializers
from our_site.models import Legend_IVT, Photo, Legend_on_photo, Comments


class Legend_IVT_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Legend_IVT
        fields = '__all__'


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class Legend_on_photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legend_on_photo
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
