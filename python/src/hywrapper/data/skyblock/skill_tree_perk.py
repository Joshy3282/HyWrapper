from __future__ import annotations

from enum import Enum
from typing import Any, Optional


class SkillTreePerk(str, Enum):
    HOTM = "HOTM"
    CORE_OF_THE_MOUNTAIN = "Core Of The Mountain"
    MINING_SPEED = "Mining Speed"
    MINING_FORTUNE = "Mining Fortune"
    EFFICIENT_MINER = "Efficient Miner"
    TITANIUM_INSANIUM = "Titanium Insanium"
    PICKOBULUS = "Pickobulus"
    MOLE = "Mole"
    KEEP_IT_COOL = "Keep It Cool"
    POWDER_BUFF = "Powder Buff"
    STEADY_HAND = "Steady Hand"
    RAGS_TO_RICHES = "Rags To Riches"
    MINING_MASTER = "Mining Master"
    DEAD_MANS_CHEST = "Dead Mans Chest"
    VANGUARD_SEEKER = "Vanguard Seeker"
    GIFTS_FROM_THE_DEPARTED = "Gifts From The Departed"
    WARM_HEART = "Warm Heart"
    SURVEYOR = "Surveyor"
    PROFESSIONAL = "Professional"
    OLD_SCHOOL = "Old School"
    LUCK_OF_THE_CAVE = "Luck Of The Cave"
    SKY_MALL = "Sky Mall"
    QUICK_FORGE = "Quick Forge"
    MINESHAFT_MAYHEM = "Mineshaft Mayhem"
    FORTUNATE_MINEMAN = "Fortunate Mineman"
    EAGER_ADVENTURER = "Eager Adventurer"
    STRONG_ARM = "Strong Arm"
    HOTF = "HOTF"
    CENTER_OF_THE_FOREST = "Center Of The Forest"
    SWEEP = "Sweep"
    FORAGING_FORTUNE = "Foraging Fortune"
    DAILY_WISHES = "Daily Wishes"
    EFFICIENT_FORAGER = "Efficient Forager"
    GALATEAS_MIGHT = "Galateas Might"
    HUNTERS_LUCK = "Hunters Luck"
    DEEP_WATERS = "Deep Waters"
    FORAGING_MADNESS = "Foraging Madness"
    LOTTERY = "Lottery"
    FOREST_STRENGTH = "Forest Strength"
    ESSENCE_FORTUNE = "Essence Fortune"
    FOREST_SPEED = "Forest Speed"
    STRENGTH_BOOST = "Strength Boost"
    SPEED_BOOST = "Speed Boost"
    DAMAGE_BOOST = "Damage Boost"

    @property
    def clean_name(self) -> str:
        return _CLEAN_NAMES[self]

    @classmethod
    def from_id(cls, id: Any) -> Optional[SkillTreePerk]:
        try:
            return cls(id)
        except ValueError:
            return None


_CLEAN_NAMES = {
    SkillTreePerk.HOTM: "HOTM",
    SkillTreePerk.CORE_OF_THE_MOUNTAIN: "Core Of The Mountain",
    SkillTreePerk.MINING_SPEED: "Mining Speed",
    SkillTreePerk.MINING_FORTUNE: "Mining Fortune",
    SkillTreePerk.EFFICIENT_MINER: "Efficient Miner",
    SkillTreePerk.TITANIUM_INSANIUM: "Titanium Insanium",
    SkillTreePerk.PICKOBULUS: "Pickobulus",
    SkillTreePerk.MOLE: "Mole",
    SkillTreePerk.KEEP_IT_COOL: "Keep It Cool",
    SkillTreePerk.POWDER_BUFF: "Powder Buff",
    SkillTreePerk.STEADY_HAND: "Steady Hand",
    SkillTreePerk.RAGS_TO_RICHES: "Rags To Riches",
    SkillTreePerk.MINING_MASTER: "Mining Master",
    SkillTreePerk.DEAD_MANS_CHEST: "Dead Mans Chest",
    SkillTreePerk.VANGUARD_SEEKER: "Vanguard Seeker",
    SkillTreePerk.GIFTS_FROM_THE_DEPARTED: "Gifts From The Departed",
    SkillTreePerk.WARM_HEART: "Warm Heart",
    SkillTreePerk.SURVEYOR: "Surveyor",
    SkillTreePerk.PROFESSIONAL: "Professional",
    SkillTreePerk.OLD_SCHOOL: "Old School",
    SkillTreePerk.LUCK_OF_THE_CAVE: "Luck Of The Cave",
    SkillTreePerk.SKY_MALL: "Sky Mall",
    SkillTreePerk.QUICK_FORGE: "Quick Forge",
    SkillTreePerk.MINESHAFT_MAYHEM: "Mineshaft Mayhem",
    SkillTreePerk.FORTUNATE_MINEMAN: "Fortunate Mineman",
    SkillTreePerk.EAGER_ADVENTURER: "Eager Adventurer",
    SkillTreePerk.STRONG_ARM: "Strong Arm",
    SkillTreePerk.HOTF: "HOTF",
    SkillTreePerk.CENTER_OF_THE_FOREST: "Center Of The Forest",
    SkillTreePerk.SWEEP: "Sweep",
    SkillTreePerk.FORAGING_FORTUNE: "Foraging Fortune",
    SkillTreePerk.DAILY_WISHES: "Daily Wishes",
    SkillTreePerk.EFFICIENT_FORAGER: "Efficient Forager",
    SkillTreePerk.GALATEAS_MIGHT: "Galateas Might",
    SkillTreePerk.HUNTERS_LUCK: "Hunters Luck",
    SkillTreePerk.DEEP_WATERS: "Deep Waters",
    SkillTreePerk.FORAGING_MADNESS: "Foraging Madness",
    SkillTreePerk.LOTTERY: "Lottery",
    SkillTreePerk.FOREST_STRENGTH: "Forest Strength",
    SkillTreePerk.ESSENCE_FORTUNE: "Essence Fortune",
    SkillTreePerk.FOREST_SPEED: "Forest Speed",
    SkillTreePerk.STRENGTH_BOOST: "Strength Boost",
    SkillTreePerk.SPEED_BOOST: "Speed Boost",
    SkillTreePerk.DAMAGE_BOOST: "Damage Boost",
}
