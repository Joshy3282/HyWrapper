from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class RabbitHitmen(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rabbit_hitmen_slots: Optional[int] = Field(default=None, alias="rabbit_hitmen_slots")
    missed_uncollected_eggs: Optional[int] = Field(default=None, alias="missed_uncollected_eggs")
    egg_slot_cooldown_mark: Optional[int] = Field(default=None, alias="egg_slot_cooldown_mark")
    egg_slot_cooldown_sum: Optional[int] = Field(default=None, alias="egg_slot_cooldown_sum")


class Shop(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    year: Optional[int] = None
    # TODO enum
    rabbits: Optional[List[str]] = Field(default=None)
    chocolate_spent: Optional[int] = Field(default=None, alias="chocolate_spent")
    cocoa_fortune_upgrades: Optional[int] = Field(default=None, alias="cocoa_fortune_upgrades")


class TimeTower(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    charges: Optional[int] = None
    activation_time: Optional[int] = Field(default=None, alias="activation_time")
    level: Optional[int] = None


class Rabbits(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    collected_eggs: Optional[Dict[str, int]] = Field(default=None, alias="collected_eggs")
    # TODO enum
    collected_locations: Optional[Dict[str, List[str]]] = Field(
        default=None, alias="collected_locations"
    )


class Easter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rabbits: Optional[Rabbits] = None
    time_tower: Optional[TimeTower] = Field(default=None, alias="timeTower")
    # TODO enum
    employees: Optional[Dict[str, int]] = Field(default=None)
    chocolate: Optional[int] = None
    total_chocolate: Optional[int] = Field(default=None, alias="total_chocolate")
    chocolate_since_prestige: Optional[int] = Field(default=None, alias="chocolate_since_prestige")
    last_viewed_chocolate_factory: Optional[int] = Field(
        default=None, alias="last_viewed_chocolate_factory"
    )
    shop: Optional[Shop] = None
    rabbit_barn_capacity_level: Optional[int] = Field(
        default=None, alias="rabbit_barn_capacity_level"
    )
    chocolate_level: Optional[int] = Field(default=None, alias="chocolate_level")
    rabbit_sort: Optional[str] = Field(default=None, alias="rabbit_sort")
    rabbit_filter: Optional[str] = Field(default=None, alias="rabbit_filter")
    supreme_chocolate_bars: Optional[int] = Field(default=None, alias="supreme_chocolate_bars")
    click_upgrades: Optional[int] = Field(default=None, alias="click_upgrades")
    chocolate_multiplier_upgrades: Optional[int] = Field(
        default=None, alias="chocolate_multiplier_upgrades"
    )
    rabbit_rarity_upgrades: Optional[int] = Field(default=None, alias="rabbit_rarity_upgrades")
    refined_dark_cacao_truffles: Optional[int] = Field(
        default=None, alias="refined_dark_cacao_truffles"
    )
    el_dorado_progress: Optional[int] = Field(default=None, alias="el_dorado_progress")
    rabbit_hitmen: Optional[RabbitHitmen] = Field(default=None, alias="rabbit_hitmen")
    golden_click_amount: Optional[int] = Field(default=None, alias="golden_click_amount")
    golden_click_year: Optional[int] = Field(default=None, alias="golden_click_year")
    rabbit_hotspot_filer: Optional[str] = Field(default=None, alias="rabbit_hotspot_filer")


class Event(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    easter: Optional[Easter] = None
