from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class AuctionsResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    page: Optional[int] = Field(default=None)
    totalPages: Optional[int] = Field(default=None)
    totalAuctions: Optional[int] = Field(default=None)
    lastUpdated: Optional[int] = Field(default=None)
    auctions: Optional[List[Auction]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Auction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: Optional[str] = Field(default=None)
    auctioneer: Optional[str] = Field(default=None)
    profileId: Optional[str] = Field(default=None, alias="profile_id")
    coop: Optional[List[str]] = Field(default=None)
    start: Optional[int] = Field(default=None)
    end: Optional[int] = Field(default=None)
    itemName: Optional[str] = Field(default=None, alias="item_name")
    itemLore: Optional[str] = Field(default=None, alias="item_lore")
    extra: Optional[str] = Field(default=None)
    category: Optional[str] = Field(default=None)
    categories: Optional[List[str]] = Field(default=None)
    tier: Optional[str] = Field(default=None)
    startingBid: Optional[int] = Field(default=None, alias="starting_bid")
    itemBytes: Optional[str] = Field(default=None, alias="item_bytes")
    claimed: Optional[bool] = Field(default=None)
    claimedBidders: Optional[List[str]] = Field(default=None, alias="claimed_bidders")
    highestBidAmount: Optional[int] = Field(default=None, alias="highest_bid_amount")
    lastUpdated: Optional[int] = Field(default=None, alias="last_updated")
    bin: Optional[bool] = Field(default=None)
    bids: Optional[List[Bid]] = Field(default=None)
    itemUuid: Optional[str] = Field(default=None, alias="item_uuid")


class Bid(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    auctionId: Optional[str] = Field(default=None, alias="auction_id")
    bidder: Optional[str] = Field(default=None)
    profileId: Optional[str] = Field(default=None, alias="profile_id")
    amount: Optional[int] = Field(default=None)
    timestamp: Optional[int] = Field(default=None)
