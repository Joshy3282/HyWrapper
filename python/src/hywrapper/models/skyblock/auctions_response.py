from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class AuctionsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    page: int = Field(default=0)
    totalPages: int = Field(default=0)
    totalAuctions: int = Field(default=0)
    lastUpdated: int = Field(default=0)
    auctions: List[Auction] = Field(default=[])
    rateLimit: Optional[RateLimit] = None


class Auction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: str = Field(default="")
    auctioneer: str = Field(default="")
    profileId: str = Field(default="")
    coop: List[str] = Field(default=[])
    start: int = Field(default=0)
    end: int = Field(default=0)
    itemName: str = Field(default="")
    itemLore: str = Field(default="")
    extra: str = Field(default="")
    category: str = Field(default="")
    categories: List[str] = Field(default=[])
    tier: str = Field(default="")
    startingBid: int = Field(default=0)
    itemBytes: str = Field(default="")
    claimed: bool = Field(default=False)
    claimedBidders: List[str] = Field(default=[])
    highestBidAmount: int = Field(default=0)
    lastUpdated: int = Field(default=0)
    bin: bool = Field(default=False)
    bids: List[Bid] = Field(default=[])
    itemUuid: Optional[str] = None


class Bid(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    auctionId: str = Field(default="")
    bidder: str = Field(default="")
    profileId: str = Field(default="")
    amount: int = Field(default=0)
    timestamp: int = Field(default=0)
