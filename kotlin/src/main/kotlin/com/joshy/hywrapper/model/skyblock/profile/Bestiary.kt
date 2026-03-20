package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class Bestiary(
    @SerialName("migrated_stats")
    val migratedStats: Boolean? = null,
    @SerialName("migration")
    val migration: Boolean? = null,
    val kills: Map<String, Int>? = null, // TODO enum
    val deaths: Map<String, Int>? = null, // TODO enum
    val milestone: Milestone? = null,
    val miscellaneous: Miscellaneous? = null
)

@Serializable
data class Milestone(
    @SerialName("last_claimed_milestone")
    val lastClaimedMilestone: Int? = null,
)

@Serializable
data class Miscellaneous(
    @SerialName("max_kills_visible")
    val maxKillsVisible: Boolean? = null,
    @SerialName("milestones_notifications")
    val milestonesNotifications: Boolean? = null,
)