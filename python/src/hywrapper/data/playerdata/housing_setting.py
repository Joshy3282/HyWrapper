from __future__ import annotations

from enum import Enum
from typing import Any, Optional


class HousingSetting(str, Enum):
    TIPS = "Tips"
    VISIBILITY = "Visibility"
    BORDER = "Border"
    PRO_TOOLS_PARTICLES = "Pro Tools Particles"
    HOUSING_PLUS_PREFIX = "Housing Plus Prefix"
    JUKEBOX_MUSIC = "Jukebox Music"

    @property
    def clean_name(self) -> str:
        return _CLEAN_NAMES[self]

    @property
    def type(self) -> Any:
        return _TYPES[self]

    @classmethod
    def from_id(cls, id: Any) -> Optional[HousingSetting]:
        try:
            return cls(id)
        except ValueError:
            return None


_CLEAN_NAMES = {
    HousingSetting.TIPS: "Tips",
    HousingSetting.VISIBILITY: "Visibility",
    HousingSetting.BORDER: "Border",
    HousingSetting.PRO_TOOLS_PARTICLES: "Pro Tools Particles",
    HousingSetting.HOUSING_PLUS_PREFIX: "Housing Plus Prefix",
    HousingSetting.JUKEBOX_MUSIC: "Jukebox Music",
}

_TYPES = {
    HousingSetting.TIPS: bool,
    HousingSetting.VISIBILITY: int,
    HousingSetting.BORDER: bool,
    HousingSetting.PRO_TOOLS_PARTICLES: bool,
    HousingSetting.HOUSING_PLUS_PREFIX: bool,
    HousingSetting.JUKEBOX_MUSIC: bool,
}
