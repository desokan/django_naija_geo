from django.db import models
from .base import GeoBaseModel


class Zone(GeoBaseModel):
    """
    Nigeria's geopolitical zone (e.g., 'North-West', 'South-East').
    """
    class Meta(GeoBaseModel.Meta):
        verbose_name = "Geopolitical Zone"
        verbose_name_plural = "Geopolitical Zones"

    def get_absolute_url(self):
        return f"/api/naija/zones/{self.pk}/"
