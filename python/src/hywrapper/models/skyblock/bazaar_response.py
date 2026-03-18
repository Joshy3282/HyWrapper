from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class BazaarResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    lastUpdated: int = Field(default=0)
    products: Dict[str, Product] = Field(default={})
    rateLimit: Optional[RateLimit] = None


class Product(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    productId: str = Field(default="")
    sellSummary: List[Summary] = Field(default=[])
    buySummary: List[Summary] = Field(default=[])
    quickStatus: Optional[QuickStatus] = None


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
