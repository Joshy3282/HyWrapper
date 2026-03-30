from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit

if TYPE_CHECKING:
    from hywrapper.data.skyblock.bazaar_item import BazaarItem


class BazaarResponse(HypixelResponse):
    """
    Information about the Bazaar

    Attributes:
        success: Whether the request was successful.
        cause: The cause of the error, if the request failed.
        last_updated: Timestamp of when the Bazaar was last updated.
        products: A list of [Product] in the Bazaar.
    """

    model_config = ConfigDict(populate_by_name=True)
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    products: Optional[Dict[str, Product]] = Field(default=None)
    rate_limit: Optional[RateLimit] = Field(default=None, exclude=True, alias="rateLimit")

    def get_product(self, item: BazaarItem) -> Optional[Product]:
        """
        Retrieves a product from the bazaar response by item ID.

        Args:
            item: The bazaar item.

        Returns:
            The product data, or None if not found.
        """
        if self.products:
            return self.products.get(item.value)
        return None


class Product(BaseModel):
    """
    Information about a bazaar product.

    Attributes:
        product_id: The item ID of the item.
        sell_summary: A list of sell orders for the item.
        buy_summary: A list of buy orders for the item.
        quick_status: General information about the item.
    """

    model_config = ConfigDict(populate_by_name=True)
    product_id: Optional[str] = Field(default=None, alias="product_id")
    sell_summary: Optional[List[Summary]] = Field(default=None, alias="sell_summary")
    buy_summary: Optional[List[Summary]] = Field(default=None, alias="buy_summary")
    quick_status: Optional[QuickStatus] = Field(default=None, alias="quick_status")


class Summary(BaseModel):
    """
    An order summary for a bazaar product

    Attributes:
        amount: The total amount of items being ordered.
        price_per_unit: The price being paid per unit.
        orders: The amount of orders at this price.
    """

    model_config = ConfigDict(populate_by_name=True)
    amount: Optional[int] = Field(default=None)
    price_per_unit: Optional[float] = Field(default=None, alias="pricePerUnit")
    orders: Optional[int] = Field(default=None)


class QuickStatus(BaseModel):
    """
    General information about an item

    Attributes:
        product_id: The item ID of the item
        sell_price: Current highest sell price
        sell_volume: Total amount of items in sell orders
        sell_moving_week: Total items sold the past week
        sell_orders: Total amount of active sell orders
        buy_price: Current highest buy price
        buy_volume: Total amount of items in buy orders
        buy_moving_week: Total items bought the past week
        buy_orders: Total amount of active buy orders
    """

    model_config = ConfigDict(populate_by_name=True)
    product_id: Optional[str] = Field(default=None, alias="productId")
    sell_price: Optional[float] = Field(default=None, alias="sellPrice")
    sell_volume: Optional[int] = Field(default=None, alias="sellVolume")
    sell_moving_week: Optional[int] = Field(default=None, alias="sellMovingWeek")
    sell_orders: Optional[int] = Field(default=None, alias="sellOrders")
    buy_price: Optional[float] = Field(default=None, alias="buyPrice")
    buy_volume: Optional[int] = Field(default=None, alias="buyVolume")
    buy_moving_week: Optional[int] = Field(default=None, alias="buyMovingWeek")
    buy_orders: Optional[int] = Field(default=None, alias="buyOrders")
