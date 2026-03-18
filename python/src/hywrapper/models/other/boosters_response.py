from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class BoostersResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    boosters: Optional[List[Booster]] = Field(default=[])
    boosterState: Optional[BoosterState] = None
    rateLimit: Optional[RateLimit] = None


class Booster(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(default="")
    purchaserUuid: str = Field(default="")
    amount: float = Field(default=0.0)
    originalLength: int = Field(default=0)
    length: int = Field(default=0)
    gameType: int = Field(default=0)
    dateActivated: int = Field(default=0)
    stacked: Optional[List[str]] = Field(default=[])


class BoosterState(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    decrementing: Optional[bool] = None
