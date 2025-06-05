from django.db import models


class GeoBaseModel(models.Model):
    """
    Abstract base model for all geographical entities.
    """
    name = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name
