from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class BingoResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    lastUpdated: int = Field(default=0)
    id: int = Field(default=0)
    name: str = Field(default="")
    start: int = Field(default=0)
    end: int = Field(default=0)
    modifier: str = Field(default="")
    goals: List[Goal] = Field(default=[])
    rateLimit: Optional[RateLimit] = None


class Goal(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(default="")
    name: str = Field(default="")
    tiers: List[int] = Field(default=[])
    progress: Optional[int] = None
    lore: str = Field(default="")
    fullLore: List[str] = Field(default=[])
    requiredAmount: Optional[int] = None
