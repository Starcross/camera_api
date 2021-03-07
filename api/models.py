from django.db import models

# API Models

SENSOR_FORMATS = [
    ('full', 'Full frame'),
    ('aps-h', 'APS-H'),
    ('aps-c', 'APS-C'),
    ('4/3', 'Four thirds'),
    ('1"', '1 inch')
]
FOCUS_TYPES = [
    ('manual', 'Manual'),
    ('auto', 'Auto')
]


class Camera(models.Model):
    model = models.CharField(max_length=200)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    sensor_format = models.CharField(max_length=10, choices=SENSOR_FORMATS)
    mount = models.ForeignKey('LensMount', on_delete=models.CASCADE)
    focus_type = models.CharField(max_length=10, choices=FOCUS_TYPES)
    release_year = models.IntegerField(null=True)
    video = models.BooleanField()
    weight = models.IntegerField(null=True)
    exif_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"


class Lens(models.Model):
    model = models.CharField(max_length=200)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    mount = models.ForeignKey('LensMount', on_delete=models.CASCADE)
    sensor_format = models.CharField(max_length=10, choices=SENSOR_FORMATS)
    focus_type = models.CharField(max_length=10, choices=FOCUS_TYPES)
    focal_range = models.CharField(max_length=20)
    max_aperture = models.CharField(max_length=20)
    aperture_blades = models.IntegerField(null=True)
    filter_diameter = models.IntegerField(null=True)
    release_year = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    exif_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name_plural = "Lenses"


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LensMount(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


