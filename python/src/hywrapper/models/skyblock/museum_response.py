from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class MuseumResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    members: Dict[str, Member] = Field(default={})
    rateLimit: Optional[RateLimit] = None


class Member(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    value: Optional[int] = Field(default=0)
    appraisal: Optional[bool] = None
    items: Dict[MuseumItem, MuseumItemInfo] = Field(default={})
    special: List[SpecialItemInfo] = Field(default=[])


class MuseumItemInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    donatedTime: Optional[int] = Field(default=0)
    featuredSlot: Optional[str] = None
    borrowing: Optional[bool] = None
    items: Optional[MuseumItem] = None


class SpecialItemInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    donatedTime: Optional[int] = Field(default=0)
    items: Optional[MuseumItem] = None


class MuseumItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: int = Field(default=0)
    data: str = Field(default="")
