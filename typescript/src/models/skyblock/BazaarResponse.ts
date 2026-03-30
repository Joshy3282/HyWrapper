import { HypixelResponse } from "../../types";
import { BazaarItem } from "../../data/skyblock/BazaarItem";

/**
 * Information about the Bazaar
 */
export interface BazaarResponse extends HypixelResponse {
    /** Timestamp of when the Bazaar was last updated. */
    lastUpdated?: number;
    /** A list of products in the Bazaar. */
    products?: Record<string, Product>;
}

/**
 * Information about a bazaar product.
 */
export interface Product {
    /** The item ID of the item. */
    product_id?: string;
    /** A list of sell orders for the item. */
    sell_summary?: Summary[];
    /** A list of buy orders for the item. */
    buy_summary?: Summary[];
    /** General information about the item. */
    quick_status?: QuickStatus;
}

/**
 * An order summary for a bazaar product
 */
export interface Summary {
    /** The total amount of items being ordered. */
    amount?: number;
    /** The price being paid per unit. */
    pricePerUnit?: number;
    /** The amount of orders at this price. */
    orders?: number;
}

/**
 * General information about an item
 */
export interface QuickStatus {
    /** The item ID of the item */
    productId?: string;
    /** Current highest sell price */
    sellPrice?: number;
    /** Total amount of items in sell orders */
    sellVolume?: number;
    /** Total items sold the past week */
    sellMovingWeek?: number;
    /** Total amount of active sell orders */
    sellOrders?: number;
    /** Current highest buy price */
    buyPrice?: number;
    /** Total amount of items in buy orders */
    buyVolume?: number;
    /** Total items bought the past week */
    buyMovingWeek?: number;
    /** Total amount of active buy orders */
    buyOrders?: number;
}

/**
 * Helper class to provide methods similar to the Kotlin version.
 */
export class BazaarResponseHelper {
    /**
     * Retrieves a product from the bazaar response by item ID.
     *
     * @param response The bazaar response.
     * @param item The bazaar item.
     * @returns The product data, or undefined if not found.
     */
    public static getProduct(response: BazaarResponse, item: BazaarItem): Product | undefined {
        return response.products?.[item];
    }
}
