from django.urls import include, path
from rest_framework import routers
from api import views

# API URLs

router = routers.DefaultRouter()
router.register(r'cameras', views.CameraViewSet)
router.register(r'lenses', views.LensViewSet)
router.register(r'lens_mounts', views.LensMountViewSet)
router.register(r'manufacturers', views.ManufacturerViewSet)

# Use automatic URL routing.
urlpatterns = [
    path('cameras/<int:pk>/compatible_lenses', views.CompatibleLenses),
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
