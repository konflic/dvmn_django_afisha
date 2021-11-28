from django.db import models
from django.db.models.fields import CommaSeparatedIntegerField


class Place(models.Model):
    title = models.CharField(max_length=300)
    description_short = models.TextField()
    description_long = models.TextField()

    def __str__(self):
        return self.title


class Coordinate(models.Model):
    long = models.FloatField()
    lat = models.FloatField()
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.place.title


class Images(models.Model):
    image_name = models.TextField()
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.place.title
