package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class CrimsonIslePlayerData(
    val quests: Quests? = null,
    @SerialName("kuudra_completed_tiers")
    val kuudraCompletedTiers: Map<String, Int>? = null, // TODO enum
    val dojo: Map<String, Int>? = null, // TODO enum
    val abiphone: Abiphone? = null,
    val matriarch: Matriarch? = null,
    @SerialName("barbarians_reputation")
    val barbariansReputation: Double? = null,
    @SerialName("mages_reputation")
    val magesReputation: Double? = null,
    @SerialName("selected_faction")
    val selectedFaction: String? = null, // TODO enum
    @SerialName("last_minibosses_killed")
    val lastMinibossesKilled: List<String>? = null, // TODO enum
    @SerialName("kuudra_party_finder")
    val kuudraPartyFinder: KuudraPartyFinder? = null,
    @SerialName("barbarians_reputation_highest")
    val barbariansReputationHighest: Int? = null,
)

@Serializable
data class Quests(
    @SerialName("quest_data")
    val questData: QuestData? = null,
    // TODO miniboss_daily
    // TODO kuudra_boss_daily
    @SerialName("quest_rewards")
    val questRewards: QuestRewards? = null,
    @SerialName("alchemist_quest")
    val alchemistQuest: AlchemistQuest? = null,
    // TODO rulenor
    @SerialName("chicken_quest")
    val chickenQuest: ChickenQuest? = null,
    @SerialName("pomtair_quest")
    val pomtairQuest: PomtairQuest? = null,
    @SerialName("suus_quest")
    val suusQuest: SuusQuest? = null,
    @SerialName("pablo_quest")
    val pabloQuest: PabloQuest? = null,
    @SerialName("duel_training_quest")
    val duelTrainingQuest: DuelTrainingQuest? = null,
    @SerialName("sirih_quest")
    val sirihQuest: SirihQuest? = null,
    // TODO edelis_quest
    // TODO mollim_quest
    // TODO aranya_quest
    @SerialName("last_reset")
    val lastReset: Int? = null,
    @SerialName("paid_bruuh")
    val paidBruuh: Boolean? = null,
    @SerialName("miniboss_data")
    val minibossData: Map<String, Boolean>? = null, // TODO enum
    @SerialName("found_kuudra_book")
    val foundKuudraBook: Boolean? = null,
    @SerialName("kuudra_loremaster")
    val kuudraLoremaster: Boolean? = null,
    @SerialName("found_kuudra_chestplate")
    val foundKuudraChestplate: Boolean? = null,
    @SerialName("found_kuudra_boots")
    val foundKuudraBoots: Boolean? = null,
    @SerialName("last_believer_blessing")
    val lastBelieverBlessing: Long? = null,
    @SerialName("fished_wet_napkin")
    val fishedWetNapkin: Boolean? = null,
    @SerialName("weird_sailor")
    val weirdSailor: Boolean? = null,
    @SerialName("found_kuudra_helmet")
    val foundKuudraHelmet: Boolean? = null,
    @SerialName("found_kuudra_leggings")
    val foundKuudraLeggings: Boolean? = null,
    @SerialName("last_kuudra_relic")
    val lastKuudraRelic: Long? = null,
    @SerialName("unlocked_cavity_npcs")
    val unlockedCavityNpcs: List<String>? = null, // TODO enum
    @SerialName("cavity_rarity")
    val cavityRarity: String? = null, // TODO enum
)

@Serializable
data class QuestData(
    @SerialName("quest_list")
    val questList: List<String>? = null, // TODO enum
    val quests: List<QuestDataData>? = null, // TODO no way this is right
)

@Serializable
data class QuestDataData(
    // TODO name..
    val status: String? = null,
    val progress: Int? = null,
    @SerialName("completed_at")
    val completedAt: Long? = null,
)

