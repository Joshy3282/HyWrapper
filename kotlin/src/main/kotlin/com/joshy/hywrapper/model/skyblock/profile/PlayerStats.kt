package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonElement

@Serializable
data class PlayerStats(
    @SerialName("candy_collected")
    val candyCollected: CandyCollected? = null,
    val deaths: Map<String, Int>? = null, // TODO enum
    val kills: Map<String, Int>? = null, // TODO enum
    val auctions: Auctions? = null,
    @SerialName("items_fished")
    val itemsFished: ItemsFished? = null,
    val races: Races? = null,
    @SerialName("end_island")
    val endIsland: EndIsland? = null,
    @SerialName("highest_critical_damage")
    val highestCriticalDamage: Double? = null,
    val gifts: Gifts? = null,
    val pets: Pets? = null,
    val mythos: Mythos? = null,
    @SerialName("shredder_rod")
    val shredderRod: ShredderRod? = null,
    @SerialName("highest_damage")
    val highestDamage: Double? = null,
    @SerialName("sea_creature_kills")
    val seaCreaturesKills: Double? = null,
    @SerialName("glowing_mushrooms_broken")
    val glowingMushroomsBroken: Double? = null,
    val rift: RiftData? = null,
    val spooky: Spooky? = null,
    @SerialName("shard_combat_hunts")
    val shardCombatHunts: Double? = null,
    @SerialName("unique_shards")
    val uniqueShards: Double? = null,
    @SerialName("shard_fishing_hunts")
    val shardFishingHunts: Double? = null,
    @SerialName("shard_forest_hunts")
    val shardForestHunts: Double? = null,
    @SerialName("shard_trap_hunts")
    val shardTrapHunts: Double? = null,
    @SerialName("shard_salt_hunts")
    val shardSaltHunts: Double? = null,
)

@Serializable
data class CandyCollected(
    val data: Map<String, JsonElement>? = null
)

@Serializable
data class Auctions(
    val bids: Double? = null,
    @SerialName("highest_bid")
    val highestBid: Double? = null,
    val won: Double? = null,
    @SerialName("total_bought")
    val totalBought: Map<String, Double>? = null, // TODO enum
    @SerialName("gold_spent")
    val goldSpent: Double? = null,
    val created: Double? = null,
    val fees: Double? = null,
    val completed: Double? = null,
    @SerialName("total_sold")
    val totalSold: Map<String, Double>? = null, // TODO enum
    @SerialName("gold_earned")
    val goldEarned: Double? = null,
    @SerialName("no_bids")
    val noBids: Double? = null,
)

@Serializable
data class ItemsFished(
    val total: Double? = null,
    val normal: Double? = null,
    val treasure: Double? = null,
    @SerialName("large_treasure")
    val largeTreasure: Double? = null,
    @SerialName("trophy_fish")
    val trophyFish: Double? = null,
    val oustanding: Double? = null,
)

@Serializable
data class Races(
    @SerialName("end_race_best_time")
    val endRaceBestTime: Double? = null,
    @SerialName("foraging_race_best_time")
    val foragingRaceBestTime: Double? = null,
    @SerialName("chicken_race_best_time_2")
    val chickenRaceBestTime2: Double? = null,
    @SerialName("dungeon_hub")
    val dungeonHub: DungeonHub? = null,
    @SerialName("rift_race_best_time")
    val riftRaceBestTime: Double? = null,

    )

@Serializable
data class DungeonHub(
    @SerialName("precursor_ruins_anything_no_return_best_time")
    val precursorRuinsAnythingNoReturnBestTime: Double? = null,
    @SerialName("precursor_ruins_no_pearls_no_return_best_time")
    val precursorRuinsNoPearlsNoReturnBestTime: Double? = null,
    @SerialName("precursor_ruins_no_abilities_no_return_best_time")
    val precursorRuinsNoAbilitiesNoReturnBestTime: Double? = null,
    @SerialName("precursor_ruins_nothing_no_return_best_time")
    val precursorRuinsNothingNoReturnBestTime: Double? = null,
)

@Serializable
data class EndIsland(
    @SerialName("dragon_fight")
    val dragonFight: DragonFight? = null,
    @SerialName("summoning_eyes_collected")
    val summoningEyesCollected: Double? = null,
    @SerialName("special_zealot_loot_collected")
    val specialZealotLootCollected: Double? = null,
)

@Serializable
data class DragonFight(
    @SerialName("ender_crystals_destroyed")
    val enderCrystalsDestroyed: Double? = null,
    @SerialName("amount_summoned")
    val amountSummoned: Map<String, Double>? = null, // TODO enum
    @SerialName("summoning_eyes_contributed")
    val summoningEyesContributed: Map<String, Double>? = null, // TODO enum
    @SerialName("most_damage")
    val mostDamage: Map<String, Double>? = null, // TODO enum
    @SerialName("highest_rank")
    val highestRank: Map<String, Double>? = null, // TODO enum
    @SerialName("fastest_kill")
    val fastestKill: Map<String, Double>? = null, // TODO enum
)

