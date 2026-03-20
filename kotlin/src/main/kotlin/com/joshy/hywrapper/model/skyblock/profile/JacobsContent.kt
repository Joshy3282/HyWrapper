package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class JacobsContent(
    @SerialName("medals_inv")
    val medalsInv: Map<String, Int>? = null, // TODO enum
    val perks: Perks? = null,
    val talked: Boolean? = null,
    val contents: Map<String, Content>? = null,
    @SerialName("unique_brackets")
    val uniqueBrackets: Map<String, List<String>>? = null, // TODO enum
    val migration: Boolean? = null,
    @SerialName("personal_bests")
    val personalBests: Map<String, Int>? = null, // TODO enum
)

@Serializable
data class Perks(
    @SerialName("double_drops")
    val doubleDrops: Int? = null,
    @SerialName("farming_level_cap")
    val farmingLevelCap: Int? = null,
    @SerialName("personal_bests")
    val personalBests: Boolean? = null,
)

@Serializable
data class Content(
    val collected: Int? = null,
    @SerialName("claimed_rewards")
    val claimedRewards: Boolean? = null,
    @SerialName("claimed_position")
    val claimedPosition: Int? = null,
    @SerialName("claimed_participants")
    val claimedParticipants: Int? = null,
)
