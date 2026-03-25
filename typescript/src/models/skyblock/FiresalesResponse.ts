import { HypixelResponse } from "../../types";

/**
 * Lists all active SkyBlock fire sales.
 */
export interface FiresalesResponse extends HypixelResponse {
    /** A list of all active firesales */
    sales?: Sale[];
}

/**
 * Information about a firesale
 */
export interface Sale {
    /** The item ID of the item */
    item_id?: string;
    /** Timestamp of when the firesale begins */
    start?: number;
    /** Timestamp of when the firesale ends */
    end?: number;
    /** Amount of items available for purchase */
    amount?: number;
    /** Cost in gems for each item */
    price?: number;
}
