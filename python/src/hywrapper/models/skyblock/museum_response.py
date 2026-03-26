from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.skyblock.museum_item import MuseumItem as MuseumItemEnum
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class MuseumResponse(HypixelResponse):
    """
    Information about a player's museum.

    :param success: Whether the request was successful.
    :param cause: The cause of the error, if the request failed.
    :param members: Information about each members museum in a coop.
    """

    model_config = ConfigDict(populate_by_name=True)
    members: Optional[Dict[str, MuseumMember]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class MuseumMember(BaseModel):
    """
    Information about a coop member's museum.

    :param value: The museums valuation when apprased.
    :param appraisal: Whether or not the museum has been appraised.
    :param items: A list of information about each donatable item.
    :param special: A list of special items donated (eg; minion skins, the fishes').
    """

    model_config = ConfigDict(populate_by_name=True)
    value: Optional[int] = Field(default=None)
    appraisal: Optional[bool] = None
    items: Optional[Dict[MuseumItemEnum, MuseumItemInfo]] = Field(default=None)
    special: Optional[List[SpecialItemInfo]] = Field(default=None)


class MuseumItemInfo(BaseModel):
    """
    Information about a specific donatable item

    :param time_donated: The timestamp the item was donated to museum.
    :param featured_slot: Slot id of where the item is being featured.
    :param borrowing: Whether the item is donated to museum, but not currently in museum.
    :param item_data: Item data for the donated item.
    """

    model_config = ConfigDict(populate_by_name=True)
    time_donated: Optional[int] = Field(default=None, alias="donated_time")
    featured_slot: Optional[str] = Field(default=None, alias="featured_slot")  # TODO enum
    borrowing: Optional[bool] = None
    item_data: Optional[MuseumItemData] = Field(default=None, alias="items")


class SpecialItemInfo(BaseModel):
    """
    Information about an item donated to the special category

    :param time_donated: The timestamp the item was donated to museum.
    :param item_data: Item data for the donated item.
    """

    model_config = ConfigDict(populate_by_name=True)
    time_donated: Optional[int] = Field(default=None, alias="donated_time")
    item_data: Optional[MuseumItemData] = Field(default=None, alias="items")


class MuseumItemData(BaseModel):
    """
    Item data for a donated item.

    :param type: Unknown
    :param data: gzipped nbt data.
    """

    model_config = ConfigDict(populate_by_name=True)
    type: Optional[int] = Field(default=None)  # TODO what is this
    data: Optional[str] = Field(default=None)
