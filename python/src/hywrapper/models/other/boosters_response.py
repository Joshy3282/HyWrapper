from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.game_type import GameType
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class BoostersResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    boosters: Optional[List[Booster]] = Field(default_factory=list)
    booster_state: Optional[BoosterState] = Field(default=None, alias="boosterState")
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Booster(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(default="", alias="_id")
    purchaser_uuid: str = Field(default="", alias="purchaserUuid")
    amount: float = Field(default=0.0)
    original_length: int = Field(default=0, alias="originalLength")
    length: int = Field(default=0)
    game_type: Optional[GameType] = Field(default=None, alias="gameType")
    date_activated: int = Field(default=0, alias="dateActivated")
    stacked: Optional[List[str]] = Field(default_factory=list)


class BoosterState(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    decrementing: Optional[bool] = None
