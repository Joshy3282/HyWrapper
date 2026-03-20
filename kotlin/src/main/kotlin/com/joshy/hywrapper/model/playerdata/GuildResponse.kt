package com.joshy.hywrapper.model.playerdata

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class GuildResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val guild: Guild? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Guild(
    @SerialName("_id")
    val id: String? = null,
    val name: String? = null,
    @SerialName("name_lower")
    val nameLower: String? = null,
    val coins: Int? = null,
    val coinsEver: Int? = null,
    val created: Long? = null,
    val members: List<Member>? = null,
    val ranks: List<Rank>? = null,
    val achievements: Map<String, Int>? = null,
    val exp: Long? = null,
    val tagColor: String? = null,
    val banner: Banner? = null,
    val publiclyListed: Boolean? = null,
    val preferredGames: List<String>? = null,
    val description: String? = null,
    val chatMute: Long? = null,
    val tag: String? = null,
    val guildExpByGameType: Map<String, Long>? = null,
) {
    fun getExpFor(game: GameType): Long {
        return guildExpByGameType?.get(game.name) ?: 0L
    }

    val parsedPreferredGames: List<GameType>
        get() =
            preferredGames?.mapNotNull {
                runCatching { GameType.valueOf(it) }.getOrNull()
            } ?: emptyList()
}

@Serializable
data class Member(
    val uuid: String? = null,
    val rank: String? = null,
    val joined: Long? = null,
    val questParticipation: Int? = null,
    val mutedTill: Long? = null,
    val expHistory: Map<String, Int>? = null,
)

@Serializable
data class Rank(
    val name: String? = null,
    val default: Boolean? = null,
    val tag: String? = null,
    val created: Long? = null,
    val priority: Int? = null,
)

@Serializable
data class Banner(
    @SerialName("Base")
    val base: String? = null,
    @SerialName("Patterns")
    val patterns: List<Pattern>? = null,
)

@Serializable
data class Pattern(
    @SerialName("Pattern")
    val pattern: String? = null,
    @SerialName("Color")
    val color: String? = null,
)
