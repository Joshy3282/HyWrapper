from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class AuctionsResponse(HypixelResponse):
    """
    Information about current auctions

    Attributes:
        success: Whether the request was successful.
        cause: The cause of the error, if the request failed.
        page: The queried page of auctions
        total_pages: Total amount of pages available
        total_auctions: Total amount of auctions active
        last_updated: Timestamp of the last time auctions were updated
        auctions: A list of [Auction]
    """

    model_config = ConfigDict(populate_by_name=True)
    page: Optional[int] = Field(default=None)
    total_pages: Optional[int] = Field(default=None, alias="totalPages")
    total_auctions: Optional[int] = Field(default=None, alias="totalAuctions")
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    auctions: Optional[List[Auction]] = Field(default=None)
    rate_limit: Optional[RateLimit] = Field(default=None, exclude=True, alias="rateLimit")


class Auction(BaseModel):
    """
    Information about a specific auction.

    Attributes:
        uuid: The auction UUID.
        auctioneer: The UUID of the seller.
        profile_id: The UUID of the seller's profile.
        coop: A list of UUIDs for the seller's coop members.
        start: Timetsamp for when the auction started.
        end: Timestamp for when the auction ended/sold.
        item_name: Name of the item sold.
        item_lore: Lore of the item sold (separated by unicode char \u00a7).
        extra: Unknown. Item name plus a bunch of attributes like item and enchants.
        category: The category of the item in auction house.
        categories: The categories of the item in auction house.
        tier: Rarity of the item.
        starting_bid: Starting bid for an auction or price of a bin auction.
        item_bytes: Item data for the auctioned item.
        claimed: Whether the item has been claimed by the buyer. TODO check this
        claimed_bidders: Whether the item has been claimed by the buyer's coop. TODO check this
        highest_bid_amount: The highest bid on the auction.
        last_updated: Timestamp of the last time the auction was modified or bin on.
        bin: Whether the auction is a bin auction.
        bids: A list of [Bid] on the auction.
        item_uuid: UUID of the item if it is an item with a UUID.
    """

    model_config = ConfigDict(populate_by_name=True)
    uuid: Optional[str] = Field(default=None)
    auctioneer: Optional[str] = Field(default=None)
    profile_id: Optional[str] = Field(default=None, alias="profile_id")
    coop: Optional[List[str]] = Field(default=None)
    start: Optional[int] = Field(default=None)
    end: Optional[int] = Field(default=None)
    item_name: Optional[str] = Field(default=None, alias="item_name")
    item_lore: Optional[str] = Field(default=None, alias="item_lore")
    extra: Optional[str] = Field(default=None)
    category: Optional[str] = Field(default=None)
    categories: Optional[List[str]] = Field(default=None)
    tier: Optional[str] = Field(default=None)
    starting_bid: Optional[int] = Field(default=None, alias="starting_bid")
    item_bytes: Optional[str] = Field(default=None, alias="item_bytes")
    claimed: Optional[bool] = Field(default=None)
    claimed_bidders: Optional[List[str]] = Field(default=None, alias="claimed_bidders")
    highest_bid_amount: Optional[int] = Field(default=None, alias="highest_bid_amount")
    last_updated: Optional[int] = Field(default=None, alias="last_updated")
    bin: Optional[bool] = Field(default=None)
    bids: Optional[List[Bid]] = Field(default=None)
    item_uuid: Optional[str] = Field(default=None, alias="item_uuid")


class Bid(BaseModel):
    """
    Information about a bid on an auction

    Attributes:
        auction_id: UUID of the auction the bid was on
        bidder: UUID of the bidder
        profile_id: UUID of the bidder's profile
        amount: Price bid
        timestamp: Timestamp of when the bid was made
    """

    model_config = ConfigDict(populate_by_name=True)
    auction_id: Optional[str] = Field(default=None, alias="auction_id")
    bidder: Optional[str] = Field(default=None)
    profile_id: Optional[str] = Field(default=None, alias="profile_id")
    amount: Optional[int] = Field(default=None)
    timestamp: Optional[int] = Field(default=None)
