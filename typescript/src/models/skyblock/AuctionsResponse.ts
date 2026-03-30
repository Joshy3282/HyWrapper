import { HypixelResponse } from "../../types";

/**
 * Information about current auctions
 */
export interface AuctionsResponse extends HypixelResponse {
    /** The queried page of auctions */
    page?: number;
    /** Total amount of pages available */
    totalPages?: number;
    /** Total amount of auctions active */
    totalAuctions?: number;
    /** Timestamp of the last time auctions were updated */
    lastUpdated?: number;
    /** A list of auctions */
    auctions?: Auction[];
}

/**
 * Information about a specific auction.
 */
export interface Auction {
    /** The auction UUID. */
    uuid?: string;
    /** The UUID of the seller. */
    auctioneer?: string;
    /** The UUID of the seller's profile. */
    profile_id?: string;
    /** A list of UUIDs for the seller's coop members. */
    coop?: string[];
    /** Timetsamp for when the auction started. */
    start?: number;
    /** Timestamp for when the auction ended/sold. */
    end?: number;
    /** Name of the item sold. */
    item_name?: string;
    /** Lore of the item sold (separated by unicode char \u00a7). */
    item_lore?: string;
    /** Unknown. Item name plus a bunch of attributes like item and enchants. */
    extra?: string;
    /** The category of the item in auction house. */
    category?: string;
    /** The categories of the item in auction house. */
    categories?: string[];
    /** Rarity of the item. */
    tier?: string;
    /** Starting bid for an auction or price of a bin auction. */
    starting_bid?: number;
    /** Item data for the auctioned item. */
    item_bytes?: string;
    /** Whether the item has been claimed by the buyer. TODO check this */
    claimed?: boolean;
    /** Whether the item has been claimed by the buyer's coop. TODO check this */
    claimed_bidders?: string[];
    /** The highest bid on the auction. */
    highest_bid_amount?: number;
    /** Timestamp of the last time the auction was modified or bin on. */
    last_updated?: number;
    /** Whether the auction is a bin auction. */
    bin?: boolean;
    /** A list of bids on the auction. */
    bids?: Bid[];
    /** UUID of the item if it is an item with a UUID. */
    item_uuid?: string;
}

/**
 * Information about a bid on an auction
 */
export interface Bid {
    /** UUID of the auction the bid was on */
    auction_id?: string;
    /** UUID of the bidder */
    bidder?: string;
    /** UUID of the bidder's profile */
    profile_id?: string;
    /** Price bid */
    amount?: number;
    /** Timestamp of when the bid was made */
    timestamp?: number;
}
