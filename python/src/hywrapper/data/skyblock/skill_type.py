from __future__ import annotations

from enum import Enum


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
