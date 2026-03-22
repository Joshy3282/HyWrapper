package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

/**
 * Lists all current news entires. These are viewable through Jerry on the island.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property sales A list of all active firesales
 * */
@Serializable
data class FiresalesResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val sales: List<Sale>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

/**
 * Information about a firesale
 *
 * @property itemId The item ID of the item
 * @property start Timestamp of when the firesale begins
 * @property end Timestamp of when the firesale ends
 * @property amount Amount of items available for purchase
 * @property price Cost in gems for each item
 * */
@Serializable
data class Sale(
    @SerialName("item_id")
    val itemId: String? = null,
    val start: Long? = null,
    val end: Long? = null,
    val amount: Int? = null,
    val price: Int? = null,
)
