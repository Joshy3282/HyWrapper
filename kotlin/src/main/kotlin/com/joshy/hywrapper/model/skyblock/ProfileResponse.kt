package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import com.joshy.hywrapper.model.skyblock.profile.*
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient
import kotlinx.serialization.json.JsonElement

@Serializable
data class ProfileResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val profile: Profile? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Profile(
    @SerialName("profile_id")
    val profileId: String? = null,
    @SerialName("community_upgrades")
    val communityUpgrades: CommunityUpgrades? = null,
    val members: Map<String, MemberData>? = null,
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
    @SerialName("skill_tree")
    val skillTree: SkillTree? = null,
    @SerialName("pets_data")
    val petsData: PetsData? = null,
    @SerialName("accessory_bag_storage")
    val accessoryBagStorage: AccessoryBagStorage? = null,
    val leveling: Leveling? = null,
    @SerialName("item_data")
    val itemData: ItemData? = null,
    @SerialName("jacobs_contest")
    val jacobsContent: JacobsContent? = null,
    val currencies: Currencies? = null,
    val foraging: Foraging? = null,
    val dungeons: Dungeons? = null,
    @SerialName("player_id")
    val playerId: String? = null,
    @SerialName("nether_island_player_data")
    val crimsonIslePlayerData: CrimsonIslePlayerData? = null,
    val experimentation: Experimentation? = null,
    @SerialName("foraging_core")
    val foragingCore: ForagingCore? = null,
    val shards: Shards? = null,
    @SerialName("mining_core")
    val miningCore: MiningCore? = null,
    val bestiary: Bestiary? = null,
    val quests: Quests? = null,
    @SerialName("player_stats")
    val playerStats: PlayerStats? = null,
    val inventory: PlayerInventory? = null,
    @SerialName("winter_player_data")
    val winterPlayerData: WinterPlayerData? = null,
    val forge: Forge? = null,
    @SerialName("fairy_soul")
    val fairySoul: FairySoul? = null,
    val temples: Temples? = null,
    @SerialName("shared_inventory")
    val sharedInventory: SharedInventory? = null,
    val attributes: Attributes? = null,
    val slayer: Slayer? = null,
    @SerialName("trophy_fish")
    val trophyFish: Map<String, JsonElement>? = null,
    val objectives: List<Objective>? = null,
    val collection: Map<String, Long>? = null,
)

@Serializable
data class SkillTree(
    val nodes: Map<String, Map<String, JsonElement>>? = null
)

@Serializable
data class Forge(
    @SerialName("forge_processes")
    val forgeProcesses: Map<String, Map<String, JsonElement>>? = null
)

@Serializable
data class GlacitePlayerData(
    // TODO enum
    @SerialName("fossils_donated")
    val fossilsDonated: List<String>? = null,
    @SerialName("fossil_dust")
    val fossilDust: Double? = null,
    // TODO enum
    @SerialName("corpses_looted")
    val corpsesLooted: Map<String, Int>? = null,
    @SerialName("mineshafts_entered")
    val mineshaftsEntered: Int? = null,
)

@Serializable
data class ProfileData(
    @SerialName("bank_account")
    val bankAccount: Double? = null,
    @SerialName("first_join")
    val firstJoin: Long? = null,
    @SerialName("personal_bank_upgrade")
    val personalBankUpgrade: Int? = null,
    @SerialName("cookie_buff_active")
    val cookieBuffActive: Boolean? = null,
)

@Serializable
data class GardenPlayerData(
    val copper: Int? = null,
    @SerialName("larva_consumed")
    val larvaConsumed: Int? = null,
    // TODO enum
    @SerialName("analyzed_greenhouse_crops")
    val analyzedGreenhouseCrops: List<String>? = null,
    // TODO enum
    @SerialName("discovered_greenhouse_crops")
    val discoveredGreenhouseCrops: List<String>? = null,
)

@Serializable
data class AccessoryBagStorage(
    val tuning: Map<String, TuningSlot>? = null,
    // TODO ENUM
    @SerialName("selected_power")
    val selectedPower: String? = null,
    @SerialName("bag_upgrades_purchased")
    val bagUpgradesPurchased: Int? = null,
    // TODO enum
    @SerialName("unlocked_powers")
    val unlockedPowers: List<String>? = null,
    @SerialName("highest_magical_power")
    val highestMagicalPower: Int? = null,
)

@Serializable
data class TuningSlot(
    val health: Int? = null,
    val defense: Int? = null,
    @SerialName("walk_speed")
    val walkSpeed: Int? = null,
    val strength: Int? = null,
    @SerialName("critical_damage")
    val criticalDamage: Int? = null,
    @SerialName("critical_chance")
    val criticalChance: Int? = null,
    @SerialName("attack_speed")
    val attackSpeed: Int? = null,
    val intelligence: Int? = null,
)

