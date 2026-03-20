from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class HousingActiveResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    success: Optional[bool] = Field(default=None)
    houses: Optional[List[House]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class HousingHouseResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    success: Optional[bool] = Field(default=None)
    house: Optional[House] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class House(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: Optional[str] = Field(default=None)
    owner: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    created_at: Optional[int] = Field(default=None, alias="createdAt")
    players: Optional[int] = Field(default=None)
    cookies: Optional[Cookies] = Field(default=None)


class Cookies(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    current: Optional[int] = Field(default=None)
