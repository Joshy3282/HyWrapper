package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class BingoResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val id: Int? = null,
    val name: String? = null,
    val start: Long? = null,
    val end: Long? = null,
    val modifier: String? = null,
    val goals: List<Goal>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Goal(
    val id: String? = null,
    val name: String? = null,
    val tiers: List<Int>? = null,
    val progress: Int? = null,
    val lore: String? = null,
    val fullLore: List<String>? = null,
    val requiredAmount: Int? = null,
)
