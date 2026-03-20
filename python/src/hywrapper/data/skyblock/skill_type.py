from __future__ import annotations

from enum import Enum
from typing import Any, Optional


class SkillType(str, Enum):
    FARMING = "Farming"
    MINING = "Mining"
    COMBAT = "Combat"
    FORAGING = "Foraging"
    FISHING = "Fishing"
    ENCHANTING = "Enchanting"
    ALCHEMY = "Alchemy"
    CARPENTRY = "Carpentry"
    RUNECRAFTING = "Runecrafting"
    SOCIAL = "Social"
    TAMING = "Taming"
    HUNTING = "Hunting"

    @property
    def clean_name(self) -> str:
        return _CLEAN_NAMES[self]

    @classmethod
    def from_id(cls, id: Any) -> Optional[SkillType]:
        try:
            return cls(id)
        except ValueError:
            return None


_CLEAN_NAMES = {
    SkillType.FARMING: "Farming",
    SkillType.MINING: "Mining",
    SkillType.COMBAT: "Combat",
    SkillType.FORAGING: "Foraging",
    SkillType.FISHING: "Fishing",
    SkillType.ENCHANTING: "Enchanting",
    SkillType.ALCHEMY: "Alchemy",
    SkillType.CARPENTRY: "Carpentry",
    SkillType.RUNECRAFTING: "Runecrafting",
    SkillType.SOCIAL: "Social",
    SkillType.TAMING: "Taming",
    SkillType.HUNTING: "Hunting",
}
