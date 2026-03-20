package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class PlayerData(
    // TODO enum
    @SerialName("visited_zones")
    val visitedZones: List<String>? = null,
    @SerialName("last_death")
    val lastDeath: Long? = null,
    // TODO enum
    val perks: Map<String, Int>? = null,
    // TODO enum
    @SerialName("garden_chips")
    val gardenChips: Map<String, Int>? = null,
    @SerialName("active_effects")
    val activeEffects: List<ActiveEffect>? = null,
    // TODO paused_effects
    @SerialName("reaper_peppers_eaten")
    val reaperPeppersEaten: Int? = null,
    // TODO temp_stat_buffs
    @SerialName("death_count")
    val deathCount: Int? = null,
    // TODO disabled_potion_effects
    // TODO enum
    @SerialName("achievement_spawned_island_types")
    val achievementSpawnedIslandTypes: List<String>? = null,
    // TODO enum
    @SerialName("visited_modes")
    val visitedModes: List<String>? = null,
    // TODO enum? meh
    @SerialName("unlocked_coll_tiers")
    val unlockedCollTiers: List<String>? = null,
    // TODO enum
    @SerialName("crafted_generators")
    val craftedGenerators: List<String>? = null,
    @SerialName("fishing_treasure_caught")
    val fishingTreasureCaught: Int? = null,
    // TODO enum
    val experience: Map<String, Double>? = null,
)

@Serializable
data class ActiveEffect(
    val effect: String? = null,
    val level: Int? = null,
    // TODO what is this
    val modifiers: List<String>? = null,
    @SerialName("ticks_remaining")
    val ticksRemaining: Long? = null,
    val infinite: Boolean? = null,
    val flags: Int? = null,
)
