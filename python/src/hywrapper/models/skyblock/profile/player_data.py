from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class ActiveEffect(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    effect: str = ""
    level: int = 0
    # TODO what is this
    modifiers: List[str] = Field(default_factory=list)
    ticks_remaining: Optional[int] = Field(default=None, alias="ticks_remaining")
    infinite: Optional[bool] = None
    flags: int = 0


class PlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    visited_zones: List[str] = Field(default_factory=list, alias="visited_zones")
    last_death: Optional[int] = Field(default=0, alias="last_death")
    # TODO enum
    perks: Dict[str, int] = Field(default_factory=dict)
    # TODO enum
    garden_chips: Dict[str, int] = Field(default_factory=dict, alias="garden_chips")
    active_effects: List[ActiveEffect] = Field(default_factory=list, alias="active_effects")
    # TODO paused_effects
    reaper_peppers_eaten: int = Field(default=0, alias="reaper_peppers_eaten")
    # TODO temp_stat_buffs
    death_count: int = Field(default=0, alias="death_count")
    # TODO disabled_potion_effects
    # TODO enum
    achievement_spawned_island_types: List[str] = Field(
        default_factory=list, alias="achievement_spawned_island_types"
    )
    # TODO enum
    visited_modes: List[str] = Field(default_factory=list, alias="visited_modes")
    # TODO enum? meh
    unlocked_coll_tiers: List[str] = Field(default_factory=list, alias="unlocked_coll_tiers")
    # TODO enum
    crafted_generators: List[str] = Field(default_factory=list, alias="crafted_generators")
    fishing_treasure_caught: int = Field(default=0, alias="fishing_treasure_caught")
    # TODO enum
    experience: Dict[str, float] = Field(default_factory=dict)
