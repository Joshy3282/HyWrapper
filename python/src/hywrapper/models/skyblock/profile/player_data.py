from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class ActiveEffect(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    effect: Optional[str] = None
    level: Optional[int] = None
    modifiers: Optional[List[Any]] = Field(default=None)
    ticks_remaining: Optional[int] = Field(default=None, alias="ticks_remaining")
    infinite: Optional[bool] = None
    flags: Optional[int] = None


class PlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    visited_zones: Optional[List[str]] = Field(default=None, alias="visited_zones")
    last_death: Optional[int] = Field(default=None, alias="last_death")
    # TODO enum
    perks: Optional[Dict[str, int]] = Field(default=None)
    # TODO enum
    garden_chips: Optional[Dict[str, int]] = Field(default=None, alias="garden_chips")
    active_effects: Optional[List[ActiveEffect]] = Field(default=None, alias="active_effects")
    paused_effects: Optional[List[Any]] = Field(default=None, alias="paused_effects")
    reaper_peppers_eaten: Optional[int] = Field(default=None, alias="reaper_peppers_eaten")
    temp_stat_buffs: Optional[List[Any]] = Field(default=None, alias="temp_stat_buffs")
    death_count: Optional[int] = Field(default=None, alias="death_count")
    disabled_potion_effects: Optional[List[Any]] = Field(
        default=None, alias="disabled_potion_effects"
    )
    # TODO enum
    achievement_spawned_island_types: Optional[List[str]] = Field(
        default=None, alias="achievement_spawned_island_types"
    )
    # TODO enum
    visited_modes: Optional[List[str]] = Field(default=None, alias="visited_modes")
    # TODO enum? meh
    unlocked_coll_tiers: Optional[List[str]] = Field(default=None, alias="unlocked_coll_tiers")
    # TODO enum
    crafted_generators: Optional[List[str]] = Field(default=None, alias="crafted_generators")
    fishing_treasure_caught: Optional[int] = Field(default=None, alias="fishing_treasure_caught")
    # TODO enum
    experience: Optional[Dict[str, float]] = Field(default=None)
