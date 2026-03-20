from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class AuctionsEndedResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    auctions: Optional[List[EndedAuction]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class EndedAuction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    auctionId: Optional[str] = Field(default=None, alias="auction_id")
    seller: Optional[str] = Field(default=None)
    sellerProfile: Optional[str] = Field(default=None, alias="seller_profile")
    buyer: Optional[str] = Field(default=None)
    buyerProfile: Optional[str] = Field(default=None, alias="buyer_profile")
    timestamp: Optional[int] = Field(default=None)
    price: Optional[int] = Field(default=None)
    bin: Optional[bool] = Field(default=None)
    itemBytes: Optional[str] = Field(default=None, alias="item_bytes")