@Serializable
data class Leveling(
    val experience: Int? = null,
    // TODO enum
    val completions: Map<String, Int>? = null,
    // TODO enum
    @SerialName("completed_tasks")
    val completedTasks: List<String>? = null,
    @SerialName("highest_pet_score")
    val highestPetScore: Int? = null,
    @SerialName("mining_fiesta_ores_mined")
    val miningFiestaOresMined: Int? = null,
    val migrated: Boolean? = null,
    @SerialName("migrated_completions_2")
    val migratedCompletionsV2: Boolean? = null,
    @SerialName("claimed_talisman")
    val claimedTalisman: Boolean? = null,
    // TODO enum
    @SerialName("bop_bonus")
    val bopBonus: String? = null,
    // TODO enum
    @SerialName("emblem_unlocks")
    val emblemUnlocks: List<String>? = null,
    @SerialName("category_expanded")
    val categoryExpanded: Boolean? = null,
    @SerialName("fishing_festival_sharks_killed")
    val fishingFestivalSharksKilled: Int? = null,
    // TODO enum
    @SerialName("task_sort")
    val taskSort: String? = null,
    // TODO enum
    @SerialName("last_viewed_tasks")
    val lastViewedTasks: List<String>? = null,
    // TODO enum
    @SerialName("selected_symbol")
    val selectedSymbol: String? = null,
)

@Serializable
data class ItemData(
    val soulflow: Int? = null,
    @SerialName("favorite_arrow")
    val favoriteArrow: String? = null,
)

@Serializable
data class Currencies(
    @SerialName("coin_purse")
    val coinPurse: Double? = null,
    @SerialName("motes_purse")
    val motesPurse: Double? = null,
    val essence: Map<String, EssenceInfo>? = null,
)

@Serializable
data class EssenceInfo(
    val current: Int? = null,
)

@Serializable
data class ForagingCore(
    @SerialName("daily_trees_cut_day")
    val dailyTreesCutDay: Int? = null,
    @SerialName("daily_trees_cut")
    val dailyTreesCut: Int? = null,
    @SerialName("daily_gifts")
    val dailyGifts: Int? = null,
    @SerialName("daily_log_cut_day")
    val dailyLogCutDay: Int? = null,
    @SerialName("daily_log_cut")
    val dailyLogCut: List<JsonElement>? = null,
    @SerialName("forests_whispers")
    val forestWhispers: Long? = null,
    @SerialName("forests_whispers_spent")
    val forestWhispersSpent: Long? = null,
    @SerialName("current_daily_effect")
    val currentDailyEffect: String? = null,
    @SerialName("current_daily_effect_last_changed")
    val currentDailyEffectLastChanged: Int? = null,
)

@Serializable
data class Shards(
    val traps: Map<String, JsonElement>? = null,
    @SerialName("shard_sort")
    val shardSort: String? = null,
    @SerialName("fusion_result_sort")
    val fusionResultSort: String? = null,
    val owned: List<ShardOwned>? = null,
)

@Serializable
data class ShardOwned(
    val type: String? = null,
    @SerialName("amount_owned")
    val amountOwned: Int? = null,
    val captured: Long? = null,
)

@Serializable
data class Quests(
    @SerialName("trapper_quest")
    val trapperQuest: TrapperQuest? = null
)

@Serializable
data class TrapperQuest(
    @SerialName("last_task_time")
    val lastTaskTime: Long? = null,
    @SerialName("pelt_count")
    val peltCount: Int? = null,
)

@Serializable
data class WinterPlayerData(
    @SerialName("refined_jyrre_uses")
    val refinedJyrreUses: Int? = null,
)

@Serializable
data class FairySoul(
    @SerialName("fairy_exchanges")
    val fairyExchanges: Int? = null,
    @SerialName("total_collected")
    val totalCollected: Int? = null,
    @SerialName("unspent_souls")
    val unspentSouls: Int? = null,
)

@Serializable
data class Temples(
    @SerialName("unlocked_temples")
    val unlockedTemples: List<String>? = null,
)

@Serializable
data class SharedInventory(
    @SerialName("carnival_mask_inventory_contents")
    val carnivalMaskInventoryContents: InventoryObject? = null,
    @SerialName("candy_inventory_contents")
    val candyInventoryContents: InventoryObject? = null,
)

@Serializable
data class Attributes(
    val stacks: Map<String, Int>? = null, // TODO enum
)

@Serializable
data class Objective(
    val status: String? = null,
    val progress: Double? = null,
    @SerialName("completed_at")
    val completedAt: Long? = null,
    val data: Map<String, String> = emptyMap()
)

@Serializable
data class CommunityUpgrades(
    @SerialName("currently_upgrading")
    val currentlyUpgrading: String? = null,
    @SerialName("upgrade_states")
    val upgradeStates: List<UpgradeState>? = null,
)

@Serializable
data class UpgradeState(
    val upgrade: String? = null,
    val tier: Int? = null,
    @SerialName("started_ms")
    val startedMs: Long? = null,
    @SerialName("started_by")
    val startedBy: String? = null,
    @SerialName("claimed_by")
    val claimedBy: String? = null,
)

@Serializable
data class Banking(
    val balance: Double? = null,
    val transactions: List<Transaction>? = null,
)

@Serializable
data class Transaction(
    val amount: Double? = null,
    val timestamp: Long? = null,
    val action: String? = null,
    @SerialName("initiator_name")
    val initiatorName: String? = null,
)