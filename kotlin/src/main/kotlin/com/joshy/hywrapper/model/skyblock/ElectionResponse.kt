package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class ElectionResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val mayor: Mayor? = null,
    val current: CurrentElection? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Mayor(
    val key: String? = null,
    val name: String? = null,
    val perks: List<Perk>? = null,
    val minister: Minister? = null,
    val election: PastElection? = null,
)

@Serializable
data class Minister(
    val key: String? = null,
    val name: String? = null,
    val perk: Perk? = null,
)

@Serializable
data class Perk(
    val name: String? = null,
    val description: String? = null,
    val minister: Boolean? = null,
)

@Serializable
data class PastElection(
    val year: Int? = null,
    val candidates: List<Candidate>? = null,
)

@Serializable
data class CurrentElection(
    val year: Int? = null,
    val candidates: List<Candidate>? = null,
)

@Serializable
data class Candidate(
    val key: String? = null,
    val name: String? = null,
    val perks: List<Perk>? = null,
    val votes: Int? = null,
)
