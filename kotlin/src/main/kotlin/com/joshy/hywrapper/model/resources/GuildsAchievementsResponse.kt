package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class GuildsAchievementsResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long = 0L,
    @SerialName("one_time")
    val oneTime: Map<String, GuildOneTimeAchievement> = emptyMap(),
    val tiered: Map<String, GuildTieredAchievement> = emptyMap(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class GuildOneTimeAchievement(
    val name: String = "",
    val description: String = "",
)

@Serializable
data class GuildTieredAchievement(
    val name: String = "",
    val description: String = "",
    val tiers: List<GuildAchievementTier> = emptyList(),
)

@Serializable
data class GuildAchievementTier(
    val tier: Int = 0,
    val amount: Int = 0,
)
