package com.joshy.hywrapper.model.playerdata

import com.joshy.hywrapper.data.playerdata.HousingSetting
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class PlayerResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val player: Player? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Player(
    @SerialName("_id")
    val id: String = "",
    val uuid: String = "",
    val displayname: String = "",
    val firstLogin: Long? = 0,
    val playername: String = "",
    val achievementsOneTime: List<String> = emptyList(),
    val achievementPoints: Long? = 0,
    // TODO stats. See player/Stats
    val housingMeta: HousingMeta? = null,
    val achievementTracking: List<String> = emptyList(),
    // TODO achievements. enum needed?
    val newPackageRank: String = "",
    val networkExp: Long? = 0L,
    // TODO monthly crates. enum needed? done every month? futureproof?
    val eugene: Eugene? = null,
    val channel: String = "",
    val lastAdsenseGenerateTime: Long? = 0L,
    val lastClaimedReward: Long? = 0L,
    val rewardHighScore: Int? = 0,
    val rewardStreak: Int? = 0,
    val totalDailyRewards: Int? = 0,
    val totalRewrads: Int? = 0,
    // TODO socialMedia. enum needed?
    // TODO petConsumables. enum needed?
    val karma: Long? = 0L,
    val monthlyPackageRank: String = "",
    val mostRecentMonthlyPackageRank: String = "",
    // TODO seasonal. bunch of bullshit here
    // TODO challenges. more bullshit
    val vanityMeta: VanityMeta? = null,
    val leveling: Leveling? = null,
    val rankPlusColor: String = "",
    val questSettings: QuestSettings? = null,
    // TODO quests. enum
    val tourney: Tourney? = null,
    val fortuneBuff: Int? = 0,
    val giftedMeta: GiftedMeta? = null,
    val achievementRewardsNew: Map<String, Long> = emptyMap(),
    val main2017Tutorial: Boolean? = null,
    val currentGadget: String = "",
    val achievementSync: AchievementSync? = null,
    val monthylRankColor: String = "",
    // TODO cachedData. enum?
    @SerialName("adsense_tokens")
    val adsenseTokens: Int = 0,
)

@Serializable
data class HousingMeta(
    val tutorialStep: String = "",
    val packages: List<String> = emptyList(),
    val plotSize: String = "",
    val allowedBlocks: List<String> = emptyList(),
    val playerSettings: Map<String, String> = emptyMap(),
    // TODO given cookies
    @SerialName("selectedChannels_v3")
    val selectedChannelsV3: List<String> = emptyList(),
) {
    @Suppress("UNCHECKED_CAST")
    fun <T : Any> getHousingSetting(setting: HousingSetting): T? {
        val raw = playerSettings[setting.name] ?: return null
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
    val dailyTwoKExp: Long? = 0L,
)

@Serializable
data class VanityMeta(
    val packages: List<String> = emptyList(),
)

@Serializable
data class Leveling(
    val claimedRewards: List<Int> = emptyList(),
)

@Serializable
data class QuestSettings(
    val autoActivate: Boolean? = null,
)

@Serializable
data class Tourney(
    @SerialName("first_join_lobby")
    val firstJoinLobby: Long? = 0,
)

@Serializable
data class GiftedMeta(
    val ranksGiven: Int? = 0,
    val rankgiftingmilestones: List<String> = emptyList(),
)

@Serializable
data class AchievementSync(
    @SerialName("quake_tiered")
    val quakeTiered: Int? = 0,
)
