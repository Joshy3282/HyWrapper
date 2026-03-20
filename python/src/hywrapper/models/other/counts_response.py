from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class GameCount(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    players: Optional[int] = None
    modes: Optional[Dict[str, int]] = Field(default=None)


class CountsResponse(HypixelResponse):
    games: Optional[Dict[str, GameCount]] = Field(default=None)
    player_count: Optional[int] = Field(default=None, alias="playerCount")
