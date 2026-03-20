package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class VanityResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val types: List<Type>? = null,
    val rarities: List<Rarity>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Type(
    val key: String? = null,
    val name: String? = null,
    val rarity: String? = null,
    @SerialName("package")
    val packageValue: String? = null,
)

@Serializable
data class Rarity(
    val name: String? = null,
    val color: String? = null,
)
