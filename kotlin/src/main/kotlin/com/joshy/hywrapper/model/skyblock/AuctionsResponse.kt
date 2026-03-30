package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

/**
 * Information about current auctions
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property page The queried page of auctions
 * @property totalPages Total amount of pages available
 * @property totalAuctions Total amount of auctions active
 * @property lastUpdated Timestamp of the last time auctions were updated
 * @property auctions A list of [Auction]
 * */
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

/**
 * Information about a specific auction.
 *
 * @property uuid The auction UUID.
 * @property auctioneer The UUID of the seller.
 * @property profileId The UUID of the seller's profile.
 * @property coop A list of UUIDs for the seller's coop members.
 * @property start Timetsamp for when the auction started.
 * @property end Timestamp for when the auction ended/sold.
 * @property itemName Name of the item sold.
 * @property itemLore Lore of the item sold (separated by unicode char \u00a7).
 * @property extra Unknown. Item name plus a bunch of attributes like item and enchants.
 * @property category The category of the item in auction house.
 * @property categories The categories of the item in auction house.
 * @property tier Rarity of the item.
 * @property startingBid Starting bid for an auction or price of a bin auction.
 * @property itemBytes Item data for the auctioned item.
 * @property claimed Whether the item has been claimed by the buyer. TODO check this
 * @property claimedBidders Whether the item has been claimed by the buyer's coop. TODO check this
 * @property highestBidAmount The highest bid on the auction.
 * @property lastUpdated Timestamp of the last time the auction was modified or bin on.
 * @property bin Whether the auction is a bin auction.
 * @property bids A list of [Bid] on the auction.
 * @property itemUuid UUID of the item if it is an item with a UUID.
 * */
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

/**
 * Information about a bid on an auction
 *
 * @property auctionId UUID of the auction the bid was on
 * @property bidder UUID of the bidder
 * @property profileId UUID of the bidder's profile
 * @property amount Price bid
 * @property timestamp Timestamp of when the bid was made
 * */
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
