from django.db import models
from .base import GeoBaseModel
from .lga import LGA


class Ward(GeoBaseModel):
    """
    Administrative ward within an LGA (e.g., 'Ward A', 'Garki Ward').
    """
    lga = models.ForeignKey(
        LGA, on_delete=models.CASCADE, related_name='wards')

    class Meta(GeoBaseModel.Meta):
        verbose_name = "Ward"
        verbose_name_plural = "Wards"
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'lga'], name='unique_ward_per_lga')
        ]

    def get_absolute_url(self):
        return f"/api/naija/wards/{self.pk}/"
