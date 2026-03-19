from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict


class SkillTreePerk(str, Enum):
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


class PerkNode(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    level: int
    enabled: bool
