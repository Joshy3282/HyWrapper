package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class QuestsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val quests: Map<String, List<Quest>>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getQuestsFor(game: GameType): List<Quest>? {
        return quests?.get(game.databaseName.lowercase())
            ?: quests?.get(game.name.lowercase())
    }
}

@Serializable
data class Quest(
    val id: String? = null,
    val name: String? = null,
    val description: String? = null,
    val rewards: List<QuestReward>? = null,
    val objectives: List<QuestObjective>? = null,
    val requirements: List<QuestRequirement>? = null,
)

@Serializable
data class QuestReward(
    val type: String? = null,
    val amount: Int? = null,
)

@Serializable
data class QuestObjective(
    val id: String? = null,
    val type: String? = null,
    @SerialName("integer")
    val integerValue: Int? = null,
)

@Serializable
data class QuestRequirement(
    val type: String? = null,
)