@Serializable
data class Gifts(
    @SerialName("total_given")
    val totalGiven: Double? = null,
    @SerialName("total_received")
    val totalReceived: Double? = null,
)

@Serializable
data class Pets(
    val milestone: PetsMilestone? = null,
    @SerialName("total_exp_gained")
    val totalExpGained: Double? = null,
)

@Serializable
data class PetsMilestone(
    @SerialName("ores_mined")
    val oresMined: Double? = null,
    @SerialName("sea_creatures_killed")
    val seaCreaturesKilled: Double? = null,
)

@Serializable
data class Mythos(
    val kills: Double? = null,
    @SerialName("burrows_dug_next")
    val burrowsDugNext: Map<String, Double>? = null,
    @SerialName("burrows_dug_combat")
    val burrowsDugCombat: Map<String, Double>? = null,
    @SerialName("burrows_dug_treasure")
    val burrowsDugTreasure: Map<String, Double>? = null,
    @SerialName("burrows_chains_complete")
    val burrowsChainsComplete: Map<String, Double>? = null,
)

@Serializable
data class ShredderRod(
    val bait: Double? = null,
    val fished: Double? = null,
)

@Serializable
data class RiftData(
    val visits: Double? = null,
    @SerialName("pass_consumed")
    val passConsumed: Double? = null,
    @SerialName("lifetime_motes_earned")
    val lifetimeMotesEarned: Double? = null,
    @SerialName("motes_orb_pickup")
    val motesOrbPickup: Double? = null,
    @SerialName("woods_larva_killed")
    val woodsLarvaKilled: Double? = null,
    @SerialName("woods_odonata_bottled")
    val woodsOdonataBottled: Double? = null,
    @SerialName("lagoon_mushroom_popped_out")
    val lagoonMushroomPoppedOut: Double? = null,
    @SerialName("lagoon_lil_pads_sold")
    val lagoonLilPadsSold: Double? = null,
    @SerialName("lagoon_rocks_game_complete")
    val lagoonRocksGameComplete: Double? = null,
    @SerialName("lagoon_leech_supreme_killed")
    val lagoonLeechSupremeKilled: Double? = null,
    @SerialName("plaza_pillar_deaths")
    val plazaPillarDeaths: Double? = null,
    @SerialName("west_cake_part_eaten")
    val westCakePartEaten: Double? = null,
    @SerialName("west_hot_dogs_given")
    val westHotDogsGiven: Double? = null,
    @SerialName("west_vermin_vacuumed")
    val westVerminVacuumed: Map<String, Double> = emptyMap(),
    @SerialName("dreadfarm_wilted_harvested")
    val dreadfarmWiltedHarvested: Double? = null,
    @SerialName("dreadfarm_caducous_harvested")
    val dreadfarmCaducousHarvested: Double? = null,
    @SerialName("dreadfarm_agaricus_harvested")
    val dreadfarmAgaricusHarvested: Double? = null,
    @SerialName("popped_balloons")
    val poppedBalloons: Double? = null,
    @SerialName("dreadfarm_chicken_killed")
    val dreadfarmChickenKilled: Double? = null,
    @SerialName("dreadfarm_bean_bulb_collected")
    val dreadfarmBeanBulbCollected: Double? = null,
    @SerialName("plaza_red_light_deaths")
    val plazaRedLightDeaths: Double? = null,
    @SerialName("plaza_horsezooka_shot")
    val plazaHorsezookaShot: Double? = null,
    @SerialName("dreadfarm_riftwarts_harvested")
    val dreadfarmRiftwartsHarvested: Double? = null,
    @SerialName("living_metal_spawnegg_used")
    val livingMetalSpawneggUsed: Double? = null,
    @SerialName("living_metal_piece_maxed")
    val livingMetalPieceMaxed: Double? = null,
    @SerialName("living_cave_snake_collected")
    val livingCaveSnakeCollected: Double? = null,
    @SerialName("colosseum_globowls_at_tentacle")
    val colosseumGlobowlsAtTentacle: Double? = null,
    @SerialName("colosseum_blaster_shots")
    val colosseumBlasterShots: Double? = null,
    @SerialName("colosseum_bacte_defeated")
    val colosseumBacteDefeated: Double? = null,
    @SerialName("castle_sent_to_prison")
    val castleSentToPrison: Double? = null,
    @SerialName("castle_effigy_broken")
    val castleEffigyBroken: Double? = null,
    @SerialName("shen_item_bought")
    val shenItemBought: Map<String, Double> = emptyMap()
)

@Serializable
data class Spooky(
    @SerialName("bats_spawned")
    val batsSpawned: Map<String, Double>? = null,
)