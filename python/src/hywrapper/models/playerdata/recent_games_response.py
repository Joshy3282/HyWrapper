from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class RecentGame(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    date: int = 0
    game_type: str = Field(default="", alias="gameType")
    mode: Optional[str] = None
    map: Optional[str] = None
    ended: Optional[int] = None


class RecentGamesResponse(HypixelResponse):
    uuid: str = ""
    games: List[RecentGame] = Field(default_factory=list)
