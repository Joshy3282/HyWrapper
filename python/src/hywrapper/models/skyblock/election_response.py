from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class ElectionResponse(HypixelResponse):
    """
    Information about the current election and next election.

    Attributes:
        success: Whether the request was successful.
        cause: The cause of the error, if the request failed.
        lastUpdated: Timestamp of when the information was last updated.
        mayor: Information about the current mayor and election results.
        current: Information about the next election.
    """

    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: Optional[int] = Field(default=None)
    mayor: Optional[Mayor] = None
    current: Optional[Election] = None
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Mayor(BaseModel):
    """
    Information about the current Mayor.

    Attributes:
        key: Type of mayor (eg; economist {Diaz}, farming {Finnegan}).
        name: Name of the mayor.
        perks: A list of the current mayors perks.
        minister: Information about the current Minister.
        election: Information about the past election.
    """

    model_config = ConfigDict(populate_by_name=True)
    key: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    perks: Optional[List[Perk]] = Field(default=None)
    minister: Optional[Minister] = None
    election: Optional[Election] = None


class Minister(BaseModel):
    """
    Information about the current Minister.

    Attributes:
        key: Type of minister (eg; economist {Diaz}, farming {Finnegan}).
        name: Name of the minister.
        perk: The ministers current perk.
    """

    model_config = ConfigDict(populate_by_name=True)
    key: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    perk: Optional[Perk] = None


class Perk(BaseModel):
    """
    Information about a mayor perk.

    Attributes:
        name: Name of the perk (eg; Pest Eradicator, Volume Trading).
        description: Description about the perk.
        minister: Whether or not the perk is the mayors minister perk.
    """

    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    minister: Optional[bool] = None


class Election(BaseModel):
    """
    Information about an election.

    Attributes:
        year: What year the election is for.
        candidates: A list of Candidate for this election.
    """

    model_config = ConfigDict(populate_by_name=True)
    year: Optional[int] = Field(default=None)
    candidates: Optional[List[Candidate]] = Field(default=None)


class Candidate(BaseModel):
    """
    Information about a candidate.

    Attributes:
        key: Type of candidate (eg; economist {Diaz}, farming {Finnegan}).
        name: Name of the candidate.
        perks: A list of the candidate perks.
        votes: The amount of votes the candidate has.
    """

    model_config = ConfigDict(populate_by_name=True)
    key: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    perks: Optional[List[Perk]] = Field(default=None)
    votes: Optional[int] = Field(default=None)
