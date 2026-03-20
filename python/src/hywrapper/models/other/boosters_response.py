from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.game_type import GameType
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class BoostersResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    success: Optional[bool] = Field(default=None)
    boosters: Optional[List[Booster]] = Field(default=None)
    booster_state: Optional[BoosterState] = Field(default=None, alias="boosterState")
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Booster(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = Field(default=None, alias="_id")
    purchaser_uuid: Optional[str] = Field(default=None, alias="purchaserUuid")
    amount: Optional[float] = Field(default=None)
    original_length: Optional[int] = Field(default=None, alias="originalLength")
    length: Optional[int] = Field(default=None)
    game_type: Optional[GameType] = Field(default=None, alias="gameType")
    date_activated: Optional[int] = Field(default=None, alias="dateActivated")
    stacked: Optional[List[str]] = Field(default=None)


class BoosterState(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    decrementing: Optional[bool] = Field(default=None)
