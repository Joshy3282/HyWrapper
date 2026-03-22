from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class BazaarResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    products: Optional[Dict[str, Product]] = Field(default=None)
    rate_limit: Optional[RateLimit] = Field(default=None, exclude=True, alias="rateLimit")


class Product(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    product_id: Optional[str] = Field(default=None, alias="product_id")
    sell_summary: Optional[List[Summary]] = Field(default=None, alias="sell_summary")
    buy_summary: Optional[List[Summary]] = Field(default=None, alias="buy_summary")
    quick_status: Optional[QuickStatus] = Field(default=None, alias="quick_status")


class Summary(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    amount: Optional[int] = Field(default=None)
    price_per_unit: Optional[float] = Field(default=None, alias="pricePerUnit")
    orders: Optional[int] = Field(default=None)


class QuickStatus(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    product_id: Optional[str] = Field(default=None, alias="productId")
    sell_price: Optional[float] = Field(default=None, alias="sellPrice")
    sell_volume: Optional[int] = Field(default=None, alias="sellVolume")
    sell_moving_week: Optional[int] = Field(default=None, alias="sellMovingWeek")
    sell_order: Optional[int] = Field(default=None, alias="sellOrder")
    buy_price: Optional[float] = Field(default=None, alias="buyPrice")
    buy_volume: Optional[int] = Field(default=None, alias="buyVolume")
    buy_moving_week: Optional[int] = Field(default=None, alias="buyMovingWeek")
    buy_orders: Optional[int] = Field(default=None, alias="buyOrders")
