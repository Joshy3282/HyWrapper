from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.skyblock.museum_item import MuseumItem as MuseumItemEnum
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class MuseumResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    members: Dict[str, Member] = Field(default_factory=dict)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Member(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    value: Optional[int] = 0
    appraisal: Optional[bool] = None
    items: Dict[MuseumItemEnum, MuseumItemInfo] = Field(default_factory=dict)
    special: List[SpecialItemInfo] = Field(default_factory=list)


class MuseumItemInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    donatedTime: Optional[int] = Field(default=0, alias="donated_time")
    featuredSlot: Optional[str] = Field(default=None, alias="featured_slot")
    borrowing: Optional[bool] = None
    items: Optional[MuseumItem] = None


class SpecialItemInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    donatedTime: Optional[int] = Field(default=0, alias="donated_time")
    items: Optional[MuseumItem] = None


class MuseumItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: int = Field(default=0)
    data: str = Field(default="")
