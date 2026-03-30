from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class AuctionsEndedResponse(HypixelResponse):
    """
    Information about the recently ended auctions.

    Attributes:
        success: Whether the request was successful.
        cause: The cause of the error, if the request failed.
        auctions: A list of [EndedAuction] for the past minute.
    """

    model_config = ConfigDict(populate_by_name=True)
    auctions: Optional[List[EndedAuction]] = Field(default=None)
    rate_limit: Optional[RateLimit] = Field(default=None, exclude=True, alias="rateLimit")


class EndedAuction(BaseModel):
    """
    Information about an ended auction.

    Attributes:
        auction_id: UUID of the auction.
        seller: UUID of the seller.
        seller_profile: UUID of the seller's profile.
        buyer: UUID of the buyer.
        buyer_profile: UUID of the buyer's profile.
        timestamp: Timestamp of when the auction ended or was purchased.
        price: The price the auction was or ended at.
        bin: Whether or not the auction was a BIN auction.
        item: Item data of the auctioned item.
    """

    model_config = ConfigDict(populate_by_name=True)
    auction_id: Optional[str] = Field(default=None, alias="auction_id")
    seller: Optional[str] = Field(default=None)
    seller_profile: Optional[str] = Field(default=None, alias="seller_profile")
    buyer: Optional[str] = Field(default=None)
    buyer_profile: Optional[str] = Field(default=None, alias="buyer_profile")
    timestamp: Optional[int] = Field(default=None)
    price: Optional[int] = Field(default=None)
    bin: Optional[bool] = Field(default=None)
    item: Optional[str] = Field(default=None, alias="item_bytes")
