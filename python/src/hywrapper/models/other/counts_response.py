from __future__ import annotations

from typing import Dict

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class GameCount(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    players: int = 0
    modes: Dict[str, int] = Field(default_factory=dict)


class CountsResponse(HypixelResponse):
    games: Dict[str, GameCount] = Field(default_factory=dict)
    player_count: int = Field(default=0, alias="playerCount")
