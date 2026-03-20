from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class AuctionsResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    page: int = Field(default=0)
    totalPages: int = Field(default=0)
    totalAuctions: int = Field(default=0)
    lastUpdated: int = Field(default=0)
    auctions: List[Auction] = Field(default_factory=list)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Auction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: str = Field(default="")
    auctioneer: str = Field(default="")
    profileId: str = Field(default="", alias="profile_id")
    coop: List[str] = Field(default_factory=list)
    start: int = Field(default=0)
    end: int = Field(default=0)
    itemName: str = Field(default="", alias="item_name")
    itemLore: str = Field(default="", alias="item_lore")
    extra: str = Field(default="")
    category: str = Field(default="")
    categories: List[str] = Field(default_factory=list)
    tier: str = Field(default="")
    startingBid: int = Field(default=0, alias="starting_bid")
    itemBytes: str = Field(default="", alias="item_bytes")
    claimed: bool = Field(default=False)
    claimedBidders: List[str] = Field(default_factory=list, alias="claimed_bidders")
    highestBidAmount: int = Field(default=0, alias="highest_bid_amount")
    lastUpdated: int = Field(default=0, alias="last_updated")
    bin: bool = Field(default=False)
    bids: List[Bid] = Field(default_factory=list)
    itemUuid: Optional[str] = Field(default=None, alias="item_uuid")


class Bid(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    auctionId: str = Field(default="", alias="auction_id")
    bidder: str = Field(default="")
    profileId: str = Field(default="", alias="profile_id")
    amount: int = Field(default=0)
    timestamp: int = Field(default=0)
