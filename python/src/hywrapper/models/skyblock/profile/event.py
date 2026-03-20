from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class RabbitHitmen(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rabbit_hitmen_slots: int = Field(default=0, alias="rabbit_hitmen_slots")
    missed_uncollected_eggs: int = Field(default=0, alias="missed_uncollected_eggs")
    egg_slot_cooldown_mark: int = Field(default=0, alias="egg_slot_cooldown_mark")
    egg_slot_cooldown_sum: int = Field(default=0, alias="egg_slot_cooldown_sum")


class Shop(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    year: int = 0
    # TODO enum
    rabbits: List[str] = Field(default_factory=list)
    chocolate_spent: int = Field(default=0, alias="chocolate_spent")
    cocoa_fortune_upgrades: int = Field(default=0, alias="cocoa_fortune_upgrades")


class TimeTower(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    charges: int = 0
    activation_time: int = Field(default=0, alias="activation_time")
    level: int = 0


class Rabbits(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    collected_eggs: Dict[str, int] = Field(default_factory=dict, alias="collected_eggs")
    # TODO enum
    collected_locations: Dict[str, List[str]] = Field(
        default_factory=dict, alias="collected_locations"
    )


class Easter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rabbits: Optional[Rabbits] = None
    time_tower: Optional[TimeTower] = Field(default=None, alias="timeTower")
    # TODO enum
    employees: Dict[str, int] = Field(default_factory=dict)
    chocolate: int = 0
    total_chocolate: int = Field(default=0, alias="total_chocolate")
    chocolate_since_prestige: int = Field(default=0, alias="chocolate_since_prestige")
    last_viewed_chocolate_factory: int = Field(default=0, alias="last_viewed_chocolate_factory")
    shop: Optional[Shop] = None
    rabbit_barn_capacity_level: int = Field(default=0, alias="rabbit_barn_capacity_level")
    chocolate_level: int = Field(default=0, alias="chocolate_level")
    rabbit_sort: str = Field(default="", alias="rabbit_sort")
    rabbit_filter: str = Field(default="", alias="rabbit_filter")
    supreme_chocolate_bars: int = Field(default=0, alias="supreme_chocolate_bars")
    click_upgrades: int = Field(default=0, alias="click_upgrades")
    chocolate_multiplier_upgrades: int = Field(default=0, alias="chocolate_multiplier_upgrades")
    rabbit_rarity_upgrades: int = Field(default=0, alias="rabbit_rarity_upgrades")
    refined_dark_cacao_truffles: int = Field(default=0, alias="refined_dark_cacao_truffles")
    el_dorado_progress: int = Field(default=0, alias="el_dorado_progress")
    rabbit_hitmen: Optional[RabbitHitmen] = Field(default=None, alias="rabbit_hitmen")
    golden_click_amount: int = Field(default=0, alias="golden_click_amount")
    golden_click_year: int = Field(default=0, alias="golden_click_year")
    rabbit_hotspot_filer: str = Field(default="", alias="rabbit_hotspot_filer")


class Event(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    easter: Optional[Easter] = None
