import { HypixelResponse } from "../../types";

/**
 * Information about the recently ended auctions.
 */
export interface AuctionsEndedResponse extends HypixelResponse {
    /** A list of ended auctions for the past minute. */
    auctions?: EndedAuction[];
}

/**
 * Information about an ended auction.
 */
export interface EndedAuction {
    /** UUID of the auction. */
    auction_id?: string;
    /** UUID of the seller. */
    seller?: string;
    /** UUID of the seller's profile. */
    seller_profile?: string;
    /** UUID of the buyer. */
    buyer?: string;
    /** UUID of the buyer's profile. */
    buyer_profile?: string;
    /** Timestamp of when the auction ended or was purchased. */
    timestamp?: number;
    /** The price the auction was or ended at. */
    price?: number;
    /** Whether or not the auction was a BIN auction. */
    bin?: boolean;
    /** Item data of the auctioned item. */
    item_bytes?: string;
}
