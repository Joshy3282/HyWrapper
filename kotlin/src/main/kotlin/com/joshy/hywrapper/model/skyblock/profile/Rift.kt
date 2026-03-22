package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonElement

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
    val lifetimePurchasedBoundaries: List<String>? = null,
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
    @SerialName("barter_bank")
    val barterBank: Map<String, JsonElement>? = null,
    val lonely: Lonely? = null,
    val seraphine: Seraphine? = null,
    @SerialName("got_scammed")
    val gotScammed: Boolean? = null,
)

@Serializable
data class Murder(
    @SerialName("step_index")
    val stepIndex: Int? = null,
    @SerialName("room_clues")
    val roomClues: List<String>? = null,
    @SerialName("step_index_pt2")
    val stepIndexPt2: Int? = null,
    @SerialName("step_index_pt3")
    val stepIndexPt3: Int? = null,
)

@Serializable
data class BarryCenter(
    @SerialName("first_talk_to_barry")
    val firstTalkToBarry: Boolean? = null,
    val convinced: List<String>? = null,
    @SerialName("received_reward")
    val receivedReward: Boolean? = null,
)

@Serializable
data class Cowboy(
    val stage: Int? = null,
    @SerialName("hay_eaten")
    val hayEaten: Int? = null,
    @SerialName("rabbit_name")
    val rabbitName: String? = null,
    @SerialName("exported_carrots")
    val exportedCarrots: Int? = null,
)

@Serializable
data class Lonely(
    @SerialName("seconds_sitting")
    val secondsSitting: Int? = null,
)

@Serializable
data class Seraphine(
    @SerialName("step_index")
    val stepIndex: Int? = null,
)

@Serializable
data class WitherCage(
    @SerialName("killed_eyes")
    val killedEyes: List<String>? = null,
)

@Serializable
data class BlackLagoon(
    @SerialName("talked_to_edwin")
    val talkedToEdwin: Boolean? = null,
    @SerialName("received_science_paper")
    val receivedSciencePaper: Boolean? = null,
    @SerialName("completed_step")
    val completedStep: Int? = null,
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
    val foundCats: List<String>? = null,
    @SerialName("unlocked_pet")
    val unlockedPet: Boolean? = null,
    val montezuma: Montezuma? = null,
)

@Serializable
data class Montezuma(
    val uuid: String? = null,
    val uniqueId: String? = null,
    val type: String? = null,
    val exp: Double? = null,
    val active: Boolean? = null,
    val tier: String? = null,
    @SerialName("held_item")
    val heldItem: String? = null,
    @SerialName("candy_used")
    val candyUsed: Int? = null,
    @SerialName("pet_soulbound")
    val petSoulbound: Boolean? = null,
    val skin: String? = null,
    val extra: Map<String, JsonElement>? = null,
)

@Serializable
data class WizardTower(
    @SerialName("wizard_quest_step")
    val wizardQuestStep: Int? = null,
    @SerialName("crumbs_laid_out")
    val crumbsLaidOut: Int? = null,
)

@Serializable
data class Enigma(
    @SerialName("bought_cloak")
    val boughtCloak: Boolean? = null,
    // TODO enum
    @SerialName("found_souls")
    val foundSouls: List<String>? = null,
    @SerialName("claimed_bonus_index")
    val claimedBonusIndex: Int? = null,
)

@Serializable
data class Gallery(
    @SerialName("elise_step")
    val eliseStep: Int? = null,
    @SerialName("secured_trophies")
    val securedTrophies: List<SecuredTrophy>? = null,
    // TODO enum maybe? not too helpful
    @SerialName("sent_trophy_dialogues")
    val sentTrophyDialogues: List<String>? = null,
)

@Serializable
data class SecuredTrophy(
    val type: String? = null,
    val timestamp: Long? = null,
    val visits: Int? = null,
)

@Serializable
data class SlayerQuest(
    val type: String? = null,
    val tier: Int? = null,
    @SerialName("start_timestamp")
    val startTimestamp: Long? = null,
    @SerialName("completion_state")
    val completionState: Int? = null,
    @SerialName("used_armor")
    val usedArmor: Boolean? = null,
    val solo: Boolean? = null,
    @SerialName("combat_xp")
    val combatXp: Int? = null,
    @SerialName("recent_mob_kills")
    val recentMobKills: List<RecentMobKill>? = null,
    @SerialName("last_killed_mob_island")
    val lastKilledMobIsland: String? = null,
    @SerialName("spawn_timestamp")
    val spawnTimestamp: Long? = null,
)

@Serializable
data class RecentMobKill(
    val xp: Double? = null,
    val timestamp: Long? = null,
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
    val selectedColors: Map<String, String>? = null,
    val talked: Boolean? = null,
    // TODO enum??? its just numbers
    @SerialName("hacked_terminals")
    val hackedTerminals: List<String>? = null,
    @SerialName("quest_complete")
    val questComplete: Boolean? = null,
)

@Serializable
data class Mirrorverse(
    // TODO enum
    @SerialName("visited_rooms")
    val visitedRooms: List<String>? = null,
    @SerialName("upside_down_hard")
    val upsideDownHard: Boolean? = null,
    // TODO item enum
    @SerialName("claimed_chest_items")
    val claimedChestItems: List<String>? = null,
    @SerialName("claimed_reward")
    val claimedReward: Boolean? = null,
)

@Serializable
data class KatHouse(
    @SerialName("bin_collected_silverfish")
    val binCollectedSilverfish: Int? = null,
    @SerialName("bin_collected_spider")
    val binCollectedSpider: Int? = null,
    @SerialName("bin_collected_mosquito")
    val binCollectedMosquito: Int? = null,
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
    val currentGlyph: Int? = null,
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
    val talkedThreeBrothers: List<String>? = null,
    @SerialName("bughunter_step")
    val bughunterStep: Int? = null,
)

@Serializable
data class Castle(
    @SerialName("unlocked_pathway_skip")
    val unlockedPathwaySkip: Boolean? = null,
    @SerialName("fairy_step")
    val fairyStep: Int? = null,
    @SerialName("grubber_stacks")
    val grubberStacks: Int? = null,
)

@Serializable
data class Access(
    @SerialName("last_free")
    val lastFree: Long? = null,
    @SerialName("consumed_prism")
    val consumedPrism: Boolean? = null,
    @SerialName("charge_track_timestamp")
    val chargeTrackTimestamp: Long? = null,
)

@Serializable
data class Dreadfarm(
    @SerialName("shania_stage")
    val shaniaStage: Int? = null,
    @SerialName("caducous_feeder_uses")
    val caducousFeederUses: List<Long>? = null,
)

@Serializable
data class Inventory(
    @SerialName("inv_contents")
    val invContents: InventoryData? = null,
    @SerialName("inv_armor")
    val invArmor: InventoryData? = null,
    @SerialName("ender_chest_contents")
    val enderChestContents: InventoryData? = null,
    @SerialName("ender_chest_page_icons")
    val enderChestPageIcons: List<InventoryData?>? = null,
    @SerialName("equipment_contents")
    val equipmentContents: InventoryData? = null,
)

@Serializable
data class InventoryData(
    val type: Int? = null,
    val data: String? = null,
)
