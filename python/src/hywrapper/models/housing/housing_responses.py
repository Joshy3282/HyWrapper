from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class HousingActiveResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    houses: List[House] = Field(default=[])
    rateLimit: Optional[RateLimit] = None


class HousingHouseResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    house: Optional[House] = None
    rateLimit: Optional[RateLimit] = None


class House(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: str = Field(default="")
    owner: str = Field(default="")
    name: str = Field(default="")
    createdAt: int = Field(default=0)
    players: int = Field(default=0)
    cookies: Optional[Cookies] = None


class Cookies(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    current: int = Field(default=0)
