from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class Reward(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None
    amount: Optional[int] = None


class Challenge(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    name: Optional[str] = None
    rewards: Optional[List[Reward]] = Field(default=None)


class ChallengesResponse(HypixelResponse):
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    challenges: Optional[Dict[str, List[Challenge]]] = Field(default=None)
