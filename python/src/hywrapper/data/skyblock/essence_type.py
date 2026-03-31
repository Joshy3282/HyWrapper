from __future__ import annotations

from enum import Enum
from typing import Any, Optional


class EssenceType(str, Enum):
    CRIMSON = "CRIMSON"
    DIAMOND = "DIAMOND"
    DRAGON = "DRAGON"
    FOREST = "FOREST"
    GOLD = "GOLD"
    ICE = "ICE"
    SPIDER = "SPIDER"
    UNDEAD = "UNDEAD"
    WITHER = "WITHER"

    @property
    def clean_name(self) -> str:
        return _CLEAN_NAMES[self]

    @classmethod
    def from_id(cls, id: Any) -> Optional[EssenceType]:
        try:
            return cls(id)
        except ValueError:
            return None


_CLEAN_NAMES = {
    EssenceType.CRIMSON: "Crimson",
    EssenceType.DIAMOND: "Diamond",
    EssenceType.DRAGON: "Dragon",
    EssenceType.FOREST: "Forest",
    EssenceType.GOLD: "Gold",
    EssenceType.ICE: "Ice",
    EssenceType.SPIDER: "Spider",
    EssenceType.UNDEAD: "Undead",
    EssenceType.WITHER: "Wither",
}
