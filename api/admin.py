from django.contrib import admin
from api.models import Camera, Lens, Manufacturer, LensMount

# Register your models here.

admin.site.register(Camera)
admin.site.register(Lens)
admin.site.register(Manufacturer)
admin.site.register(LensMount)
