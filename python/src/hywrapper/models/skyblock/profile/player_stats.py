from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field


class PlayerStats(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    candyCollected: Optional[CandyCollected] = Field(default=None, alias="candy_collected")
    deaths: Optional[Dict[str, int]] = None
    kills: Optional[Dict[str, int]] = None
    auctions: Optional[Auctions] = None
    itemsFished: Optional[ItemsFished] = Field(default=None, alias="items_fished")
    races: Optional[Races] = None
    endIsland: Optional[EndIsland] = Field(default=None, alias="end_island")
    highestCriticalDamage: Optional[float] = Field(default=None, alias="highest_critical_damage")
    gifts: Optional[Gifts] = None
    pets: Optional[Pets] = None
    mythos: Optional[Mythos] = None
    shredderRod: Optional[ShredderRod] = Field(default=None, alias="shredder_rod")
    highestDamage: Optional[float] = Field(default=None, alias="highest_damage")
    seaCreaturesKills: Optional[float] = Field(default=None, alias="sea_creature_kills")
    glowingMushroomsBroken: Optional[float] = Field(default=None, alias="glowing_mushrooms_broken")
    rift: Optional[RiftStats] = None
    spooky: Optional[Spooky] = None
    shardCombatHunts: Optional[float] = Field(default=None, alias="shard_combat_hunts")
    uniqueShards: Optional[float] = Field(default=None, alias="unique_shards")
    shardFishingHunts: Optional[float] = Field(default=None, alias="shard_fishing_hunts")
    shardForestHunts: Optional[float] = Field(default=None, alias="shard_forest_hunts")
    shardTrapHunts: Optional[float] = Field(default=None, alias="shard_trap_hunts")
    shardSaltHunts: Optional[float] = Field(default=None, alias="shard_salt_hunts")


class CandyCollected(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    total: Optional[int] = None
    greenCandy: Optional[int] = Field(default=None, alias="green_candy")
    purpleCandy: Optional[int] = Field(default=None, alias="purple_candy")


class Auctions(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bids: Optional[float] = None
    highestBid: Optional[float] = Field(default=None, alias="highest_bid")
    won: Optional[float] = None
    totalBought: Optional[Dict[str, float]] = Field(default=None, alias="total_bought")
    goldSpent: Optional[float] = Field(default=None, alias="gold_spent")
    created: Optional[float] = None
    fees: Optional[float] = None
    completed: Optional[float] = None
    totalSold: Optional[Dict[str, float]] = Field(default=None, alias="total_sold")
    goldEarned: Optional[float] = Field(default=None, alias="gold_earned")
    noBids: Optional[float] = Field(default=None, alias="no_bids")


class ItemsFished(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    total: Optional[float] = None
    normal: Optional[float] = None
    treasure: Optional[float] = None
    largeTreasure: Optional[float] = Field(default=None, alias="large_treasure")
    trophyFish: Optional[float] = Field(default=None, alias="trophy_fish")
    oustanding: Optional[float] = None


class Races(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    endRaceBestTime: Optional[float] = Field(default=None, alias="end_race_best_time")
    foragingRaceBestTime: Optional[float] = Field(default=None, alias="foraging_race_best_time")
    chickenRaceBestTime2: Optional[float] = Field(default=None, alias="chicken_race_best_time_2")
    dungeonHub: Optional[DungeonHub] = Field(default=None, alias="dungeon_hub")
    riftRaceBestTime: Optional[float] = Field(default=None, alias="rift_race_best_time")


class DungeonHub(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    precursorRuinsAnythingNoReturnBestTime: Optional[float] = Field(
        default=None, alias="precursor_ruins_anything_no_return_best_time"
    )
    precursorRuinsNoPearlsNoReturnBestTime: Optional[float] = Field(
        default=None, alias="precursor_ruins_no_pearls_no_return_best_time"
    )
    precursorRuinsNoAbilitiesNoReturnBestTime: Optional[float] = Field(
        default=None, alias="precursor_ruins_no_abilities_no_return_best_time"
    )
    precursorRuinsNothingNoReturnBestTime: Optional[float] = Field(
        default=None, alias="precursor_ruins_nothing_no_return_best_time"
    )


class EndIsland(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    dragonFight: Optional[DragonFight] = Field(default=None, alias="dragon_fight")
    summoningEyesCollected: Optional[float] = Field(default=None, alias="summoning_eyes_collected")
    specialZealotLootCollected: Optional[float] = Field(
        default=None, alias="special_zealot_loot_collected"
    )


class DragonFight(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    enderCrystalsDestroyed: Optional[float] = Field(default=None, alias="ender_crystals_destroyed")
    amountSummoned: Optional[Dict[str, float]] = Field(default=None, alias="amount_summoned")
    summoningEyesContributed: Optional[Dict[str, float]] = Field(
        default=None, alias="summoning_eyes_contributed"
    )
    mostDamage: Optional[Dict[str, float]] = Field(default=None, alias="most_damage")
    highestRank: Optional[Dict[str, float]] = Field(default=None, alias="highest_rank")
    fastestKill: Optional[Dict[str, float]] = Field(default=None, alias="fastest_kill")


class Gifts(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    totalGiven: Optional[float] = Field(default=None, alias="total_given")
    totalReceived: Optional[float] = Field(default=None, alias="total_received")


class Pets(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    milestone: Optional[PetsMilestone] = None
    totalExpGained: Optional[float] = Field(default=None, alias="total_exp_gained")


class PetsMilestone(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    oresMined: Optional[float] = Field(default=None, alias="ores_mined")
    seaCreaturesKilled: Optional[float] = Field(default=None, alias="sea_creatures_killed")


class Mythos(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    kills: Optional[float] = None
    burrowsDugNext: Optional[Dict[str, float]] = Field(default=None, alias="burrows_dug_next")
    burrowsDugCombat: Optional[Dict[str, float]] = Field(default=None, alias="burrows_dug_combat")
    burrowsDugTreasure: Optional[Dict[str, float]] = Field(
        default=None, alias="burrows_dug_treasure"
    )
    burrowsChainsComplete: Optional[Dict[str, float]] = Field(
        default=None, alias="burrows_chains_complete"
    )


class ShredderRod(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bait: Optional[float] = None
    fished: Optional[float] = None


class RiftStats(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    visits: Optional[float] = None
    passConsumed: Optional[float] = Field(default=None, alias="pass_consumed")
    lifetimeMotesEarned: Optional[float] = Field(default=None, alias="lifetime_motes_earned")
    motesOrbPickup: Optional[float] = Field(default=None, alias="motes_orb_pickup")
    woodsLarvaKilled: Optional[float] = Field(default=None, alias="woods_larva_killed")
    woodsOdonataBottled: Optional[float] = Field(default=None, alias="woods_odonata_bottled")
    lagoonMushroomPoppedOut: Optional[float] = Field(
        default=None, alias="lagoon_mushroom_popped_out"
    )
    lagoonLilPadsSold: Optional[float] = Field(default=None, alias="lagoon_lil_pads_sold")
    lagoonRocksGameComplete: Optional[float] = Field(
        default=None, alias="lagoon_rocks_game_complete"
    )
    lagoonLeechSupremeKilled: Optional[float] = Field(
        default=None, alias="lagoon_leech_supreme_killed"
    )
    plazaPillarDeaths: Optional[float] = Field(default=None, alias="plaza_pillar_deaths")
    westCakePartEaten: Optional[float] = Field(default=None, alias="west_cake_part_eaten")
    westHotDogsGiven: Optional[float] = Field(default=None, alias="west_hot_dogs_given")
    westVerminVacuumed: Optional[Dict[str, float]] = Field(
        default_factory=dict, alias="west_vermin_vacuumed"
    )
    dreadfarmWiltedHarvested: Optional[float] = Field(
        default=None, alias="dreadfarm_wilted_harvested"
    )
    dreadfarmCaducousHarvested: Optional[float] = Field(
        default=None, alias="dreadfarm_caducous_harvested"
    )
    dreadfarmAgaricusHarvested: Optional[float] = Field(
        default=None, alias="dreadfarm_agaricus_harvested"
    )
    poppedBalloons: Optional[float] = Field(default=None, alias="popped_balloons")
    dreadfarmChickenKilled: Optional[float] = Field(default=None, alias="dreadfarm_chicken_killed")
    dreadfarmBeanBulbCollected: Optional[float] = Field(
        default=None, alias="dreadfarm_bean_bulb_collected"
    )
    plazaRedLightDeaths: Optional[float] = Field(default=None, alias="plaza_red_light_deaths")
    plazaHorsezookaShot: Optional[float] = Field(default=None, alias="plaza_horsezooka_shot")
    dreadfarmRiftwartsHarvested: Optional[float] = Field(
        default=None, alias="dreadfarm_riftwarts_harvested"
    )
    livingMetalSpawneggUsed: Optional[float] = Field(
        default=None, alias="living_metal_spawnegg_used"
    )
    livingMetalPieceMaxed: Optional[float] = Field(default=None, alias="living_metal_piece_maxed")
    livingCaveSnakeCollected: Optional[float] = Field(
        default=None, alias="living_cave_snake_collected"
    )
    colosseumGlobowlsAtTentacle: Optional[float] = Field(
        default=None, alias="colosseum_globowls_at_tentacle"
    )
    colosseumBlasterShots: Optional[float] = Field(default=None, alias="colosseum_blaster_shots")
    colosseumBacteDefeated: Optional[float] = Field(default=None, alias="colosseum_bacte_defeated")
    castleSentToPrison: Optional[float] = Field(default=None, alias="castle_sent_to_prison")
    castleEffigyBroken: Optional[float] = Field(default=None, alias="castle_effigy_broken")
    shenItemBought: Optional[Dict[str, float]] = Field(
        default_factory=dict, alias="shen_item_bought"
    )


class Spooky(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    batsSpawned: Optional[Dict[str, float]] = Field(default=None, alias="bats_spawned")
