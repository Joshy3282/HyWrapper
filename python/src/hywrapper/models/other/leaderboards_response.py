from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class LeaderboardsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    leaderboards: Dict[str, List[Leaderboard]] = Field(default={})
    rateLimit: Optional[RateLimit] = None


class Leaderboard(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    path: str = Field(default="")
    prefix: str = Field(default="")
    title: str = Field(default="")
    location: str = Field(default="")
    count: int = Field(default=0)
    leaders: List[str] = Field(default=[])
