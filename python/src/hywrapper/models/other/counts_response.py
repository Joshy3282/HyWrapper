from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class CountsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    games: Dict[str, GameCount] = Field(default={})
    playerCount: int = Field(default=0)
    rateLimit: Optional[RateLimit] = None


class GameCount(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    players: int = Field(default=0)
    modes: Dict[str, int] = Field(default={})
