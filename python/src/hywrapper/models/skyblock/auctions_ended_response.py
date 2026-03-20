from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class AuctionsEndedResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    auctions: List[EndedAuction] = Field(default_factory=list)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class EndedAuction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    auctionId: str = Field(default="", alias="auction_id")
    seller: str = Field(default="")
    sellerProfile: str = Field(default="", alias="seller_profile")
    buyer: str = Field(default="")
    buyerProfile: str = Field(default="", alias="buyer_profile")
    timestamp: int = Field(default=0)
    price: int = Field(default=0)
    bin: Optional[bool] = None
    itemBytes: str = Field(default="", alias="item_bytes")
