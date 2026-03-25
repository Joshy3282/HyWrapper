import { HypixelResponse } from "../../types";
import {
    Bestiary,
    CrimsonIslePlayerData,
    Dungeons,
    Event,
    Experimentation,
    Foraging,
    PlayerInventory,
    JacobsContent,
    MiningCore,
    PetsData,
    PlayerData,
    PlayerStats,
    Rift,
    Slayer,
    InventoryObject,
} from "./profile";

export interface ProfileResponse extends HypixelResponse {
    profile?: Profile;
}

export interface Profile {
    profile_id?: string;
    community_upgrades?: CommunityUpgrades;
    members?: Record<string, MemberData>;
    banking?: Banking;
}

export interface MemberData {
    rift?: Rift;
    player_data?: PlayerData;
    glacite_player_data?: GlacitePlayerData;
    profile?: ProfileData;
    event?: Event;
    garden_player_data?: GardenPlayerData;
    skill_tree?: SkillTree;
    pets_data?: PetsData;
    accessory_bag_storage?: AccessoryBagStorage;
    leveling?: ProfileLeveling;
    item_data?: ItemData;
    jacobs_contest?: JacobsContent;
    currencies?: Currencies;
    foraging?: Foraging;
    dungeons?: Dungeons;
    player_id?: string;
    nether_island_player_data?: CrimsonIslePlayerData;
    experimentation?: Experimentation;
    foraging_core?: ForagingCore;
    shards?: Shards;
    mining_core?: MiningCore;
    bestiary?: Bestiary;
    quests?: Quests;
    player_stats?: PlayerStats;
    inventory?: PlayerInventory;
    winter_player_data?: WinterPlayerData;
    forge?: Forge;
    fairy_soul?: FairySoul;
    temples?: Temples;
    shared_inventory?: SharedInventory;
    attributes?: Attributes;
    slayer?: Slayer;
    trophy_fish?: Record<string, any>;
    objectives?: Objective[];
    collection?: Record<string, number>;
}

export interface SkillTree {
    nodes?: Record<string, Record<string, any>>;
}

export interface Forge {
    forge_processes?: Record<string, Record<string, any>>;
}

export interface GlacitePlayerData {
    /** TODO enum */
    fossils_donated?: string[];
    fossil_dust?: number;
    /** TODO enum */
    corpses_looted?: Record<string, number>;
    mineshafts_entered?: number;
}

export interface ProfileData {
    bank_account?: number;
    first_join?: number;
    personal_bank_upgrade?: number;
    cookie_buff_active?: boolean;
}

export interface GardenPlayerData {
    copper?: number;
    larva_consumed?: number;
    /** TODO enum */
    analyzed_greenhouse_crops?: string[];
    /** TODO enum */
    discovered_greenhouse_crops?: string[];
}

export interface AccessoryBagStorage {
    tuning?: Record<string, TuningSlot>;
    /** TODO ENUM */
    selected_power?: string;
    bag_upgrades_purchased?: number;
    /** TODO enum */
    unlocked_powers?: string[];
    highest_magical_power?: number;
}

export interface TuningSlot {
    health?: number;
    defense?: number;
    walk_speed?: number;
    strength?: number;
    critical_damage?: number;
    critical_chance?: number;
    attack_speed?: number;
    intelligence?: number;
}

export interface ProfileLeveling {
    experience?: number;
    /** TODO enum */
    completions?: Record<string, number>;
    /** TODO enum */
    completed_tasks?: string[];
    highest_pet_score?: number;
    mining_fiesta_ores_mined?: number;
    migrated?: boolean;
    migrated_completions_2?: boolean;
    claimed_talisman?: boolean;
    /** TODO enum */
    bop_bonus?: string;
    /** TODO enum */
    emblem_unlocks?: string[];
    category_expanded?: boolean;
    fishing_festival_sharks_killed?: number;
    /** TODO enum */
    task_sort?: string;
    /** TODO enum */
    last_viewed_tasks?: string[];
    /** TODO enum */
    selected_symbol?: string;
}

export interface ItemData {
    soulflow?: number;
    favorite_arrow?: string;
}

export interface Currencies {
    coin_purse?: number;
    motes_purse?: number;
    essence?: Record<string, EssenceInfo>;
}

export interface EssenceInfo {
    current?: number;
}

export interface ForagingCore {
    daily_trees_cut_day?: number;
    daily_trees_cut?: number;
    daily_gifts?: number;
    daily_log_cut_day?: number;
    daily_log_cut?: any[];
    forests_whispers?: number;
    forests_whispers_spent?: number;
    current_daily_effect?: string;
    current_daily_effect_last_changed?: number;
}

export interface Shards {
    traps?: Record<string, any>;
    shard_sort?: string;
    fusion_result_sort?: string;
    owned?: ShardOwned[];
}

export interface ShardOwned {
    type?: string;
    amount_owned?: number;
    captured?: number;
}

export interface Quests {
    trapper_quest?: TrapperQuest;
}

export interface TrapperQuest {
    last_task_time?: number;
    pelt_count?: number;
}

export interface WinterPlayerData {
    refined_jyrre_uses?: number;
}

export interface FairySoul {
    fairy_exchanges?: number;
    total_collected?: number;
    unspent_souls?: number;
}

export interface Temples {
    unlocked_temples?: string[];
}

export interface SharedInventory {
    carnival_mask_inventory_contents?: InventoryObject;
    candy_inventory_contents?: InventoryObject;
}

export interface Attributes {
    /** TODO enum */
    stacks?: Record<string, number>;
}

export interface Objective {
    status?: string;
    progress?: number;
    completed_at?: number;
    data?: Record<string, string>;
}

export interface CommunityUpgrades {
    currently_upgrading?: string;
    upgrade_states?: UpgradeState[];
}

export interface UpgradeState {
    upgrade?: string;
    tier?: number;
    started_ms?: number;
    started_by?: string;
    claimed_by?: string;
}

export interface Banking {
    balance?: number;
    transactions?: Transaction[];
}

export interface Transaction {
    amount?: number;
    timestamp?: number;
    action?: string;
    initiator_name?: string;
}
