from __future__ import annotations

from enum import Enum


class GardenUpgrade(str, Enum):
    GROWTH_SPEED = "Crop Growth Speed"
    CROP_UPGRADE = "Crop Upgrade"
    PLOT_LIMIT = "Plot Limit"
