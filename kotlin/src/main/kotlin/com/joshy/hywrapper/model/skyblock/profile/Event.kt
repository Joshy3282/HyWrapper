package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class Event(
    val easter: Easter? = null,
)

@Serializable
data class Easter(
    val rabbits: Rabbits? = null,
    val timeTower: TimeTower? = null,
    // TODO enum
    val employees: Map<String, Int> = emptyMap(),
    val chocolate: Long = 0L,
    @SerialName("total_chocolate")
    val totalChocolate: Long = 0L,
    @SerialName("chocolate_since_prestige")
    val chocolateSincePrestige: Long = 0L,
    @SerialName("last_viewed_chocolate_factory")
    val lastViewedChocolateFactory: Long = 0L,
    val shop: Shop? = null,
    @SerialName("rabbit_barn_capacity_level")
    val rabbitBarnCapacityLevel: Int = 0,
    @SerialName("chocolate_level")
    val chocolateLevel: Int = 0,
    @SerialName("rabbit_sort")
    val rabbitSort: String = "",
    @SerialName("rabbit_filter")
    val rabbitFilter: String = "",
    @SerialName("supreme_chocolate_bars")
    val supremeChocolateBars: Int = 0,
    @SerialName("click_upgrades")
    val clickUpgrades: Int = 0,
    @SerialName("chocolate_multiplier_upgrades")
    val chocolateMultiplierUpgrades: Int = 0,
    @SerialName("rabbit_rarity_upgrades")
    val rabbitRarityUpgrades: Int = 0,
    @SerialName("refined_dark_cacao_truffles")
    val refinedDarkCacaoTruffles: Int = 0,
    @SerialName("el_dorado_progress")
    val elDoradoProgress: Int = 0,
    @SerialName("rabbit_hitmen")
    val rabbitHitmen: RabbitHitmen? = null,
    @SerialName("golden_click_amount")
    val goldenClickAmount: Int = 0,
    @SerialName("golden_click_year")
    val goldenClickYear: Int = 0,
    @SerialName("rabbit_hotspot_filer")
    val rabbitHotspotFiler: String = "",
)

@Serializable
data class Rabbits(
    // TODO enum
    @SerialName("collected_eggs")
    val collectedEggs: Map<String, Long> = emptyMap(),
    // TODO enum
    @SerialName("collected_locations")
    val collectedLocations: Map<String, List<String>> = emptyMap(),
    // TODO rabbits
)

@Serializable
data class TimeTower(
    val charges: Int = 0,
    @SerialName("activation_time")
    val activationTime: Long = 0L,
    val level: Int = 0,
)

@Serializable
data class Shop(
    val year: Int = 0,
    // TODO enum
    val rabbits: List<String> = emptyList(),
    @SerialName("chocolate_spent")
    val chocolateSpent: Long = 0L,
    @SerialName("cocoa_fortune_upgrades")
    val cocoaFortuneUpgrades: Int = 0,
)

@Serializable
data class RabbitHitmen(
    @SerialName("rabbit_hitmen_slots")
    val rabbitHitmenSlots: Int = 0,
    @SerialName("missed_uncollected_eggs")
    val missedUncollectedEggs: Int = 0,
    @SerialName("egg_slot_cooldown_mark")
    val eggSlotCooldownMark: Long = 0L,
    @SerialName("egg_slot_cooldown_sum")
    val eggSlotCooldownSum: Long = 0L,
)
