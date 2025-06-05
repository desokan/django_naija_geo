# Expose models for direct import
from .base import GeoBaseModel
from .zone import Zone
from .state import State
from .lga import LGA
from .ward import Ward

__all__ = ["GeoBaseModel", "Zone", "State", "LGA", "Ward"]
