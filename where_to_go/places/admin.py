from django.contrib import admin
from .models import Place, Coordinate, Image

# Register your models here.
admin.site.register(Place)
admin.site.register(Coordinate)
admin.site.register(Image)
