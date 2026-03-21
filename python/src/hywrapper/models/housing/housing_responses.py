from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class HousingActiveResponse(HypixelResponse):
    """
    List of all active Houses.

    Attributes:
        success: Whether the request was successful.
        houses: A list of [House].
        rateLimit: The rate limit information for the request.
    """

    model_config = ConfigDict(populate_by_name=True)
    success: Optional[bool] = Field(default=None)
    houses: Optional[List[House]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class HousingHouseResponse(HypixelResponse):
    """
    Information about a House.

    Attributes:
        success: Whether the request was successful.
        house: The [House] details.
        rateLimit: The rate limit information for the request.
    """

    model_config = ConfigDict(populate_by_name=True)
    success: Optional[bool] = Field(default=None)
    house: Optional[House] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class House(BaseModel):
    """
    House information.

    Attributes:
        uuid: The UUID of the house.
        owner: The UUID of the player who owns the house.
        name: The display name of the house.
        created_at: The timestamp when the house was created.
        players: The current number of players in the house.
        cookies: The [Cookies] statistics for the house.
    """

    model_config = ConfigDict(populate_by_name=True)
    uuid: Optional[str] = Field(default=None)
    owner: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    created_at: Optional[int] = Field(default=None, alias="createdAt")
    players: Optional[int] = Field(default=None)
    cookies: Optional[Cookies] = Field(default=None)


class Cookies(BaseModel):
    """
    Cookie information.

    Attributes:
        current: The current number of cookies the house has received.
    """

    model_config = ConfigDict(populate_by_name=True)
    current: Optional[int] = Field(default=None)


class HousingHousesResponse(HypixelResponse):
    """
    List of a player's houses.

    Attributes:
        success: Whether the request was successful.
        houses: A list of [House] belonging to the player.
        rateLimit: The rate limit information for the request.
    """

    model_config = ConfigDict(populate_by_name=True)
    success: Optional[bool] = Field(default=None)
    houses: Optional[List[House]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)
