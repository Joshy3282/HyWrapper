from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class ElectionResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: int = Field(default=0)
    mayor: Optional[Mayor] = None
    current: Optional[CurrentElection] = None
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Mayor(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    key: str = Field(default="")
    name: str = Field(default="")
    perks: List[Perk] = Field(default_factory=list)
    minister: Optional[Minister] = None
    election: Optional[PastElection] = None


class Minister(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    key: str = Field(default="")
    name: str = Field(default="")
    perk: Optional[Perk] = None


class Perk(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    description: str = Field(default="")
    minister: Optional[bool] = None


class PastElection(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    year: int = Field(default=0)
    candidates: List[Candidate] = Field(default_factory=list)


class CurrentElection(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    year: int = Field(default=0)
    candidates: List[Candidate] = Field(default_factory=list)


class Candidate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    key: str = Field(default="")
    name: str = Field(default="")
    perks: List[Perk] = Field(default_factory=list)
    votes: int = Field(default=0)
