from __future__ import annotations

from typing import Dict, List

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class Leaderboard(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    path: str = ""
    prefix: str = ""
    title: str = ""
    location: str = ""
    count: int = 0
    leaders: List[str] = Field(default_factory=list)


class LeaderboardsResponse(HypixelResponse):
    leaderboards: Dict[str, List[Leaderboard]] = Field(default_factory=dict)
