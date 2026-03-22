package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonElement

@Serializable
data class Event(
    val easter: Easter? = null,
)

@Serializable
data class Easter(
    val rabbits: Map<String, JsonElement>? = null,
    val timeTower: TimeTower? = null,
    // TODO enum
    val employees: Map<String, Int>? = null,
    val chocolate: Long? = null,
    @SerialName("total_chocolate")
    val totalChocolate: Long? = null,
    @SerialName("chocolate_since_prestige")
    val chocolateSincePrestige: Long? = null,
    @SerialName("last_viewed_chocolate_factory")
    val lastViewedChocolateFactory: Long? = null,
    val shop: Shop? = null,
    @SerialName("rabbit_barn_capacity_level")
    val rabbitBarnCapacityLevel: Int? = null,
    @SerialName("chocolate_level")
    val chocolateLevel: Int? = null,
    @SerialName("rabbit_sort")
    val rabbitSort: String? = null,
    @SerialName("rabbit_filter")
    val rabbitFilter: String? = null,
    @SerialName("supreme_chocolate_bars")
    val supremeChocolateBars: Int? = null,
    @SerialName("click_upgrades")
    val clickUpgrades: Int? = null,
    @SerialName("chocolate_multiplier_upgrades")
    val chocolateMultiplierUpgrades: Int? = null,
    @SerialName("rabbit_rarity_upgrades")
    val rabbitRarityUpgrades: Int? = null,
    @SerialName("refined_dark_cacao_truffles")
    val refinedDarkCacaoTruffles: Int? = null,
    @SerialName("el_dorado_progress")
    val elDoradoProgress: Int? = null,
    @SerialName("rabbit_hitmen")
    val rabbitHitmen: RabbitHitmen? = null,
    @SerialName("golden_click_amount")
    val goldenClickAmount: Int? = null,
    @SerialName("golden_click_year")
    val goldenClickYear: Int? = null,
    @SerialName("rabbit_hotspot_filer")
    val rabbitHotspotFiler: String? = null,
)

@Serializable
data class TimeTower(
    val charges: Int? = null,
    @SerialName("activation_time")
    val activationTime: Long? = null,
    val level: Int? = null,
)

@Serializable
data class Shop(
    val year: Int? = null,
    // TODO enum
    val rabbits: List<String>? = null,
    @SerialName("chocolate_spent")
    val chocolateSpent: Long? = null,
    @SerialName("cocoa_fortune_upgrades")
    val cocoaFortuneUpgrades: Int? = null,
)

@Serializable
data class RabbitHitmen(
    @SerialName("rabbit_hitmen_slots")
    val rabbitHitmenSlots: Int? = null,
    @SerialName("missed_uncollected_eggs")
    val missedUncollectedEggs: Int? = null,
    @SerialName("egg_slot_cooldown_mark")
    val eggSlotCooldownMark: Long? = null,
    @SerialName("egg_slot_cooldown_sum")
    val eggSlotCooldownSum: Long? = null,
)
