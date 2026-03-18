from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class ChallengesResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    lastUpdated: int = Field(default=0)
    challenges: Dict[str, List[Challenge]] = Field(default={})
    rateLimit: Optional[RateLimit] = None


class Challenge(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(default="")
    name: str = Field(default="")
    rewards: List[Reward] = Field(default=[])


class Reward(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = Field(default="")
    amount: int = Field(default=0)
