package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class AuctionsEndedResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val auctions: List<EndedAuction>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

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
    val itemBytes: String? = null,
)
