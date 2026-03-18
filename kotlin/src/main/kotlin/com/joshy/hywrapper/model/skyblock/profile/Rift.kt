package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class Rift(
    @SerialName("village_plaza")
    val villagePlaza: VillagePlaza? = null,
    @SerialName("wither_cage")
    val witherCage: WitherCage? = null,
    @SerialName("black_lagoon")
    val blackLagoon: BlackLagoon? = null,
    @SerialName("dead_cats")
    val deadCats: DeadCats? = null,
    @SerialName("wizard_tower")
    val wizardTower: WizardTower? = null,
    val enigma: Enigma? = null,
    @SerialName("slayer_quest")
    val slayerQuest: SlayerQuest? = null,
    // TODO enum?
    @SerialName("lifetime_purchased_boundaries")
    val lifetimePurchasedBoundaries: List<String> = emptyList(),
    @SerialName("west_village")
    val westVillage: WestVillage? = null,
    @SerialName("wyld_woods")
    val wyldWoods: WyldWoods? = null,
    val castle: Castle? = null,
    val access: Access? = null,
    val dreadfarm: Dreadfarm? = null,
    val inventory: Inventory? = null,
)

@Serializable
data class VillagePlaza(
    val murder: Murder? = null,
    val barryCenter: BarryCenter? = null,
    val cowboy: Cowboy? = null,
    // TODO barter_bank ??
    val lonely: Lonely? = null,
    val seraphine: Seraphine? = null,
    @SerialName("got_scammed")
    val gotScammed: Boolean? = null,
)

@Serializable
data class Murder(
    @SerialName("step_index")
    val stepIndex: Int = 0,
    @SerialName("room_clues")
    val roomClues: List<String> = emptyList(),
    @SerialName("step_index_pt2")
    val stepIndexPt2: Int = 0,
    @SerialName("step_index_pt3")
    val stepIndexPt3: Int = 0,
)

@Serializable
data class BarryCenter(
    @SerialName("first_talk_to_barry")
    val firstTalkToBarry: Boolean? = null,
    val convinced: List<String> = emptyList(),
    @SerialName("received_reward")
    val receivedReward: Boolean? = null,
)

@Serializable
data class Cowboy(
    val stage: Int = 0,
    @SerialName("hay_eaten")
    val hayEaten: Int,
    @SerialName("rabbit_name")
    val rabbitName: String = "",
    @SerialName("exported_carrots")
    val exportedCarrots: Int = 0,
)

@Serializable
data class Lonely(
    @SerialName("seconds_sitting")
    val secondsSitting: Int = 0,
)

@Serializable
data class Seraphine(
    @SerialName("step_index")
    val stepIndex: Int = 0,
)

@Serializable
data class WitherCage(
    @SerialName("killed_eyes")
    val killedEyes: List<String> = emptyList(),
)

@Serializable
data class BlackLagoon(
    @SerialName("talked_to_edwin")
    val talkedToEdwin: Boolean? = null,
    @SerialName("received_science_paper")
    val receivedSciencePaper: Boolean? = null,
    @SerialName("completed_step")
    val completedStep: Int = 0,
    @SerialName("delivered_science_paper")
    val deliveredSciencePaper: Boolean? = null,
)

@Serializable
data class DeadCats(
    @SerialName("talked_to_jacquelle")
    val talkedToJacquelle: Boolean? = null,
    @SerialName("picked_up_detector")
    val pickedUpDetector: Boolean? = null,
    @SerialName("found_cats")
    val foundCats: List<String> = emptyList(),
    @SerialName("unlocked_pet")
    val unlockedPet: Boolean? = null,
    val montezuma: Montezuma? = null,
)

@Serializable
data class Montezuma(
    // TODO says null so what is this
    val uuid: String? = null,
    val uniqueId: String = "",
    val type: String = "",
    val exp: Double = 0.0,
    val active: Boolean? = null,
    val tier: String = "",
    // TODO same as uuid
    val heldItem: String? = null,
    // TODO
    val candyUsed: Int = 0,
    val petSoulbound: Boolean? = null,
    // TODO
    val skin: String? = null,
    // TODO
    val extra: String? = null,
)

@Serializable
data class WizardTower(
    @SerialName("wizard_quest_step")
    val wizardQuestStep: Int = 0,
    @SerialName("crumbs_laid_out")
    val crumbsLaidOut: Int = 0,
)

@Serializable
data class Enigma(
    @SerialName("bought_cloak")
    val boughtCloak: Boolean? = null,
    // TODO enum
    @SerialName("found_souls")
    val foundSouls: List<String> = emptyList(),
    @SerialName("claimed_bonus_index")
    val claimedBonusIndex: Int = 0,
)

@Serializable
data class Gallery(
    @SerialName("elise_step")
    val eliseStep: Int = 0,
    @SerialName("secured_trophies")
    val securedTrophies: List<SecuredTrophy> = emptyList(),
    // TODO enum maybe? not too helpful
    @SerialName("sent_trophy_dialogues")
    val sentTrophyDialogues: List<String> = emptyList(),
)

