package com.joshy.hywrapper.model.playerdata

import com.joshy.hywrapper.data.playerdata.HousingSetting
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class PlayerResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val player: Player? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Player(
    @SerialName("_id")
    val id: String? = null,
    val uuid: String? = null,
    val displayname: String? = null,
    val firstLogin: Long? = null,
    val playername: String? = null,
    val achievementsOneTime: List<String>? = null,
    val achievementPoints: Long? = null,
    // TODO stats. See player/Stats
    val housingMeta: HousingMeta? = null,
    val achievementTracking: List<String>? = null,
    // TODO achievements. enum needed?
    val newPackageRank: String? = null,
    val networkExp: Long? = null,
    // TODO monthly crates. enum needed? done every month? futureproof?
    val eugene: Eugene? = null,
    val channel: String? = null,
    val lastAdsenseGenerateTime: Long? = null,
    val lastClaimedReward: Long? = null,
    val rewardHighScore: Int? = null,
    val rewardStreak: Int? = null,
    val totalDailyRewards: Int? = null,
    val totalRewrads: Int? = null,
    // TODO socialMedia. enum needed?
    // TODO petConsumables. enum needed?
    val karma: Long? = null,
    val monthlyPackageRank: String? = null,
    val mostRecentMonthlyPackageRank: String? = null,
    // TODO seasonal. bunch of bullshit here
    // TODO challenges. more bullshit
    val vanityMeta: VanityMeta? = null,
    val leveling: Leveling? = null,
    val rankPlusColor: String? = null,
    val questSettings: QuestSettings? = null,
    // TODO quests. enum
    val tourney: Tourney? = null,
    val fortuneBuff: Int? = null,
    val giftedMeta: GiftedMeta? = null,
    val achievementRewardsNew: Map<String, Long>? = null,
    val main2017Tutorial: Boolean? = null,
    val currentGadget: String? = null,
    val achievementSync: AchievementSync? = null,
    val monthylRankColor: String? = null,
    // TODO cachedData. enum?
    @SerialName("adsense_tokens")
    val adsenseTokens: Int? = null,
)

@Serializable
data class HousingMeta(
    val tutorialStep: String? = null,
    val packages: List<String>? = null,
    val plotSize: String? = null,
    val allowedBlocks: List<String>? = null,
    val playerSettings: Map<String, String>? = null,
    // TODO given cookies
    @SerialName("selectedChannels_v3")
    val selectedChannelsV3: List<String>? = null,
) {
    @Suppress("UNCHECKED_CAST")
    fun <T : Any> getHousingSetting(setting: HousingSetting): T? {
        val raw = playerSettings?.get(setting.name) ?: return null
        val valueStr = raw.substringAfter("-")
        val parsed: Any? =
            when (setting.type) {
                Boolean::class -> valueStr.toBooleanStrictOrNull()
                Int::class -> valueStr.toIntOrNull()
                String::class -> valueStr
                else -> valueStr
            }

        return parsed as? T
    }
}

@Serializable
data class Eugene(
    val dailyTwoKExp: Long? = null,
)

@Serializable
data class VanityMeta(
    val packages: List<String>? = null,
)

@Serializable
data class Leveling(
    val claimedRewards: List<Int>? = null,
)

@Serializable
data class QuestSettings(
    val autoActivate: Boolean? = null,
)

@Serializable
data class Tourney(
    @SerialName("first_join_lobby")
    val firstJoinLobby: Long? = null,
)

@Serializable
data class GiftedMeta(
    val ranksGiven: Int? = null,
    val rankgiftingmilestones: List<String>? = null,
)

@Serializable
data class AchievementSync(
    @SerialName("quake_tiered")
    val quakeTiered: Int? = null,
)
