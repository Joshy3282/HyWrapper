package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

/**
 * Information about the most recent Bingo.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property lastUpdated Timestamp of when Bingo was last modified.
 * @property id Integer ID of the Bingo event.
 * @property name Name of the Bingo event.
 * @property start Timestamp of the Bingo event's start.
 * @property end Timestamp of the Bingo event's end.
 * @property modifier What type of Bingo event it is.
 * @property goals A list of [Goal] information.
 * */
@Serializable
data class BingoResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val id: Int? = null,
    val name: String? = null,
    val start: Long? = null,
    val end: Long? = null,
    val modifier: String? = null, // TODO make this an enum
    val goals: List<Goal>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

/**
 * Information about a Bingo goal.
 *
 * @property id ID for the goal.
 * @property name Name of the goal.
 * @property tiers List of tiers for the goal.
 * @property progress Current progress for global goals.
 * @property lore Lore as a string.
 * @property fullLore Lore as a string list (no different?) // TODO find out
 * @property requiredAmount Required amount to complete the goal.
 * */
@Serializable
data class Goal(
    val id: String? = null,
    val name: String? = null,
    val tiers: List<Int>? = null,
    val progress: Int? = null,
    val lore: String? = null,
    val fullLore: List<String>? = null,
    val requiredAmount: Int? = null,
)
