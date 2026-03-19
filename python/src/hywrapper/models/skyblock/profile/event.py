from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Event(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    easter: Optional[Easter] = None


class Easter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rabbits: Optional[Rabbits] = None
    timeTower: Optional[TimeTower] = None
    employees: Dict[str, int] = Field(default={})
    chocolate: int = Field(default=0)
    totalChocolate: int = Field(default=0)
    chocolateSincePrestige: int = Field(default=0)
    lastViewedChocolateFactory: int = Field(default=0)
    shop: Optional[Shop] = None
    rabbitBarnCapacityLevel: int = Field(default=0)
    chocolateLevel: int = Field(default=0)
    rabbitSort: str = Field(default="")
    rabbitFilter: str = Field(default="")
    supremeChocolateBars: int = Field(default=0)
    clickUpgrades: int = Field(default=0)
    chocolateMultiplierUpgrades: int = Field(default=0)
    rabbitRarityUpgrades: int = Field(default=0)
    refinedDarkCacaoTruffles: int = Field(default=0)
    elDoradoProgress: int = Field(default=0)
    rabbitHitmen: Optional[RabbitHitmen] = None
    goldenClickAmount: int = Field(default=0)
    goldenClickYear: int = Field(default=0)
    rabbitHotspotFiler: str = Field(default="")


class Rabbits(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    collectedEggs: Dict[str, int] = Field(default={})
    collectedLocations: Dict[str, List[str]] = Field(default={})


class TimeTower(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    charges: int = Field(default=0)
    activationTime: int = Field(default=0)
    level: int = Field(default=0)


class Shop(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    year: int = Field(default=0)
    rabbits: List[str] = Field(default=[])
    chocolateSpent: int = Field(default=0)
    cocoaFortuneUpgrades: int = Field(default=0)


class RabbitHitmen(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rabbitHitmenSlots: int = Field(default=0)
    missedUncollectedEggs: int = Field(default=0)
    eggSlotCooldownMark: int = Field(default=0)
    eggSlotCooldownSum: int = Field(default=0)
