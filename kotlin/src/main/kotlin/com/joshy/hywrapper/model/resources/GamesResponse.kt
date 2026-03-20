package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class GamesResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val games: Map<String, Game>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getGameInfo(gameType: GameType): Game? {
        return games?.get(gameType.name)
    }
}

@Serializable
data class Game(
    val id: Int? = null,
    val name: String? = null,
    val databaseName: String? = null,
    val modeNames: Map<String, String>? = null,
    val legacy: Boolean? = null,
    val retired: Boolean? = null,
)
