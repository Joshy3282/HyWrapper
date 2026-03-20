package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class Slayer(
    @SerialName("slayer_quest")
    val slayerQuest: OngoingSlayerQuest? = null,
    @SerialName("slayer_bosses")
    val slayerBosses: Map<String, SlayerData>? = null, // TODO enum
)

@Serializable
data class OngoingSlayerQuest(
    val type: String? = null, // TODO enum
    val tier: Int? = null, // TODO enum
    @SerialName("start_timestamp")
    val startTimestamp: Long? = null,
    @SerialName("completion_state")
    val completionState: Int? = null,
    @SerialName("used_armor")
    val usedArmor: Boolean? = null,
    val solo: Boolean? = null,
)

@Serializable
data class SlayerData(
    @SerialName("claimed_levels")
    val claimedLevels: Map<String, Boolean> = emptyMap(),
    val xp: Long? = null,
    @SerialName("boss_kills_tier_0") val bossKillsTier0: Int? = null,
    @SerialName("boss_kills_tier_1") val bossKillsTier1: Int? = null,
    @SerialName("boss_kills_tier_2") val bossKillsTier2: Int? = null,
    @SerialName("boss_kills_tier_3") val bossKillsTier3: Int? = null,
    @SerialName("boss_kills_tier_4") val bossKillsTier4: Int? = null,
    @SerialName("boss_attempts_tier_0") val bossAttemptsTier0: Int? = null,
    @SerialName("boss_attempts_tier_1") val bossAttemptsTier1: Int? = null,
    @SerialName("boss_attempts_tier_2") val bossAttemptsTier2: Int? = null,
    @SerialName("boss_attempts_tier_3") val bossAttemptsTier3: Int? = null,
    @SerialName("boss_attempts_tier_4") val bossAttemptsTier4: Int? = null,
)