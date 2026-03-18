from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class CollectionsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    lastUpdated: int = Field(default=0)
    version: str = Field(default="")
    collections: Dict[str, Collection] = Field(default={})
    rateLimit: Optional[RateLimit] = None


class Collection(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    items: Dict[str, CollectionItem] = Field(default={})


class CollectionItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    maxTiers: int = Field(default=0)
    tiers: List[CollectionTier] = Field(default=[])


class CollectionTier(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tier: int = Field(default=0)
    amountRequired: int = Field(default=0)
    unlocks: List[str] = Field(default=[])
