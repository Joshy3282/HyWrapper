package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class GuildsAchievementsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    @SerialName("one_time")
    val oneTime: Map<String, GuildOneTimeAchievement>? = null,
    val tiered: Map<String, GuildTieredAchievement>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class GuildOneTimeAchievement(
    val name: String? = null,
    val description: String? = null,
)

@Serializable
data class GuildTieredAchievement(
    val name: String? = null,
    val description: String? = null,
    val tiers: List<GuildAchievementTier>? = null,
)

@Serializable
data class GuildAchievementTier(
    val tier: Int? = null,
    val amount: Int? = null,
)
