from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class PlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    visitedZones: List[str] = Field(default=[])
    lastDeath: Optional[int] = Field(default=0)
    perks: Dict[str, int] = Field(default={})
    gardenChips: Dict[str, int] = Field(default={})
    activeEffects: List[ActiveEffect] = Field(default=[])
    reaperPeppersEaten: int = Field(default=0)
    deathCount: int = Field(default=0)
    achievementSpawnedIslandTypes: List[str] = Field(default=[])
    visitedModes: List[str] = Field(default=[])
    unlockedCollTiers: List[str] = Field(default=[])
    craftedGenerators: List[str] = Field(default=[])
    fishingTreasureCaught: int = Field(default=0)
    experience: Dict[str, float] = Field(default={})


class ActiveEffect(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    effect: str = Field(default="")
    level: int = Field(default=0)
    modifiers: List[str] = Field(default=[])
    ticksRemaining: Optional[int] = Field(default=0)
    infinite: Optional[bool] = None
    flags: int = Field(default=0)