@Serializable
data class QuestRewards(
    @SerialName("WITHER_SOUL")
    val witherSoul: Int? = null,
    @SerialName("BEZOS")
    val bezos: Int? = null,
    @SerialName("FLAMING_HEART")
    val flamingHeart: Int? = null,
    @SerialName("CORRUPTED_FRAGMENT")
    val corruptedFragment: Int? = null,
    @SerialName("LUMINO_FIBER")
    val luminoFiber: Int? = null,
    @SerialName("crimson_isle_dojo_test_of_mob_kb_drating_c")
    val crimsonIsleDojoTestOfMobKbDratingC: String? = null,
    @SerialName("crimson_isle_fetch_tentacle_meat_c")
    val crimsonIsleFetchTentacleMeatC: String? = null,
    @SerialName("crimson_isle_soulfish_b")
    val crimsonIsleSoulfishB: String? = null,
    @SerialName("crimson_isle_kill_ashfang_a")
    val crimsonIsleKillAshfangA: String? = null,
    @SerialName("crimson_isle_rescue_s")
    val crimsonIsleRescueS: String? = null
)

@Serializable
data class AlchemistQuest(
    @SerialName("alchemist_quest_start")
    val alchemistQuestStart: Boolean? = null,
    @SerialName("alchemist_quest_progress")
    val alchemistQuestProgress: Int? = null,
)

@Serializable
data class ChickenQuest(
    @SerialName("chicken_quest_progress")
    val chickenQuestProgress: Int? = null,
    @SerialName("chicken_quest_start")
    val chickenQuestStart: Boolean? = null,
    // TODO chicken_quest_collected
)

@Serializable
data class PomtairQuest(
    @SerialName("talked_to_npc")
    val talkedToNpc: Boolean? = null,
)

@Serializable
data class SuusQuest(
    @SerialName("talked_to_npc")
    val talkedToNpc: Boolean? = null,
    @SerialName("last_toy_drop")
    val lastToyDrop: Long? = null,
    @SerialName("last_completion")
    val lastCompletion: Long? = null,
)

@Serializable
data class PabloQuest(
    @SerialName("pablo_active")
    val pabloActive: Boolean? = null,
    @SerialName("pablo_item")
    val pabloItem: String? = null
)

@Serializable
data class DuelTrainingQuest(
    @SerialName("duel_training_phase_barbarians")
    val duelTrainingPhaseBarbarians: Int? = null,
    @SerialName("duel_training_last_complete_barbarians")
    val duelTrainingLastCompleteBarbarians: Long? = null,
)

@Serializable
data class SirihQuest(
    @SerialName("sulphur_given")
    val sulpurGiven: Int? = null,
    @SerialName("last_give")
    val lastGive: Long? = null,
)

@Serializable
data class Abiphone(
    // TODO contact_data
    // TODO games
    @SerialName("operator_chip")
    val operatorChip: OperatorChip? = null,
    @SerialName("active_contacts")
    val activeContacts: List<String>? = null, // TODO enum
    @SerialName("trio_contact_addons")
    val trioContactAddons: Int? = null,
    @SerialName("selected_sort")
    val selectedSort: String? = null,
    @SerialName("has_used_sirius_personal_phone_number_item")
    val hasUsedSiriusPersonalPhoneNumberItem: Boolean? = null,
    @SerialName("last_dye_called_year")
    val lastDyeCalledYear: Int? = null,
)

@Serializable
data class OperatorChip(
    @SerialName("repaired_index")
    val repairedIndex: Int? = null,
)

@Serializable
data class Matriarch(
    @SerialName("pearls_collected")
    val pearlsCollected: Int? = null,
    @SerialName("last_attempt")
    val lastAttempt: Long? = null,
    @SerialName("recent_refreshes")
    val recentRefreshes: List<Long>? = null,
)

@Serializable
data class KuudraPartyFinder(
    @SerialName("search_settings")
    val searchSettings: SearchSettings? = null,
    @SerialName("group_builder")
    val groupBuilder: GroupBuilder? = null
)

@Serializable
data class SearchSettings(
    val tier: String? = null,
)

@Serializable
data class GroupBuilder(
    val tier: String? = null,
    val note: String? = null,
    @SerialName("combat_level_required")
    val combatLevelRequired: Int? = null,
)