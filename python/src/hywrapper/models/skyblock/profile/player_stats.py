from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict, Field


class PlayerStats(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    candy_collected: Optional[Dict[str, Any]] = Field(default=None, alias="candy_collected")
    deaths: Optional[Dict[str, int]] = None
    kills: Optional[Dict[str, int]] = None
    auctions: Optional[Auctions] = None
    items_fished: Optional[ItemsFished] = Field(default=None, alias="items_fished")
    races: Optional[Races] = None
    end_island: Optional[EndIsland] = Field(default=None, alias="end_island")
    highest_critical_damage: Optional[float] = Field(default=None, alias="highest_critical_damage")
    gifts: Optional[Gifts] = None
    pets: Optional[Pets] = None
    mythos: Optional[Mythos] = None
    shredder_rod: Optional[ShredderRod] = Field(default=None, alias="shredder_rod")
    highest_damage: Optional[float] = Field(default=None, alias="highest_damage")
    sea_creature_kills: Optional[float] = Field(default=None, alias="sea_creature_kills")
    glowing_mushrooms_broken: Optional[float] = Field(
        default=None, alias="glowing_mushrooms_broken"
    )
    rift: Optional[RiftStats] = None
    spooky: Optional[Spooky] = None
    shard_combat_hunts: Optional[float] = Field(default=None, alias="shard_combat_hunts")
    unique_shards: Optional[float] = Field(default=None, alias="unique_shards")
    shard_fishing_hunts: Optional[float] = Field(default=None, alias="shard_fishing_hunts")
    shard_forest_hunts: Optional[float] = Field(default=None, alias="shard_forest_hunts")
    shard_trap_hunts: Optional[float] = Field(default=None, alias="shard_trap_hunts")
    shard_salt_hunts: Optional[float] = Field(default=None, alias="shard_salt_hunts")


class Auctions(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bids: Optional[float] = None
    highest_bid: Optional[float] = Field(default=None, alias="highest_bid")
    won: Optional[float] = None
    total_bought: Optional[Dict[str, float]] = Field(default=None, alias="total_bought")
    gold_spent: Optional[float] = Field(default=None, alias="gold_spent")
    created: Optional[float] = None
    fees: Optional[float] = None
    completed: Optional[float] = None
    total_sold: Optional[Dict[str, float]] = Field(default=None, alias="total_sold")
    gold_earned: Optional[float] = Field(default=None, alias="gold_earned")
    no_bids: Optional[float] = Field(default=None, alias="no_bids")


class ItemsFished(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    total: Optional[float] = None
    normal: Optional[float] = None
    treasure: Optional[float] = None
    large_treasure: Optional[float] = Field(default=None, alias="large_treasure")
    trophy_fish: Optional[float] = Field(default=None, alias="trophy_fish")
    oustanding: Optional[float] = None


class Races(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    end_race_best_time: Optional[float] = Field(default=None, alias="end_race_best_time")
    foraging_race_best_time: Optional[float] = Field(default=None, alias="foraging_race_best_time")
    chicken_race_best_time_2: Optional[float] = Field(
        default=None, alias="chicken_race_best_time_2"
    )
    dungeon_hub: Optional[DungeonHub] = Field(default=None, alias="dungeon_hub")
    rift_race_best_time: Optional[float] = Field(default=None, alias="rift_race_best_time")


class DungeonHub(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    precursor_ruins_anything_no_return_best_time: Optional[float] = Field(
        default=None, alias="precursor_ruins_anything_no_return_best_time"
    )
    precursor_ruins_no_pearls_no_return_best_time: Optional[float] = Field(
        default=None, alias="precursor_ruins_no_pearls_no_return_best_time"
    )
    precursor_ruins_no_abilities_no_return_best_time: Optional[float] = Field(
        default=None, alias="precursor_ruins_no_abilities_no_return_best_time"
    )
    precursor_ruins_nothing_no_return_best_time: Optional[float] = Field(
        default=None, alias="precursor_ruins_nothing_no_return_best_time"
    )


class EndIsland(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    dragon_fight: Optional[DragonFight] = Field(default=None, alias="dragon_fight")
    summoning_eyes_collected: Optional[float] = Field(
        default=None, alias="summoning_eyes_collected"
    )
    special_zealot_loot_collected: Optional[float] = Field(
        default=None, alias="special_zealot_loot_collected"
    )


class DragonFight(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    ender_crystals_destroyed: Optional[float] = Field(
        default=None, alias="ender_crystals_destroyed"
    )
    amount_summoned: Optional[Dict[str, float]] = Field(default=None, alias="amount_summoned")
    summoning_eyes_contributed: Optional[Dict[str, float]] = Field(
        default=None, alias="summoning_eyes_contributed"
    )
    most_damage: Optional[Dict[str, float]] = Field(default=None, alias="most_damage")
    highest_rank: Optional[Dict[str, float]] = Field(default=None, alias="highest_rank")
    fastest_kill: Optional[Dict[str, float]] = Field(default=None, alias="fastest_kill")


class Gifts(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    total_given: Optional[float] = Field(default=None, alias="total_given")
    total_received: Optional[float] = Field(default=None, alias="total_received")


class Pets(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    milestone: Optional[PetsMilestone] = None
    total_exp_gained: Optional[float] = Field(default=None, alias="total_exp_gained")


class PetsMilestone(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    ores_mined: Optional[float] = Field(default=None, alias="ores_mined")
    sea_creatures_killed: Optional[float] = Field(default=None, alias="sea_creatures_killed")


class Mythos(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    kills: Optional[float] = None
    burrows_dug_next: Optional[Dict[str, float]] = Field(default=None, alias="burrows_dug_next")
    burrows_dug_combat: Optional[Dict[str, float]] = Field(default=None, alias="burrows_dug_combat")
    burrows_dug_treasure: Optional[Dict[str, float]] = Field(
        default=None, alias="burrows_dug_treasure"
    )
    burrows_chains_complete: Optional[Dict[str, float]] = Field(
        default=None, alias="burrows_chains_complete"
    )


class ShredderRod(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bait: Optional[float] = None
    fished: Optional[float] = None


class RiftStats(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    visits: Optional[float] = None
    pass_consumed: Optional[float] = Field(default=None, alias="pass_consumed")
    lifetime_motes_earned: Optional[float] = Field(default=None, alias="lifetime_motes_earned")
    motes_orb_pickup: Optional[float] = Field(default=None, alias="motes_orb_pickup")
    woods_larva_killed: Optional[float] = Field(default=None, alias="woods_larva_killed")
    woods_odonata_bottled: Optional[float] = Field(default=None, alias="woods_odonata_bottled")
    lagoon_mushroom_popped_out: Optional[float] = Field(
        default=None, alias="lagoon_mushroom_popped_out"
    )
    lagoon_lil_pads_sold: Optional[float] = Field(default=None, alias="lagoon_lil_pads_sold")
    lagoon_rocks_game_complete: Optional[float] = Field(
        default=None, alias="lagoon_rocks_game_complete"
    )
    lagoon_leech_supreme_killed: Optional[float] = Field(
        default=None, alias="lagoon_leech_supreme_killed"
    )
    plaza_pillar_deaths: Optional[float] = Field(default=None, alias="plaza_pillar_deaths")
    west_cake_part_eaten: Optional[float] = Field(default=None, alias="west_cake_part_eaten")
    west_hot_dogs_given: Optional[float] = Field(default=None, alias="west_hot_dogs_given")
    west_vermin_vacuumed: Optional[Dict[str, float]] = Field(
        default_factory=dict, alias="west_vermin_vacuumed"
    )
    dreadfarm_wilted_harvested: Optional[float] = Field(
        default=None, alias="dreadfarm_wilted_harvested"
    )
    dreadfarm_caducous_harvested: Optional[float] = Field(
        default=None, alias="dreadfarm_caducous_harvested"
    )
    dreadfarm_agaricus_harvested: Optional[float] = Field(
        default=None, alias="dreadfarm_agaricus_harvested"
    )
    popped_balloons: Optional[float] = Field(default=None, alias="popped_balloons")
    dreadfarm_chicken_killed: Optional[float] = Field(
        default=None, alias="dreadfarm_chicken_killed"
    )
    dreadfarm_bean_bulb_collected: Optional[float] = Field(
        default=None, alias="dreadfarm_bean_bulb_collected"
    )
    plaza_red_light_deaths: Optional[float] = Field(default=None, alias="plaza_red_light_deaths")
    plaza_horsezooka_shot: Optional[float] = Field(default=None, alias="plaza_horsezooka_shot")
    dreadfarm_riftwarts_harvested: Optional[float] = Field(
        default=None, alias="dreadfarm_riftwarts_harvested"
    )
    living_metal_spawnegg_used: Optional[float] = Field(
        default=None, alias="living_metal_spawnegg_used"
    )
    living_metal_piece_maxed: Optional[float] = Field(
        default=None, alias="living_metal_piece_maxed"
    )
    living_cave_snake_collected: Optional[float] = Field(
        default=None, alias="living_cave_snake_collected"
    )
    colosseum_globowls_at_tentacle: Optional[float] = Field(
        default=None, alias="colosseum_globowls_at_tentacle"
    )
    colosseum_blaster_shots: Optional[float] = Field(default=None, alias="colosseum_blaster_shots")
    colosseum_bacte_defeated: Optional[float] = Field(
        default=None, alias="colosseum_bacte_defeated"
    )
    castle_sent_to_prison: Optional[float] = Field(default=None, alias="castle_sent_to_prison")
    castle_effigy_broken: Optional[float] = Field(default=None, alias="castle_effigy_broken")
    shen_item_bought: Optional[Dict[str, float]] = Field(
        default_factory=dict, alias="shen_item_bought"
    )


class Spooky(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bats_spawned: Optional[Dict[str, float]] = Field(default=None, alias="bats_spawned")
