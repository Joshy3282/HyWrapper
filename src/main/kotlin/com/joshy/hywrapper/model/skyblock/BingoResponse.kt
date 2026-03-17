package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class BingoResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long = 0L,
    val id: Int = 0,
    val name: String = "",
    val start: Long = 0,
    val end: Long = 0,
    val modifier: String = "",
    val goals: List<Goal> = emptyList(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Goal(
    val id: String = "",
    val name: String = "",
    val tiers: List<Int> = emptyList(),
    val progress: Int? = null,
    val lore: String = "",
    val fullLore: List<String> = emptyList(),
    val requiredAmount: Int? = null,
)
