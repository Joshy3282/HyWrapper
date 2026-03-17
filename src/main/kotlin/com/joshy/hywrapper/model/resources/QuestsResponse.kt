package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class QuestsResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long = 0L,
    val quests: Map<String, List<Quest>> = emptyMap(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getQuestsFor(game: GameType): List<Quest> {
        return quests[game.databaseName.lowercase()]
            ?: quests[game.name.lowercase()]
            ?: emptyList()
    }
}

@Serializable
data class Quest(
    val id: String = "",
    val name: String = "",
    val description: String = "",
    val rewards: List<QuestReward> = emptyList(),
    val objectives: List<QuestObjective> = emptyList(),
    val requirements: List<QuestRequirement> = emptyList(),
)

@Serializable
data class QuestReward(
    val type: String = "",
    val amount: Int = 0,
)

@Serializable
data class QuestObjective(
    val id: String = "",
    val type: String = "",
    @SerialName("integer")
    val integerValue: Int? = null,
)

@Serializable
data class QuestRequirement(
    val type: String = "",
)
