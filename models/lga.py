from django.db import models
from .base import GeoBaseModel
from .state import State


class LGA(GeoBaseModel):
    """
    Local Government Area (e.g., 'Agege', 'Jos North').
    """
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name='lgas')

    class Meta(GeoBaseModel.Meta):
        verbose_name = "Local Government Area"
        verbose_name_plural = "Local Government Areas"
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'state'], name='unique_lga_per_state')
        ]

    def get_absolute_url(self):
        return f"/api/naija/lgas/{self.pk}/"
