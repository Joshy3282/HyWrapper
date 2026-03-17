package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class GamesResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long = 0L,
    val games: Map<String, Game> = emptyMap(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getGameInfo(gameType: GameType): Game? {
        return games[gameType.name]
    }
}

@Serializable
data class Game(
    val id: Int = 0,
    val name: String = "",
    val databaseName: String = "",
    val modeNames: Map<String, String> = emptyMap(),
    val legacy: Boolean = false,
    val retired: Boolean = false,
)
