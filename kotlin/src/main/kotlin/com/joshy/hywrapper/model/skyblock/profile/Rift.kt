package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class Rift(
    val villagePlaza: VillagePlaza? = null,
    val witherCage: WitherCage? = null,
    val blackLagoon: BlackLagoon? = null,
)

@Serializable
data class VillagePlaza(
    val murder: Murder? = null,
    val barryCenter: BarryCenter? = null,
    val cowboy: Cowboy? = null,
    // TODO barter_bank ??
    val lonely: Lonely? = null,
    val seraphine: Seraphine? = null,
    @SerialName("got_scammed")
    val gotScammed: Boolean? = null,
)

@Serializable
data class Murder(
    @SerialName("step_index")
    val stepIndex: Int = 0,
    @SerialName("room_clues")
    val roomClues: List<String> = emptyList(),
    @SerialName("step_index_pt2")
    val stepIndexPt2: Int = 0,
    @SerialName("step_index_pt3")
    val stepIndexPt3: Int = 0,
)

@Serializable
data class BarryCenter(
    @SerialName("first_talk_to_barry")
    val firstTalkToBarry: Boolean? = null,
    val convinced: List<String> = emptyList(),
    @SerialName("received_reward")
    val receivedReward: Boolean? = null,
)

@Serializable
data class Cowboy(
    val stage: Int = 0,
    @SerialName("hay_eaten")
    val hayEaten: Int,
    @SerialName("rabbit_name")
    val rabbitName: String = "",
    @SerialName("exported_carrots")
    val exportedCarrots: Int = 0,
)

@Serializable
data class Lonely(
    @SerialName("seconds_sitting")
    val secondsSitting: Int = 0,
)

@Serializable
data class Seraphine(
    @SerialName("step_index")
    val stepIndex: Int = 0,
)

@Serializable
data class WitherCage(
    @SerialName("killed_eyes")
    val killedEyes: List<String> = emptyList(),
)

@Serializable
data class BlackLagoon(
    @SerialName("talked_to_edwin")
    val talkedToEdwin: Boolean? = null,
    @SerialName("received_science_paper")
    val receivedSciencePaper: Boolean? = null,
    @SerialName("completed_step")
    val completedStep: Int = 0,
    @SerialName("delivered_science_paper")
    val deliveredSciencePaper: Boolean? = null,
)
