from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class CollectionsResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: int = Field(default=0)
    version: str = Field(default="")
    collections: Dict[str, Collection] = Field(default_factory=dict)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Collection(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    items: Dict[str, CollectionItem] = Field(default_factory=dict)


class CollectionItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    maxTiers: int = Field(default=0)
    tiers: List[CollectionTier] = Field(default_factory=list)


class CollectionTier(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tier: int = Field(default=0)
    amountRequired: int = Field(default=0)
    unlocks: List[str] = Field(default_factory=list)
