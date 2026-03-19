package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import com.joshy.hywrapper.model.skyblock.profile.Event
import com.joshy.hywrapper.model.skyblock.profile.PetsData
import com.joshy.hywrapper.model.skyblock.profile.PlayerData
import com.joshy.hywrapper.model.skyblock.profile.Rift
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class ProfileResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val profile: Profile? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Profile(
    @SerialName("profile_id")
    val profileId: String = "",
    @SerialName("community_upgrades")
    val communityUpgrades: CommunityUpgrades? = null,
    val members: Map<String, MemberData> = emptyMap(),
    val banking: Banking? = null,
)

@Serializable
data class MemberData(
    val rift: Rift? = null,
    @SerialName("player_data")
    val playerData: PlayerData? = null,
    @SerialName("glacite_player_data")
    val glacitePlayerData: GlacitePlayerData? = null,
    val profile: ProfileData? = null,
    val event: Event? = null,
    @SerialName("garden_player_data")
    val gardenPlayerData: GardenPlayerData? = null,
    // TODO skill_tree
    @SerialName("pets_data")
    val petsData: PetsData? = null,
    @SerialName("accessory_bag_storage")
    val accessoryBagStorage: AccessoryBagStorage? = null,
    val leveling: Leveling? = null,
    @SerialName("item_data")
    val itemData: ItemData? = null,
)

@Serializable
data class GlacitePlayerData(
    // TODO enum
    @SerialName("fossils_donated")
    val fossilsDonated: List<String> = emptyList(),
    @SerialName("fossil_dust")
    val fossilDust: Double = 0.0,
    // TODO enum
    @SerialName("corpses_looted")
    val corpsesLooted: Map<String, Int> = emptyMap(),
    @SerialName("mineshafts_entered")
    val mineshaftsEntered: Int = 0,
)

@Serializable
data class ProfileData(
    @SerialName("bank_account")
    val bankAccount: Double = 0.0,
    @SerialName("first_join")
    val firstJoin: Long? = 0L,
    @SerialName("personal_bank_upgrade")
    val personalBankUpgrade: Int = 0,
    @SerialName("cookie_buff_active")
    val cookieBuffActive: Boolean? = null,
)

@Serializable
data class GardenPlayerData(
    val copper: Int = 0,
    @SerialName("larva_consumed")
    val larvaConsumed: Int = 0,
    // TODO enum
    @SerialName("analyzed_greenhouse_crops")
    val analyzedGreenhouseCrops: List<String> = emptyList(),
    // TODO enum
    @SerialName("discovered_greenhouse_crops")
    val discoveredGreenhouseCrops: List<String> = emptyList(),
)

@Serializable
data class AccessoryBagStorage(
    val tuning: Map<String, TuningSlot> = emptyMap(),
    // TODO ENUM
    @SerialName("selected_power")
    val selectedPower: String = "",
    @SerialName("bag_upgrades_purchased")
    val bagUpgradesPurchased: Int = 0,
    // TODO enum
    @SerialName("unlocked_powers")
    val unlockedPowers: List<String> = emptyList(),
    @SerialName("highest_magical_power")
    val highestMagicalPower: Int = 0,
)

@Serializable
data class TuningSlot(
    val health: Int = 0,
    val defense: Int = 0,
    @SerialName("walk_speed")
    val walkSpeed: Int = 0,
    val strength: Int = 0,
    @SerialName("critical_damage")
    val criticalDamage: Int = 0,
    @SerialName("critical_chance")
    val criticalChance: Int = 0,
    @SerialName("attack_speed")
    val attackSpeed: Int = 0,
    val intelligence: Int = 0,
)

@Serializable
data class Leveling(
    val experience: Int = 0,
    // TODO enum
    val completions: Map<String, Int> = emptyMap(),
    // TODO enum
    @SerialName("completed_tasks")
    val completedTasks: List<String> = emptyList(),
    @SerialName("highest_pet_score")
    val highestPetScore: Int = 0,
    @SerialName("mining_fiesta_ores_mined")
    val miningFiestaOresMined: Int = 0,
    val migrated: Boolean? = null,
    @SerialName("migrated_completions_2")
    val migratedCompletionsV2: Boolean? = null,
    @SerialName("claimed_talisman")
    val claimedTalisman: Boolean? = null,
    // TODO enum
    @SerialName("bop_bonus")
    val bopBonus: String = "",
    // TODO enum
    @SerialName("emblem_unlocks")
    val emblemUnlocks: List<String> = emptyList(),
    @SerialName("category_expanded")
    val categoryExpanded: Boolean? = null,
    @SerialName("fishing_festival_sharks_killed")
    val fishingFestivalSharksKilled: Int = 0,
    // TODO enum
    @SerialName("task_sort")
    val taskSort: String = "",
    // TODO enum
    @SerialName("last_viewed_tasks")
    val lastViewedTasks: List<String> = emptyList(),
    // TODO enum
    @SerialName("selected_symbol")
    val selectedSymbol: String = "",
)

@Serializable
data class ItemData(
    val soulflow: Int = 0,
    @SerialName("favorite_arrow")
    val favoriteArrow: String = "",
)

@Serializable
data class CommunityUpgrades(
    @SerialName("currently_upgrading")
    val currentlyUpgrading: String = "",
    @SerialName("upgrade_states")
    val upgradeStates: List<UpgradeState> = emptyList(),
)

@Serializable
data class UpgradeState(
    val upgrade: String = "",
    val tier: Int = 1,
    @SerialName("started_ms")
    val startedMs: Long = 0L,
    @SerialName("started_by")
    val startedBy: String = "",
    @SerialName("claimed_by")
    val claimedBy: String = "",
)

@Serializable
data class Banking(
    val balance: Double = 0.0,
    val transactions: List<Transaction> = emptyList(),
)

@Serializable
data class Transaction(
    val amount: Double = 0.0,
    val timestamp: Long = 0L,
    val action: String = "",
    @SerialName("initiator_name")
    val initiatorName: String = "",
)
