from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Rift(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    villagePlaza: Optional[VillagePlaza] = None
    witherCage: Optional[WitherCage] = None
    blackLagoon: Optional[BlackLagoon] = None


class VillagePlaza(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    murder: Optional[Murder] = None
    barryCenter: Optional[BarryCenter] = None
    cowboy: Optional[Cowboy] = None
    lonely: Optional[Lonely] = None
    seraphine: Optional[Seraphine] = None
    gotScammed: Optional[bool] = None


class Murder(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    stepIndex: int = Field(default=0)
    roomClues: List[str] = Field(default=[])
    stepIndexPt2: int = Field(default=0)
    stepIndexPt3: int = Field(default=0)


class BarryCenter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    firstTalkToBarry: Optional[bool] = None
    convinced: List[str] = Field(default=[])
    receivedReward: Optional[bool] = None


class Cowboy(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    stage: int = Field(default=0)
    hayEaten: int
    rabbitName: str = Field(default="")
    exportedCarrots: int = Field(default=0)


class Lonely(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    secondsSitting: int = Field(default=0)


class Seraphine(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    stepIndex: int = Field(default=0)


class WitherCage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    killedEyes: List[str] = Field(default=[])


class BlackLagoon(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    talkedToEdwin: Optional[bool] = None
    receivedSciencePaper: Optional[bool] = None
    completedStep: int = Field(default=0)
    deliveredSciencePaper: Optional[bool] = None
