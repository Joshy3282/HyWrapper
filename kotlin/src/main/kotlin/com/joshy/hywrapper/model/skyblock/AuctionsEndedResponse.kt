package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class AuctionsEndedResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val auctions: List<EndedAuction> = emptyList(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class EndedAuction(
    @SerialName("auction_id")
    val auctionId: String = "",
    val seller: String = "",
    @SerialName("seller_profile")
    val sellerProfile: String = "",
    val buyer: String = "",
    @SerialName("buyer_profile")
    val buyerProfile: String = "",
    val timestamp: Long = 0L,
    val price: Int = 0,
    val bin: Boolean? = null,
    @SerialName("item_bytes")
    val itemBytes: String = "",
)
