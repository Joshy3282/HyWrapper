from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class NewsResponse(HypixelResponse):
    """
    Lists all current news entires. These are viewable through Jerry on the island.

    @property success Whether the request was successful.
    @property cause The cause of the error, if the request failed.
    @property news The list of current news' information.
    """

    model_config = ConfigDict(populate_by_name=True)
    news: Optional[List[NewsItem]] = Field(default=None, alias="items")
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class NewsItem(BaseModel):
    """
    Information about a news entry

    @property title Title of the entry, ususally a version.
    @property text Description of the entry.
    @property link The link that opens when clicked.
    @property item The item in the menu.
    """

    model_config = ConfigDict(populate_by_name=True)
    title: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)
    link: Optional[str] = Field(default=None)
    item: Optional[NewsMaterial] = None


class NewsMaterial(BaseModel):
    """
    Material of the item.

    @property material The material of the item.
    """

    model_config = ConfigDict(populate_by_name=True)
    material: Optional[str] = Field(default=None)
