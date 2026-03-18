from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class NewsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    items: List[NewsItem] = Field(default=[])
    rateLimit: Optional[RateLimit] = None


class NewsItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str = Field(default="")
    text: str = Field(default="")
    link: str = Field(default="")
    item: Optional[NewsMaterial] = None


class NewsMaterial(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    material: str = Field(default="")
