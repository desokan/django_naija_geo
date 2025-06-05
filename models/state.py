from django.db import models
from .base import GeoBaseModel
from .zone import Zone


class State(GeoBaseModel):
    """
    Nigerian state (e.g., 'Lagos', 'Kano').
    """
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name='states')
    capital = models.CharField(max_length=100)
    slogan = models.CharField(max_length=200, blank=True)

    class Meta(GeoBaseModel.Meta):
        verbose_name = "State"
        verbose_name_plural = "States"
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'zone'], name='unique_state_per_zone')
        ]

    def get_absolute_url(self):
        return f"/api/naija/states/{self.pk}/"
