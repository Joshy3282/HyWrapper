import { HypixelResponse } from "../../types";
import { BazaarItem } from "../../data/skyblock/BazaarItem";

export interface BazaarResponse extends HypixelResponse {
    lastUpdated?: number;
    products?: Record<string, Product>;
}

export interface Product {
    product_id?: string;
    sell_summary?: Summary[];
    buy_summary?: Summary[];
    quick_status?: QuickStatus;
}

export interface Summary {
    amount?: number;
    pricePerUnit?: number;
    orders?: number;
}

export interface QuickStatus {
    productId?: string;
    sellPrice?: number;
    sellVolume?: number;
    sellMovingWeek?: number;
    sellOrder?: number;
    buyPrice?: number;
    buyVolume?: number;
    buyMovingWeek?: number;
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
