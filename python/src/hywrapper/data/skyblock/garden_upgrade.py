from __future__ import annotations

from enum import Enum
from typing import Any, Optional


class GardenUpgrade(str, Enum):
    GROWTH_SPEED = "GROWTH_SPEED"
    CROP_UPGRADE = "YIELD"
    PLOT_LIMIT = "PLOT_LIMIT"

    @property
    def clean_name(self) -> str:
        return _CLEAN_NAMES[self]

    @classmethod
    def from_id(cls, id: Any) -> Optional[GardenUpgrade]:
        try:
            return cls(id)
        except ValueError:
            return None


_CLEAN_NAMES = {
    GardenUpgrade.GROWTH_SPEED: "Crop Growth Speed",
    GardenUpgrade.CROP_UPGRADE: "Crop Upgrade",
    GardenUpgrade.PLOT_LIMIT: "Plot Limit",
}
