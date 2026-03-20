from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class Type(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    key: str = ""
    name: str = ""
    rarity: Optional[str] = None
    package_value: str = Field(default="", alias="package")


class Rarity(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = ""
    color: str = ""


class VanityResponse(HypixelResponse):
    last_updated: int = Field(default=0, alias="lastUpdated")
    types: List[Type] = Field(default_factory=list)
    rarities: List[Rarity] = Field(default_factory=list)
