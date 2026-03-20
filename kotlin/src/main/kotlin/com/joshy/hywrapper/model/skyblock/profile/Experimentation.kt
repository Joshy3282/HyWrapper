package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class Experimentation(
    val simon: Simon? = null,
    val pairings: Pairings? = null,
    val numbers: Numbers? = null,
    @SerialName("claims_resets")
    val claimsReset: Int? = null,
    @SerialName("claims_resets_timestamp")
    val claimsResetsTimestamp: Long? = null,
    @SerialName("serums_drank")
    val serumsDrank: Int? = null,
    @SerialName("claimed_retroactive_rng")
    val claimedRetroactiveRng: Boolean? = null,
    @SerialName("charge_track_timestamp")
    val chargeTrackTimestamp: Long? = null,
)

@Serializable
data class Simon(
    @SerialName("last_attempt") val lastAttempt: Long? = null,
    @SerialName("last_claimed") val lastClaimed: Long? = null,
    @SerialName("bonus_clicks") val bonusClicks: Int? = null,
    val claimed: Boolean? = null,

    // Tier 0
    @SerialName("attempts_0") val attempts0: Int? = null,
    @SerialName("claims_0") val claims0: Int? = null,
    @SerialName("best_score_0") val bestScore0: Int? = null,

    // Tier 1
    @SerialName("attempts_1") val attempts1: Int? = null,
    @SerialName("claims_1") val claims1: Int? = null,
    @SerialName("best_score_1") val bestScore1: Int? = null,

    // Tier 2
    @SerialName("attempts_2") val attempts2: Int? = null,
    @SerialName("claims_2") val claims2: Int? = null,
    @SerialName("best_score_2") val bestScore2: Int? = null,

    // Tier 3
    @SerialName("attempts_3") val attempts3: Int? = null,
    @SerialName("claims_3") val claims3: Int? = null,
    @SerialName("best_score_3") val bestScore3: Int? = null,

    // Tier 4
    @SerialName("attempts_4") val attempts4: Int? = null,
    @SerialName("claims_4") val claims4: Int? = null,
    @SerialName("best_score_4") val bestScore4: Int? = null,

    // Tier 5
    @SerialName("attempts_5") val attempts5: Int? = null,
    @SerialName("claims_5") val claims5: Int? = null,
    @SerialName("best_score_5") val bestScore5: Int? = null
)

@Serializable
data class Pairings(
    @SerialName("last_attempt") val lastAttempt: Long? = null,
    @SerialName("last_claimed") val lastClaimed: Long? = null,
    @SerialName("bonus_clicks") val bonusClicks: Int? = null,
    val claimed: Boolean? = null,

    // Tier 0
    @SerialName("attempts_0") val attempts0: Int? = null,
    @SerialName("claims_0") val claims0: Int? = null,
    @SerialName("best_score_0") val bestScore0: Int? = null,

    // Tier 1
    @SerialName("attempts_1") val attempts1: Int? = null,
    @SerialName("claims_1") val claims1: Int? = null,
    @SerialName("best_score_1") val bestScore1: Int? = null,

    // Tier 2
    @SerialName("attempts_2") val attempts2: Int? = null,
    @SerialName("claims_2") val claims2: Int? = null,
    @SerialName("best_score_2") val bestScore2: Int? = null,

    // Tier 3
    @SerialName("attempts_3") val attempts3: Int? = null,
    @SerialName("claims_3") val claims3: Int? = null,
    @SerialName("best_score_3") val bestScore3: Int? = null,

    // Tier 4
    @SerialName("attempts_4") val attempts4: Int? = null,
    @SerialName("claims_4") val claims4: Int? = null,
    @SerialName("best_score_4") val bestScore4: Int? = null,

    // Tier 5
    @SerialName("attempts_5") val attempts5: Int? = null,
    @SerialName("claims_5") val claims5: Int? = null,
    @SerialName("best_score_5") val bestScore5: Int? = null
)

@Serializable
data class Numbers(
    @SerialName("last_attempt") val lastAttempt: Long? = null,
    @SerialName("last_claimed") val lastClaimed: Long? = null,
    @SerialName("bonus_clicks") val bonusClicks: Int? = null,
    val claimed: Boolean? = null,

    // Tier 0
    @SerialName("attempts_0") val attempts0: Int? = null,
    @SerialName("claims_0") val claims0: Int? = null,
    @SerialName("best_score_0") val bestScore0: Int? = null,

    // Tier 1
    @SerialName("attempts_1") val attempts1: Int? = null,
    @SerialName("claims_1") val claims1: Int? = null,
    @SerialName("best_score_1") val bestScore1: Int? = null,

    // Tier 2
    @SerialName("attempts_2") val attempts2: Int? = null,
    @SerialName("claims_2") val claims2: Int? = null,
    @SerialName("best_score_2") val bestScore2: Int? = null,

    // Tier 3
    @SerialName("attempts_3") val attempts3: Int? = null,
    @SerialName("claims_3") val claims3: Int? = null,
    @SerialName("best_score_3") val bestScore3: Int? = null,

    // Tier 4
    @SerialName("attempts_4") val attempts4: Int? = null,
    @SerialName("claims_4") val claims4: Int? = null,
    @SerialName("best_score_4") val bestScore4: Int? = null,

    // Tier 5
    @SerialName("attempts_5") val attempts5: Int? = null,
    @SerialName("claims_5") val claims5: Int? = null,
    @SerialName("best_score_5") val bestScore5: Int? = null
)