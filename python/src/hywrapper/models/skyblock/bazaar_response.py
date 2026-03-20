from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class BazaarResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: Optional[int] = Field(default=None)
    products: Optional[Dict[str, Product]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Product(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    productId: Optional[str] = Field(default=None, alias="product_id")
    sellSummary: Optional[List[Summary]] = Field(default=None, alias="sell_summary")
    buySummary: Optional[List[Summary]] = Field(default=None, alias="buy_summary")
    quickStatus: Optional[QuickStatus] = Field(default=None, alias="quick_status")


class Summary(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    amount: Optional[int] = Field(default=None)
    pricePerUnit: Optional[float] = Field(default=None)
    orders: Optional[int] = Field(default=None)


class QuickStatus(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    productId: Optional[str] = Field(default=None)
    sellPrice: Optional[float] = Field(default=None)
    sellVolume: Optional[int] = Field(default=None)
    sellMovingWeek: Optional[int] = Field(default=None)
    sellOrder: Optional[int] = Field(default=None)
    buyPrice: Optional[float] = Field(default=None)
    buyVolume: Optional[int] = Field(default=None)
    buyMovingWeek: Optional[int] = Field(default=None)
    buyOrders: Optional[int] = Field(default=None)
