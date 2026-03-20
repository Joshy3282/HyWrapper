from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class BazaarResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: int = Field(default=0)
    products: Dict[str, Product] = Field(default_factory=dict)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Product(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    productId: str = Field(default="", alias="product_id")
    sellSummary: List[Summary] = Field(default_factory=list, alias="sell_summary")
    buySummary: List[Summary] = Field(default_factory=list, alias="buy_summary")
    quickStatus: Optional[QuickStatus] = Field(default=None, alias="quick_status")


class Summary(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    amount: int = Field(default=0)
    pricePerUnit: float = Field(default=0.0)
    orders: int = Field(default=0)


class QuickStatus(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    productId: str = Field(default="")
    sellPrice: float = Field(default=0.0)
    sellVolume: int = Field(default=0)
    sellMovingWeek: int = Field(default=0)
    sellOrder: int = Field(default=0)
    buyPrice: float = Field(default=0.0)
    buyVolume: int = Field(default=0)
    buyMovingWeek: int = Field(default=0)
    buyOrders: int = Field(default=0)
