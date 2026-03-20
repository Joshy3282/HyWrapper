from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class FiresalesResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    sales: Optional[List[Sale]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Sale(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    itemId: Optional[str] = Field(default=None, alias="item_id")
    start: Optional[int] = Field(default=None)
    end: Optional[int] = Field(default=None)
    amount: Optional[int] = Field(default=None)
    price: Optional[int] = Field(default=None)
