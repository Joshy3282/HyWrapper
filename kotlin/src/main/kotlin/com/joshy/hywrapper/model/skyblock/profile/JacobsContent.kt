package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class JacobsContent(
    @SerialName("medals_inv")
    val medalsInv: Map<String, Int> = emptyMap(), // TODO enum
    val perks: Perks? = null,
    val talked: Boolean? = null,
    val contents: Map<String, Content> = emptyMap(),
    @SerialName("unique_brackets")
    val uniqueBrackets: Map<String, List<String>> = emptyMap(), // TODO enum
    val migration: Boolean? = null,
    @SerialName("personal_bests")
    val personalBests: Map<String, Int> = emptyMap(), // TODO enum
)

@Serializable
data class Perks(
    @SerialName("double_drops")
    val doubleDrops: Int = 0,
    @SerialName("farming_level_cap")
    val farmingLevelCap: Int = 0,
    @SerialName("personal_bests")
    val personalBests: Boolean? = null,
)

@Serializable
data class Content(
    val collected: Int = 0,
    @SerialName("claimed_rewards")
    val claimedRewards: Boolean? = null,
    @SerialName("claimed_position")
    val claimedPosition: Int = 0,
    @SerialName("claimed_participants")
    val claimedParticipants: Int = 0,
)
