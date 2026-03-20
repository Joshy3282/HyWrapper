from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class RecentGame(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    date: Optional[int] = None
    game_type: Optional[str] = Field(default=None, alias="gameType")
    mode: Optional[str] = None
    map: Optional[str] = None
    ended: Optional[int] = None


class RecentGamesResponse(HypixelResponse):
    uuid: Optional[str] = None
    games: Optional[List[RecentGame]] = Field(default=None)
