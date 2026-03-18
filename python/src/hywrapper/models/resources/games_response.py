from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class GamesResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    lastUpdated: int = Field(default=0)
    games: Dict[str, Game] = Field(default={})
    rateLimit: Optional[RateLimit] = None


class Game(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: int = Field(default=0)
    name: str = Field(default="")
    databaseName: str = Field(default="")
    modeNames: Dict[str, str] = Field(default={})
    legacy: bool = Field(default=False)
    retired: bool = Field(default=False)
