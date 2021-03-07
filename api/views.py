from rest_framework import viewsets
from rest_framework import views
from rest_framework import generics

from api.models import Camera, Lens, LensMount, Manufacturer
from api.serializers import CameraReadSerializer, CameraWriteSerializer, LensReadSerializer, LensWriteSerializer, \
    LensMountSerializer, ManufacturerSerializer

# API Views


class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST']:
            return CameraWriteSerializer
        else:
            return CameraReadSerializer


class LensViewSet(viewsets.ModelViewSet):
    queryset = Lens.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST']:
            return LensWriteSerializer
        else:
            return LensReadSerializer


class LensMountViewSet(viewsets.ModelViewSet):
    queryset = LensMount.objects.all()
    serializer_class = LensMountSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CompatibleLenses(generics.ListAPIView):
    serializer_class = LensReadSerializer

    def get_queryset(self):
        camera = Camera.objects.get(pk=self.kwargs['pk'])
        return camera.mount.lens_set.all()


class CompatibleCameras(generics.ListAPIView):
    serializer_class = CameraReadSerializer

    def get_queryset(self):
        lens = Lens.objects.get(pk=self.kwargs['pk'])
        return lens.mount.camera_set.all()


