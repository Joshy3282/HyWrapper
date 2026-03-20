from __future__ import annotations

from enum import Enum
from typing import Any, Optional


class GardenResource(str, Enum):
    WHEAT = "WHEAT"
    CARROT = "CARROT_ITEM"
    POTATO = "POTATO_ITEM"
    PUMPKIN = "PUMPKIN"
    MELON = "MELON"
    COCOA_BEANS = "INK_SACK:3"
    SUNFLOWER = "DOUBLE_PLANT"
    SUGAR_CANE = "SUGAR_CANE"
    MUSHROOM = "MUSHROOM_COLLECTION"
    CACTUS = "CACTUS"
    NETHER_WART = "NETHER_STALK"
    MOONFLOWER = "MOONFLOWER"
    WILD_ROSE = "WILD_ROSE"

    @property
    def clean_name(self) -> str:
        return _CLEAN_NAMES[self]

    @classmethod
    def from_id(cls, id: Any) -> Optional[GardenResource]:
        try:
            return cls(id)
        except ValueError:
            return None


_CLEAN_NAMES = {
    GardenResource.WHEAT: "Wheat",
    GardenResource.CARROT: "Carrot",
    GardenResource.POTATO: "Potato",
    GardenResource.PUMPKIN: "Pumpkin",
    GardenResource.MELON: "Melon",
    GardenResource.COCOA_BEANS: "Cocoa Beans",
    GardenResource.SUNFLOWER: "Sunflower",
    GardenResource.SUGAR_CANE: "Sugar Cane",
    GardenResource.MUSHROOM: "Mushroom",
    GardenResource.CACTUS: "Cactus",
    GardenResource.NETHER_WART: "Nether Wart",
    GardenResource.MOONFLOWER: "Moonflower",
    GardenResource.WILD_ROSE: "Wild Rose",
}
