from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class BingoResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: Optional[int] = Field(default=None)
    id: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    start: Optional[int] = Field(default=None)
    end: Optional[int] = Field(default=None)
    modifier: Optional[str] = Field(default=None)
    goals: Optional[List[Goal]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Goal(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    tiers: Optional[List[int]] = Field(default=None)
    progress: Optional[int] = Field(default=None)
    lore: Optional[str] = Field(default=None)
    fullLore: Optional[List[str]] = Field(default=None)
    requiredAmount: Optional[int] = Field(default=None)
