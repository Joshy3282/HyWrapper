from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class NewsResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    items: Optional[List[NewsItem]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class NewsItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)
    link: Optional[str] = Field(default=None)
    item: Optional[NewsMaterial] = None


class NewsMaterial(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    material: Optional[str] = Field(default=None)
