package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class FiresalesResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val sales: List<Sale> = emptyList(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Sale(
    @SerialName("item_id")
    val itemId: String = "",
    val start: Long = 0L,
    val end: Long = 0L,
    val amount: Int = 0,
    val price: Int = 0,
)
