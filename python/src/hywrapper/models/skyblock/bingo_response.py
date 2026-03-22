from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class BingoResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    id: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    start: Optional[int] = Field(default=None)
    end: Optional[int] = Field(default=None)
    modifier: Optional[str] = Field(default=None)
    goals: Optional[List[Goal]] = Field(default=None)
    rate_limit: Optional[RateLimit] = Field(default=None, exclude=True, alias="rateLimit")


class Goal(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    tiers: Optional[List[int]] = Field(default=None)
    progress: Optional[int] = Field(default=None)
    lore: Optional[str] = Field(default=None)
    full_lore: Optional[List[str]] = Field(default=None, alias="fullLore")
    required_amount: Optional[int] = Field(default=None, alias="requiredAmount")
