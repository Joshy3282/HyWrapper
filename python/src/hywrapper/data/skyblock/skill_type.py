from __future__ import annotations

from enum import Enum
from typing import Any, Optional


class SkillType(str, Enum):
    FARMING = "FARMING"
    MINING = "MINING"
    COMBAT = "COMBAT"
    FORAGING = "FORAGING"
    FISHING = "FISHING"
    ENCHANTING = "ENCHANTING"
    ALCHEMY = "ALCHEMY"
    CARPENTRY = "CARPENTRY"
    RUNECRAFTING = "RUNECRAFTING"
    SOCIAL = "SOCIAL"
    TAMING = "TAMING"
    HUNTING = "HUNTING"

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
