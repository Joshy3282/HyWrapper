from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class HousingActiveResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    houses: List[House] = Field(default_factory=list)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class HousingHouseResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    house: Optional[House] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class House(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: str = Field(default="")
    owner: str = Field(default="")
    name: str = Field(default="")
    created_at: int = Field(default=0, alias="createdAt")
    players: int = Field(default=0)
    cookies: Optional[Cookies] = Field(default=None)


class Cookies(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    current: int = Field(default=0)
