import { HypixelResponse } from "../../types";

export interface AuctionsEndedResponse extends HypixelResponse {
    auctions?: EndedAuction[];
}

export interface EndedAuction {
    auction_id?: string;
    seller?: string;
    seller_profile?: string;
    buyer?: string;
    buyer_profile?: string;
    timestamp?: number;
    price?: number;
    bin?: boolean;
    item_bytes?: string;
}
