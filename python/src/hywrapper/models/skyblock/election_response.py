from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class ElectionResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: Optional[int] = Field(default=None)
    mayor: Optional[Mayor] = None
    current: Optional[CurrentElection] = None
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Mayor(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    key: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    perks: Optional[List[Perk]] = Field(default=None)
    minister: Optional[Minister] = None
    election: Optional[PastElection] = None


class Minister(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    key: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    perk: Optional[Perk] = None


class Perk(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    minister: Optional[bool] = None


class PastElection(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    year: Optional[int] = Field(default=None)
    candidates: Optional[List[Candidate]] = Field(default=None)


class CurrentElection(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    year: Optional[int] = Field(default=None)
    candidates: Optional[List[Candidate]] = Field(default=None)


class Candidate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    key: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    perks: Optional[List[Perk]] = Field(default=None)
    votes: Optional[int] = Field(default=None)
