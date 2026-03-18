from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class FiresalesResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    sales: List[Sale] = Field(default=[])
    rateLimit: Optional[RateLimit] = None


class Sale(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    itemId: str = Field(default="")
    start: int = Field(default=0)
    end: int = Field(default=0)
    amount: int = Field(default=0)
    price: int = Field(default=0)