@Serializable
data class SecuredTrophy(
    val type: String = "",
    val timestamp: Long = 0L,
    val visits: Int = 0,
)

@Serializable
data class SlayerQuest(
    val type: String = "",
    val tier: Int = 0,
    @SerialName("start_timestamp")
    val startTimestamp: Long = 0L,
    @SerialName("completion_state")
    val completionState: Int = 0,
    @SerialName("used_armor")
    val usedArmor: Boolean? = null,
    val solo: Boolean? = null,
    @SerialName("combat_xp")
    val combatXp: Int = 0,
    @SerialName("recent_mob_kills")
    val recentMobKills: List<RecentMobKill> = emptyList(),
    @SerialName("last_killed_mob_island")
    val lastKilledMobIsland: String = "",
    @SerialName("spawn_timestamp")
    val spawnTimestamp: Long = 0L,
)

@Serializable
data class RecentMobKill(
    val xp: Double = 0.0,
    val timestamp: Long = 0L,
)

@Serializable
data class WestVillage(
    @SerialName("crazy_kloon")
    val crazyKloon: CrazyKloon? = null,
    val mirrorverse: Mirrorverse? = null,
    @SerialName("kat_house")
    val katHouse: KatHouse? = null,
    val glyph: Glyph? = null,
)

@Serializable
data class CrazyKloon(
    // TODO enum
    @SerialName("selected_colors")
    val selectedColors: Map<String, String> = emptyMap(),
    val talked: Boolean? = null,
    // TODO enum??? its just numbers
    @SerialName("hacked_terminals")
    val hackedTerminals: List<String> = emptyList(),
    @SerialName("quest_complete")
    val questComplete: Boolean? = null,
)

@Serializable
data class Mirrorverse(
    // TODO enum
    @SerialName("visited_rooms")
    val visitedRooms: List<String> = emptyList(),
    @SerialName("upside_down_hard")
    val upsideDownHard: Boolean? = null,
    // TODO item enum
    @SerialName("claimed_chest_items")
    val claimedChestItems: List<String> = emptyList(),
    @SerialName("claimed_reward")
    val claimedReward: Boolean? = null,
)

@Serializable
data class KatHouse(
    @SerialName("bin_collected_silverfish")
    val binCollectedSilverfish: Int = 0,
    @SerialName("bin_collected_spider")
    val binCollectedSpider: Int = 0,
    @SerialName("bin_collected_mosquito")
    val binCollectedMosquito: Int = 0,
)

@Serializable
data class Glyph(
    @SerialName("claimed_wand")
    val claimedWand: Boolean? = null,
    @SerialName("current_glyph_delivered")
    val currentGlyphDelivered: Boolean? = null,
    @SerialName("current_glyph_completed")
    val currentGlyphCompleted: Boolean? = null,
    @SerialName("current_glyph")
    val currentGlyph: Int = 0,
    val completed: Boolean? = null,
    @SerialName("claimed_bracelet")
    val claimedBraclet: Boolean? = null,
)

@Serializable
data class WyldWoods(
    @SerialName("sirius_started_q_a")
    val siriusStartedQA: Boolean? = null,
    @SerialName("sirius_q_a_chain_done")
    val siriusQAChainDone: Boolean? = null,
    @SerialName("sirius_completed_q_a")
    val siriusCompletedQA: Boolean? = null,
    @SerialName("sirius_claimed_doubloon")
    val siriusClaimedDoubloon: Boolean? = null,
    // TODO enum?
    @SerialName("talked_threebrothers")
    val talkedThreeBrothers: List<String> = emptyList(),
    @SerialName("bughunter_step")
    val bughunterStep: Int = 0,
)

@Serializable
data class Castle(
    @SerialName("unlocked_pathway_skip")
    val unlockedPathwaySkip: Boolean? = null,
    @SerialName("fairy_step")
    val fairyStep: Int = 0,
    @SerialName("grubber_stacks")
    val grubberStacks: Int = 0,
)

@Serializable
data class Access(
    @SerialName("last_free")
    val lastFree: Long = 0L,
    @SerialName("consumed_prism")
    val consumedPrism: Boolean? = null,
    @SerialName("charge_track_timestamp")
    val chargeTrackTimestamp: Long = 0L,
)

@Serializable
data class Dreadfarm(
    @SerialName("shania_stage")
    val shaniaStage: Int = 0,
    @SerialName("caducous_feeder_uses")
    val caducousFeederUses: List<Long> = emptyList(),
)

@Serializable
data class Inventory(
    @SerialName("inv_contents")
    val invContents: InventoryData? = null,
    @SerialName("inv_armor")
    val invArmor: InventoryData? = null,
    @SerialName("ender_chest_contents")
    val enderChestContents: InventoryData? = null,
    // TODO all null?
    @SerialName("ender_chest_page_icons")
    val enderChestPageIcons: List<InventoryData> = emptyList(),
    @SerialName("equipment_contents")
    val equipmentContents: InventoryData? = null,
)

@Serializable
data class InventoryData(
    val type: Int = 0,
    val data: String = "",
)
