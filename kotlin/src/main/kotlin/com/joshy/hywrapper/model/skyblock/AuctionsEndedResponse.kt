package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

/**
 * Information about the recently ended auctions.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property auctions A list of [EndedAuction] for the past minute.
 * */
@Serializable
data class AuctionsEndedResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val auctions: List<EndedAuction>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

/**
 * Information about an ended auction.
 *
 * @property auctionId UUID of the auction.
 * @property seller UUID of the seller.
 * @property sellerProfile UUID of the seller's profile.
 * @property buyer UUID of the buyer.
 * @property buyerProfile UUID of the buyer's profile.
 * @property timestamp Timestamp of when the auction ended or was purchased.
 * @property price The price the auction was or ended at.
 * @property bin Whether or not the auction was a BIN auction.
 * @property item Item data of the auctioned item.
 * */
@Serializable
data class EndedAuction(
    @SerialName("auction_id")
    val auctionId: String? = null,
    val seller: String? = null,
    @SerialName("seller_profile")
    val sellerProfile: String? = null,
    val buyer: String? = null,
    @SerialName("buyer_profile")
    val buyerProfile: String? = null,
    val timestamp: Long? = null,
    val price: Int? = null,
    val bin: Boolean? = null,
    @SerialName("item_bytes")
    val item: String? = null,
)
