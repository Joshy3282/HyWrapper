export interface PlayerData {
    /** TODO enum */
    visited_zones?: string[];
    last_death?: number;
    /** TODO enum */
    perks?: Record<string, number>;
    /** TODO enum */
    garden_chips?: Record<string, number>;
    active_effects?: ActiveEffect[];
    paused_effects?: any[];
    reaper_peppers_eaten?: number;
    temp_stat_buffs?: any[];
    death_count?: number;
    disabled_potion_effects?: any[];
    /** TODO enum */
    achievement_spawned_island_types?: string[];
    /** TODO enum */
    visited_modes?: string[];
    /** TODO enum? meh */
    unlocked_coll_tiers?: string[];
    /** TODO enum */
    crafted_generators?: string[];
    fishing_treasure_caught?: number;
    /** TODO enum */
    experience?: Record<string, number>;
}

export interface ActiveEffect {
    effect?: string;
    level?: number;
    modifiers?: any[];
    ticks_remaining?: number;
    infinite?: boolean;
    flags?: number;
}
