from rest_framework import serializers

from api.models import Camera, Lens, LensMount, Manufacturer

# Django REST framework serializers


class CameraReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'
        depth = 1


class CameraWriteSerializer(serializers.ModelSerializer):
    # Use write specific serializer with no nesting
    class Meta:
        model = Camera
        fields = '__all__'


class LensReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lens
        fields = '__all__'
        depth = 1


class LensWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lens
        fields = '__all__'



class LensMountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LensMount
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


