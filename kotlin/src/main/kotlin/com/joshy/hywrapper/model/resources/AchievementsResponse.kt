package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class AchievementsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val achievements: Map<String, GameAchievement>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getAchievementsFor(game: GameType): GameAchievement? {
        return achievements?.get(game.databaseName.lowercase())
            ?: achievements?.get(game.name.lowercase())
    }
}

@Serializable
data class GameAchievement(
    @SerialName("one_time")
    val oneTime: Map<String, OneTimeAchievement>? = null,
    val tiered: Map<String, TieredAchievement>? = null,
    @SerialName("total_points")
    val totalPoints: Int? = null,
    @SerialName("total_legacy_points")
    val totalLegacyPoints: Int? = null,
)

@Serializable
data class OneTimeAchievement(
    val name: String? = null,
    val description: String? = null,
    val points: Int? = null,
    val gamePercentUnlocked: Double? = null,
    val globalPercentUnlocked: Double? = null,
)

@Serializable
data class TieredAchievement(
    val name: String? = null,
    val description: String? = null,
    val tiers: List<AchievementTier>? = null,
)

@Serializable
data class AchievementTier(
    val tier: Int? = null,
    val points: Int? = null,
    val amount: Long? = null,
)
