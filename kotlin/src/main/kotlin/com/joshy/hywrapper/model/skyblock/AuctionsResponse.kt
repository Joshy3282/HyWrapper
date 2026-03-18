package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class AuctionsResponse(
    override val success: Boolean = false,
    override val cause: String? = null,

    val page: Int = 0,
    val totalPages: Int = 0,
    val totalAuctions: Int = 0,
    val lastUpdated: Long = 0L,

    val auctions: List<Auction> = emptyList()

) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}


@Serializable
data class Auction(
    val uuid: String = "",
    val auctioneer: String = "",
    @SerialName("profile_id")
    val profileId: String = "",
    val coop: List<String> = emptyList(),
    val start: Long = 0L,
    val end: Long = 0L,
    @SerialName("item_name")
    val itemName: String = "",
    @SerialName("item_lore")
    val itemLore: String = "",
    val extra: String = "",
    val category: String = "",
    val categories: List<String> = emptyList(),
    val tier: String = "",
    @SerialName("starting_bid")
    val startingBid: Long = 0L,
    @SerialName("item_bytes")
    val itemBytes: String = "",
    val claimed: Boolean = false,
    @SerialName("claimed_bidders")
    val claimedBidders: List<String> = emptyList(),
    @SerialName("highest_bid_amount")
    val highestBidAmount: Long = 0L,
    @SerialName("last_updated")
    val lastUpdated: Long = 0L,
    val bin: Boolean = false,
    val bids: List<Bid> = emptyList(),
    @SerialName("item_uuid")
    val itemUuid: String? = null
)

@Serializable
data class Bid(
    @SerialName("auction_id")
    val auctionId: String = "",
    val bidder: String = "",
    @SerialName("profile_id")
    val profileId: String = "",
    val amount: Long = 0L,
    val timestamp: Long = 0L
)