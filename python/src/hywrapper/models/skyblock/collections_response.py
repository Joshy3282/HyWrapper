from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class CollectionsResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: Optional[int] = Field(default=None)
    version: Optional[str] = Field(default=None)
    collections: Optional[Dict[str, Collection]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Collection(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = Field(default=None)
    items: Optional[Dict[str, CollectionItem]] = Field(default=None)


class CollectionItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = Field(default=None)
    maxTiers: Optional[int] = Field(default=None)
    tiers: Optional[List[CollectionTier]] = Field(default=None)


class CollectionTier(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tier: Optional[int] = Field(default=None)
    amountRequired: Optional[int] = Field(default=None)
    unlocks: Optional[List[str]] = Field(default=None)
