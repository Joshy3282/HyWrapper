from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class VanityResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    lastUpdated: int = Field(default=0)
    types: List[Type] = Field(default=[])
    rarities: List[Rarity] = Field(default=[])
    rateLimit: Optional[RateLimit] = None


class Type(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    key: str = Field(default="")
    name: str = Field(default="")
    rarity: Optional[str] = None
    packageValue: str = Field(default="")


class Rarity(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    color: str = Field(default="")
