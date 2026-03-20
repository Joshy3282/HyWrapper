from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.skyblock.museum_item import MuseumItem as MuseumItemEnum
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class MuseumResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    members: Optional[Dict[str, Member]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Member(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    value: Optional[int] = Field(default=None)
    appraisal: Optional[bool] = None
    items: Optional[Dict[MuseumItemEnum, MuseumItemInfo]] = Field(default=None)
    special: Optional[List[SpecialItemInfo]] = Field(default=None)


class MuseumItemInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    donatedTime: Optional[int] = Field(default=None, alias="donated_time")
    featuredSlot: Optional[str] = Field(default=None, alias="featured_slot")
    borrowing: Optional[bool] = None
    items: Optional[MuseumItem] = None


class SpecialItemInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    donatedTime: Optional[int] = Field(default=None, alias="donated_time")
    items: Optional[MuseumItem] = None


class MuseumItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[int] = Field(default=None)
    data: Optional[str] = Field(default=None)
