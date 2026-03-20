from __future__ import annotations

from typing import Dict, List

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class Reward(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = ""
    amount: int = 0


class Challenge(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = ""
    name: str = ""
    rewards: List[Reward] = Field(default_factory=list)


class ChallengesResponse(HypixelResponse):
    last_updated: int = Field(default=0, alias="lastUpdated")
    challenges: Dict[str, List[Challenge]] = Field(default_factory=dict)
