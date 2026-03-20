from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class Game(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[int] = None
    name: Optional[str] = None
    database_name: Optional[str] = Field(default=None, alias="databaseName")
    mode_names: Optional[Dict[str, str]] = Field(default=None, alias="modeNames")
    legacy: Optional[bool] = None
    retired: Optional[bool] = None


class GamesResponse(HypixelResponse):
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    games: Optional[Dict[str, Game]] = Field(default=None)
