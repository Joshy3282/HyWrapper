from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class AuctionsEndedResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    auctions: List[EndedAuction] = Field(default=[])
    rateLimit: Optional[RateLimit] = None


class EndedAuction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    auctionId: str = Field(default="")
    seller: str = Field(default="")
    sellerProfile: str = Field(default="")
    buyer: str = Field(default="")
    buyerProfile: str = Field(default="")
    timestamp: int = Field(default=0)
    price: int = Field(default=0)
    bin: Optional[bool] = None
    itemBytes: str = Field(default="")
