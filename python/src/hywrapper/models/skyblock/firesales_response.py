from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class FiresalesResponse(HypixelResponse):
    """
    Lists all active fire sales.

    Attributes:
        success: Whether the request was successful.
        cause: The cause of the error, if the request failed.
        sales: A list of all active firesales.
    """

    model_config = ConfigDict(populate_by_name=True)
    sales: Optional[List[Sale]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Sale(BaseModel):
    """
    Information about a firesale.

    Attributes:
        itemId: The item ID of the item.
        start: Timestamp of when the firesale begins.
        end: Timestamp of when the firesale ends.
        amount: Amount of items available for purchase.
        price: Cost in gems for each item.
    """

    model_config = ConfigDict(populate_by_name=True)
    itemId: Optional[str] = Field(default=None, alias="item_id")
    start: Optional[int] = Field(default=None)
    end: Optional[int] = Field(default=None)
    amount: Optional[int] = Field(default=None)
    price: Optional[int] = Field(default=None)
