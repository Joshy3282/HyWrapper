package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class AuctionsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val page: Int? = null,
    val totalPages: Int? = null,
    val totalAuctions: Int? = null,
    val lastUpdated: Long? = null,
    val auctions: List<Auction>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Auction(
    val uuid: String? = null,
    val auctioneer: String? = null,
    @SerialName("profile_id")
    val profileId: String? = null,
    val coop: List<String>? = null,
    val start: Long? = null,
    val end: Long? = null,
    @SerialName("item_name")
    val itemName: String? = null,
    @SerialName("item_lore")
    val itemLore: String? = null,
    val extra: String? = null,
    val category: String? = null,
    val categories: List<String>? = null,
    val tier: String? = null,
    @SerialName("starting_bid")
    val startingBid: Long? = null,
    @SerialName("item_bytes")
    val itemBytes: String? = null,
    val claimed: Boolean? = null,
    @SerialName("claimed_bidders")
    val claimedBidders: List<String>? = null,
    @SerialName("highest_bid_amount")
    val highestBidAmount: Long? = null,
    @SerialName("last_updated")
    val lastUpdated: Long? = null,
    val bin: Boolean? = null,
    val bids: List<Bid>? = null,
    @SerialName("item_uuid")
    val itemUuid: String? = null,
)

@Serializable
data class Bid(
    @SerialName("auction_id")
    val auctionId: String? = null,
    val bidder: String? = null,
    @SerialName("profile_id")
    val profileId: String? = null,
    val amount: Long? = null,
    val timestamp: Long? = null,
)
