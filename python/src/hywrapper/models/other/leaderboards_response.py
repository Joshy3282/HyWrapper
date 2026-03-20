from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class Leaderboard(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    path: Optional[str] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    location: Optional[str] = None
    count: Optional[int] = None
    leaders: Optional[List[str]] = Field(default=None)


class LeaderboardsResponse(HypixelResponse):
    leaderboards: Optional[Dict[str, List[Leaderboard]]] = Field(default=None)
