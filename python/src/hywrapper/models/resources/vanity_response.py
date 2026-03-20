from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class Type(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    key: Optional[str] = None
    name: Optional[str] = None
    rarity: Optional[str] = None
    package_value: Optional[str] = Field(default=None, alias="package")


class Rarity(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = None
    color: Optional[str] = None


class VanityResponse(HypixelResponse):
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    types: Optional[List[Type]] = Field(default=None)
    rarities: Optional[List[Rarity]] = Field(default=None)
