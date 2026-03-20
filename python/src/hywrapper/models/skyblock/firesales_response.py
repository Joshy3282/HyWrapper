from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class FiresalesResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    sales: List[Sale] = Field(default_factory=list)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Sale(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    itemId: str = Field(default="", alias="item_id")
    start: int = Field(default=0)
    end: int = Field(default=0)
    amount: int = Field(default=0)
    price: int = Field(default=0)
