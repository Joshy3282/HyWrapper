package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class PlayerData(
    // TODO enum
    @SerialName("visited_zones")
    val visitedZones: List<String> = emptyList(),
    @SerialName("last_death")
    val lastDeath: Long? = 0L,
    // TODO enum
    val perks: Map<String, Int> = emptyMap(),
    // TODO enum
    @SerialName("garden_chips")
    val gardenChips: Map<String, Int> = emptyMap(),
    @SerialName("active_effects")
    val activeEffects: List<ActiveEffect> = emptyList(),
    // TODO paused_effects
    @SerialName("reaper_peppers_eaten")
    val reaperPeppersEaten: Int = 0,
    // TODO temp_stat_buffs
    @SerialName("death_count")
    val deathCount: Int = 0,
    // TODO disabled_potion_effects
    // TODO enum
    @SerialName("achievement_spawned_island_types")
    val achievementSpawnedIslandTypes: List<String> = emptyList(),
    // TODO enum
    @SerialName("visited_modes")
    val visitedModes: List<String> = emptyList(),
    // TODO enum? meh
    @SerialName("unlocked_coll_tiers")
    val unlockedCollTiers: List<String> = emptyList(),
    // TODO enum
    @SerialName("crafted_generators")
    val craftedGenerators: List<String> = emptyList(),
    @SerialName("fishing_treasure_caught")
    val fishingTreasureCaught: Int = 0,
    // TODO enum
    val experience: Map<String, Double> = emptyMap(),
)

@Serializable
data class ActiveEffect(
    val effect: String = "",
    val level: Int = 0,
    // TODO what is this
    val modifiers: List<String> = emptyList(),
    @SerialName("ticks_remaining")
    val ticksRemaining: Long? = 0L,
    val infinite: Boolean? = null,
    val flags: Int = 0,
)
