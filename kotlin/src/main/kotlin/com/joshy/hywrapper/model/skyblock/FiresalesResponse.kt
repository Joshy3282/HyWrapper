package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class FiresalesResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val sales: List<Sale>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Sale(
    @SerialName("item_id")
    val itemId: String? = null,
    val start: Long? = null,
    val end: Long? = null,
    val amount: Int? = null,
    val price: Int? = null,
)
