from __future__ import annotations

from typing import List, Optional

from pydantic import ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit
from hywrapper.models.skyblock.profile_response import Profile


class ProfilesResponse(HypixelResponse):
    """
    Information about a player's profiles

    Attributes:
        success: Whether the request was successful.
        cause: The cause of the error, if the request failed.
        profiles: A list of the player's profiles
    """

    model_config = ConfigDict(populate_by_name=True)
    profiles: Optional[List[Profile]] = Field(default=None)
    rate_limit: Optional[RateLimit] = Field(default=None, exclude=True, alias="rateLimit")
