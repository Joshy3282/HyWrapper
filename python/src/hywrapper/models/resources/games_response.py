from __future__ import annotations

from typing import Dict

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class Game(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: int = 0
    name: str = ""
    database_name: str = Field(default="", alias="databaseName")
    mode_names: Dict[str, str] = Field(default_factory=dict, alias="modeNames")
    legacy: bool = False
    retired: bool = False


class GamesResponse(HypixelResponse):
    last_updated: int = Field(default=0, alias="lastUpdated")
    games: Dict[str, Game] = Field(default_factory=dict)
