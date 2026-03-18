package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class AchievementsResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long = 0L,
    val achievements: Map<String, GameAchievement> = emptyMap(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getAchievementsFor(game: GameType): GameAchievement? {
        return achievements[game.databaseName.lowercase()]
            ?: achievements[game.name.lowercase()]
    }
}

@Serializable
data class GameAchievement(
    @SerialName("one_time")
    val oneTime: Map<String, OneTimeAchievement> = emptyMap(),
    val tiered: Map<String, TieredAchievement> = emptyMap(),
    @SerialName("total_points")
    val totalPoints: Int = 0,
    @SerialName("total_legacy_points")
    val totalLegacyPoints: Int = 0,
)

@Serializable
data class OneTimeAchievement(
    val name: String = "",
    val description: String = "",
    val points: Int = 0,
    val gamePercentUnlocked: Double? = null,
    val globalPercentUnlocked: Double? = null,
)

@Serializable
data class TieredAchievement(
    val name: String,
    val description: String = "",
    val tiers: List<AchievementTier> = emptyList(),
)

@Serializable
data class AchievementTier(
    val tier: Int = 0,
    val points: Int = 0,
    val amount: Long = 0L,
)
