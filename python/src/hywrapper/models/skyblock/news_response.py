from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class NewsResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    items: List[NewsItem] = Field(default_factory=list)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class NewsItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str = Field(default="")
    text: str = Field(default="")
    link: str = Field(default="")
    item: Optional[NewsMaterial] = None


class NewsMaterial(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    material: str = Field(default="")
