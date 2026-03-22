package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

/**
 * Information about the current election and next election.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property lastUpdated Timestamp of when the information was last updated.
 * @property mayor Information about the current mayor and election results.
 * @property current Information about the next election.
 * */
@Serializable
data class ElectionResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val mayor: Mayor? = null,
    val current: Election? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

/**
 * Information about the current Mayor.
 *
 * @property key Type of mayor (eg; economist {Diaz}, farming {Finnegan}).
 * @property name Name of the mayor.
 * @property perks A list of the current mayors perks.
 * @property minister Information about the current Minister.
 * @property election Information about the past election.
 * */
@Serializable
data class Mayor(
    val key: String? = null,
    val name: String? = null,
    val perks: List<Perk>? = null,
    val minister: Minister? = null,
    val election: Election? = null,
)

/**
 * Information about the current Minister.
 *
 * @property key Type of minister (eg; economist {Diaz}, farming {Finnegan}).
 * @property name Name of the minister.
 * @property perk The ministers current perk.
 * */
@Serializable
data class Minister(
    val key: String? = null,
    val name: String? = null,
    val perk: Perk? = null,
)


/**
 * Information about a mayor perk.
 *
 * @property name Name of the perk (eg; Pest Eradicator, Volume Trading).
 * @property description Description about the perk.
 * @property minister Whether or not the perk is the mayors minister perk.
 * */
@Serializable
data class Perk(
    val name: String? = null,
    val description: String? = null,
    val minister: Boolean? = null,
)

/**
 * Information about an election.
 *
 * @property year What year the election is for.
 * @property candidates A list of [Candidate] for this election.
 * */
@Serializable
data class Election(
    val year: Int? = null,
    val candidates: List<Candidate>? = null,
)

/**
 * Information about a candidate
 *
 * @property key Type of candidate (eg; economist {Diaz}, farming {Finnegan}).
 * @property name Name of the candidate.
 * @property perks A list of the candidate perks.
 * @property votes The amount of votes the candidate has.
 * */
@Serializable
data class Candidate(
    val key: String? = null,
    val name: String? = null,
    val perks: List<Perk>? = null,
    val votes: Int? = null,
)
