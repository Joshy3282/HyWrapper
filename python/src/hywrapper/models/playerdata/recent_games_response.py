from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.game_type import GameType
from hywrapper.models.rate_limit import RateLimit


class RecentGamesResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    uuid: str = Field(default="")
    games: List[RecentGame] = Field(default=[])
    rateLimit: Optional[RateLimit] = None


class RecentGame(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    date: int = Field(default=0)
    gameType: str = Field(default="")
    mode: Optional[str] = None
    map: Optional[str] = None
    ended: Optional[int] = None
    parsedGameType: Optional[GameType] = None
