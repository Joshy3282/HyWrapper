export interface PlayerStats {
    candy_collected?: CandyCollected;
    /** TODO enum */
    deaths?: Record<string, number>;
    /** TODO enum */
    kills?: Record<string, number>;
    auctions?: Auctions;
    items_fished?: ItemsFished;
    races?: Races;
    end_island?: EndIsland;
    highest_critical_damage?: number;
    gifts?: Gifts;
    pets?: Pets;
    mythos?: Mythos;
    shredder_rod?: ShredderRod;
    highest_damage?: number;
    sea_creature_kills?: number;
    glowing_mushrooms_broken?: number;
    rift?: RiftData;
    spooky?: Spooky;
    shard_combat_hunts?: number;
    unique_shards?: number;
    shard_fishing_hunts?: number;
    shard_forest_hunts?: number;
    shard_trap_hunts?: number;
    shard_salt_hunts?: number;
}

export interface CandyCollected {
    data?: Record<string, any>;
}

export interface Auctions {
    bids?: number;
    highest_bid?: number;
    won?: number;
    /** TODO enum */
    total_bought?: Record<string, number>;
    gold_spent?: number;
    created?: number;
    fees?: number;
    completed?: number;
    /** TODO enum */
    total_sold?: Record<string, number>;
    gold_earned?: number;
    no_bids?: number;
}

export interface ItemsFished {
    total?: number;
    normal?: number;
    treasure?: number;
    large_treasure?: number;
    trophy_fish?: number;
    oustanding?: number;
}

export interface Races {
    end_race_best_time?: number;
    foraging_race_best_time?: number;
    chicken_race_best_time_2?: number;
    dungeon_hub?: DungeonHub;
    rift_race_best_time?: number;
}

export interface DungeonHub {
    precursor_ruins_anything_no_return_best_time?: number;
    precursor_ruins_no_pearls_no_return_best_time?: number;
    precursor_ruins_no_abilities_no_return_best_time?: number;
    precursor_ruins_nothing_no_return_best_time?: number;
}

export interface EndIsland {
    dragon_fight?: DragonFight;
    summoning_eyes_collected?: number;
    special_zealot_loot_collected?: number;
}

export interface DragonFight {
    ender_crystals_destroyed?: number;
    /** TODO enum */
    amount_summoned?: Record<string, number>;
    /** TODO enum */
    summoning_eyes_contributed?: Record<string, number>;
    /** TODO enum */
    most_damage?: Record<string, number>;
    /** TODO enum */
    highest_rank?: Record<string, number>;
    /** TODO enum */
    fastest_kill?: Record<string, number>;
}

export interface Gifts {
    total_given?: number;
    total_received?: number;
}

export interface Pets {
    milestone?: PetsMilestone;
    total_exp_gained?: number;
}

export interface PetsMilestone {
    ores_mined?: number;
    sea_creatures_killed?: number;
}

export interface Mythos {
    kills?: number;
    burrows_dug_next?: Record<string, number>;
    burrows_dug_combat?: Record<string, number>;
    burrows_dug_treasure?: Record<string, number>;
    burrows_chains_complete?: Record<string, number>;
}

export interface ShredderRod {
    bait?: number;
    fished?: number;
}

export interface RiftData {
    visits?: number;
    pass_consumed?: number;
    lifetime_motes_earned?: number;
    motes_orb_pickup?: number;
    woods_larva_killed?: number;
    woods_odonata_bottled?: number;
    lagoon_mushroom_popped_out?: number;
    lagoon_lil_pads_sold?: number;
    lagoon_rocks_game_complete?: number;
    lagoon_leech_supreme_killed?: number;
    plaza_pillar_deaths?: number;
    west_cake_part_eaten?: number;
    west_hot_dogs_given?: number;
    west_vermin_vacuumed?: Record<string, number>;
    dreadfarm_wilted_harvested?: number;
    dreadfarm_agaricus_harvested?: number;
    popped_balloons?: number;
    dreadfarm_chicken_killed?: number;
    dreadfarm_bean_bulb_collected?: number;
    plaza_red_light_deaths?: number;
    plaza_horsezooka_shot?: number;
    dreadfarm_riftwarts_harvested?: number;
    living_metal_spawnegg_used?: number;
    living_metal_piece_maxed?: number;
    living_cave_snake_collected?: number;
    colosseum_globowls_at_tentacle?: number;
    colosseum_blaster_shots?: number;
    colosseum_bacte_defeated?: number;
    castle_sent_to_prison?: number;
    castle_effigy_broken?: number;
    shen_item_bought?: Record<string, number>;
}

export interface Spooky {
    bats_spawned?: Record<string, number>;
}
