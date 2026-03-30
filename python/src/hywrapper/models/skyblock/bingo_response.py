from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class BingoResponse(HypixelResponse):
    """
    Information about the most recent Bingo.

    Attributes:
        success: Whether the request was successful.
        cause: The cause of the error, if the request failed.
        last_updated: Timestamp of when Bingo was last modified.
        id: Integer ID of the Bingo event.
        name: Name of the Bingo event.
        start: Timestamp of the Bingo event's start.
        end: Timestamp of the Bingo event's end.
        modifier: What type of Bingo event it is.
        goals: A list of [Goal] information.
    """

    model_config = ConfigDict(populate_by_name=True)
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    id: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    start: Optional[int] = Field(default=None)
    end: Optional[int] = Field(default=None)
    modifier: Optional[str] = Field(default=None)
    goals: Optional[List[Goal]] = Field(default=None)
    rate_limit: Optional[RateLimit] = Field(default=None, exclude=True, alias="rateLimit")


class Goal(BaseModel):
    """
    Information about a Bingo goal.

    Attributes:
        id: ID for the goal.
        name: Name of the goal.
        tiers: List of tiers for the goal.
        progress: Current progress for global goals.
        lore: Lore as a string.
        full_lore: Lore as a string list (no different?) // TODO find out
        required_amount: Required amount to complete the goal.
    """

    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    tiers: Optional[List[int]] = Field(default=None)
    progress: Optional[int] = Field(default=None)
    lore: Optional[str] = Field(default=None)
    full_lore: Optional[List[str]] = Field(default=None, alias="fullLore")
    required_amount: Optional[int] = Field(default=None, alias="requiredAmount")
