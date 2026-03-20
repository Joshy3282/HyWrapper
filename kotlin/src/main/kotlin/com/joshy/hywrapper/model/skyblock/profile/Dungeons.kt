package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

// TODO bunch of enums

@Serializable
data class Dungeons(
    @SerialName("dungeon_types")
    val dungeonType: DungeonType? = null,
    @SerialName("player_classes")
    val playerClasses: Map<String, Map<String, Double>>? = null,
    @SerialName("dungeon_journal")
    val dungeonJournal: DungeonJournal? = null,
    @SerialName("dungeons_blah_blah")
    val dungeonsBlahBlah: List<String>? = null, // TODO enum
    @SerialName("selected_dungeon_class")
    val selectedDungeonClass: String? = null,
    @SerialName("daily_runs")
    val dailyRuns: DailyRuns? = null,
    // TODO treasures
    @SerialName("dungeon_hub_race_settings")
    val dungeonHubRaceSettings: DungeonHubRaceSettings? = null,
    @SerialName("last_dungeon_run")
    val lastDungeonRun: String? = null,
    val secrets: Int? = null,
)

@Serializable
data class DungeonType(
    val catacombs: Catacombs? = null,
    @SerialName("master_catacombs")
    val masterCatacombs: MasterCatacombs? = null
)

@Serializable
data class Catacombs(
    @SerialName("times_played")
    val timesPlayed: Map<String, Int>? = null,
    val experience: Double? = null,
    @SerialName("tier_completions")
    val tierCompletions: Map<String, Int>? = null,
    @SerialName("fastest_time")
    val fastestTime: Map<String, Int>? = null,
    @SerialName("best_runs")
    val bestRuns: Map<String, BestRun>? = null,
    @SerialName("best_score")
    val bestScore: Map<String, Int>? = null,
    @SerialName("mobs_killed")
    val mobsKilled: Map<String, Int>? = null,
    @SerialName("most_mobs_killed")
    val mostMobsKilled: Map<String, Int>? = null,
    @SerialName("most_damage_tank")
    val mostDamageTank: Map<String, Double>? = null,
    @SerialName("most_healing")
    val mostHealing: Map<String, Double>? = null,
    @SerialName("watcher_kills")
    val watcherKills: Map<String, Int>? = null,
    @SerialName("highest_tier_completed")
    val highestTierCompleted: Int? = null,
    @SerialName("fastest_time_s")
    val fastestTimeS: Map<String, Double>? = null,
    @SerialName("fastest_time_s_plus")
    val fastestTimeSPlus: Map<String, Double>? = null,
    @SerialName("most_damage_berserk")
    val mostDamageBerserk: Map<String, Double>? = null,
    @SerialName("most_damage_healer")
    val mostDamageHealer: Map<String, Double>? = null,
    @SerialName("most_damage_mage")
    val mostDamageMage: Map<String, Double>? = null,
    @SerialName("milestone_completions")
    val milestoneCompletions: Map<String, Double>? = null,
    @SerialName("most_damage_archer")
    val mostDamageArcher: Map<String, Double>? = null,
)

@Serializable
data class MasterCatacombs(
    @SerialName("times_played")
    val timesPlayed: Map<String, Int>? = null,
    @SerialName("tier_completions")
    val tierCompletions: Map<String, Int>? = null,
    @SerialName("fastest_time")
    val fastestTime: Map<String, Int>? = null,
    @SerialName("best_runs")
    val bestRuns: Map<String, BestRun>? = null,
    @SerialName("best_score")
    val bestScore: Map<String, Int>? = null,
    @SerialName("mobs_killed")
    val mobsKilled: Map<String, Int>? = null,
    @SerialName("most_mobs_killed")
    val mostMobsKilled: Map<String, Int>? = null,
    @SerialName("most_damage_tank")
    val mostDamageTank: Map<String, Double>? = null,
    @SerialName("most_healing")
    val mostHealing: Map<String, Double>? = null,
    @SerialName("watcher_kills")
    val watcherKills: Map<String, Int>? = null,
    @SerialName("highest_tier_completed")
    val highestTierCompleted: Int? = null,
    @SerialName("fastest_time_s")
    val fastestTimeS: Map<String, Double>? = null,
    @SerialName("fastest_time_s_plus")
    val fastestTimeSPlus: Map<String, Double>? = null,
    @SerialName("most_damage_berserk")
    val mostDamageBerserk: Map<String, Double>? = null,
    @SerialName("most_damage_healer")
    val mostDamageHealer: Map<String, Double>? = null,
    @SerialName("most_damage_mage")
    val mostDamageMage: Map<String, Double>? = null,
    @SerialName("milestone_completions")
    val milestoneCompletions: Map<String, Double>? = null,
    @SerialName("most_damage_archer")
    val mostDamageArcher: Map<String, Double>? = null,
)

@Serializable
data class BestRun(
    val timestamp: Long? = null,
    @SerialName("score_exploration")
    val scoreExploration: Int? = null,
    @SerialName("score_speed")
    val scoreSpeed: Int? = null,
    @SerialName("score_skill")
    val scoreSkill: Int? = null,
    @SerialName("score_bonus")
    val scoreBonus: Int? = null,
    @SerialName("dungeon_class")
    val dungeonClass: String? = null,
    val teammates: List<String>? = null,
    @SerialName("elapsed_time")
    val elapsedTime: Long? = null,
    @SerialName("damage_dealt")
    val damageDealt: Double? = null,
    val deaths: Int? = null,
    @SerialName("mobs_killed")
    val mobsKilled: Int? = null,
    @SerialName("secrets_found")
    val secretsFound: Int? = null,
    @SerialName("damage_mitigated")
    val damageMitigated: Double? = null,
    @SerialName("ally_healing")
    val allyHealing: Double? = null
)

@Serializable
data class DungeonJournal(
    @SerialName("unlocked_journals")
    val unlockedJournals: List<String>? = null, // TODO enum
)

@Serializable
data class DailyRuns(
    @SerialName("current_day_stamp")
    val currentDayStamp: Int? = null,
    @SerialName("completed_runs_count")
    val completedRunsCount: Int? = null,
)

@Serializable
data class DungeonHubRaceSettings(
    @SerialName("selected_race")
    val selectedRace: String? = null,
    @SerialName("selected_setting")
    val selectedSetting: String? = null,
    val runback: Boolean? = null,
)