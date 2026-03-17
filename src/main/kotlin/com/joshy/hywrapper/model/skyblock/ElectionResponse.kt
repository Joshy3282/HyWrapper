package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class ElectionResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long = 0L,
    val mayor: Mayor? = null,
    val current: CurrentElection? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Mayor(
    val key: String = "",
    val name: String = "",
    val perks: List<Perk> = emptyList(),
    val minister: Minister? = null,
    val election: PastElection? = null,
)

@Serializable
data class Minister(
    val key: String = "",
    val name: String = "",
    val perk: Perk? = null,
)

@Serializable
data class Perk(
    val name: String = "",
    val description: String = "",
    val minister: Boolean? = null,
)

@Serializable
data class PastElection(
    val year: Int = 0,
    val candidates: List<Candidate> = emptyList(),
)

@Serializable
data class CurrentElection(
    val year: Int = 0,
    val candidates: List<Candidate> = emptyList(),
)

@Serializable
data class Candidate(
    val key: String = "",
    val name: String = "",
    val perks: List<Perk> = emptyList(),
    val votes: Int = 0,
)
