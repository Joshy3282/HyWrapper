package com.joshy.hywrapper.model.playerdata

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class GuildResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val guild: Guild? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Guild(
    @SerialName("_id")
    val id: String = "",
    val name: String = "",
    @SerialName("name_lower")
    val nameLower: String = "",
    val coins: Int = 0,
    val coinsEver: Int = 0,
    val created: Long = 0L,
    val members: List<Member> = emptyList(),
    val ranks: List<Rank> = emptyList(),
    val achievements: Map<String, Int> = emptyMap(),
    val exp: Long = 0L,
    val tagColor: String = "",
    val banner: Banner? = null,
    val publiclyListed: Boolean? = null,
    val preferredGames: List<String> = emptyList(),
    val description: String = "",
    val chatMute: Long = 0L,
    val tag: String = "",
    val guildExpByGameType: Map<String, Long> = emptyMap(),
) {
    fun getExpFor(game: GameType): Long {
        return guildExpByGameType[game.name] ?: 0L
    }

    val parsedPreferredGames: List<GameType>
        get() =
            preferredGames.mapNotNull {
                runCatching { GameType.valueOf(it) }.getOrNull()
            }
}

@Serializable
data class Member(
    val uuid: String = "",
    val rank: String = "",
    val joined: Long = 0L,
    val questParticipation: Int = 0,
    val mutedTill: Long = 0L,
    val expHistory: Map<String, Int> = emptyMap(),
)

@Serializable
data class Rank(
    val name: String = "",
    val default: Boolean? = null,
    val tag: String? = null,
    val created: Long = 0L,
    val priority: Int = 0,
)

@Serializable
data class Banner(
    @SerialName("Base")
    val base: String = "",
    @SerialName("Patterns")
    val patterns: List<Pattern> = emptyList(),
)

@Serializable
data class Pattern(
    @SerialName("Pattern")
    val pattern: String = "",
    @SerialName("Color")
    val color: String = "",
)
