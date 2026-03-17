package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class VanityResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long = 0L,
    val types: List<Type> = emptyList(),
    val rarities: List<Rarity> = emptyList(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Type(
    val key: String = "",
    val name: String = "",
    val rarity: String? = null,
    @SerialName("package")
    val packageValue: String = "",
)

@Serializable
data class Rarity(
    val name: String = "",
    val color: String = "",
)
