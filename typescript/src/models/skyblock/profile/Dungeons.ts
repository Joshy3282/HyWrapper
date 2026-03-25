export interface Dungeons {
    dungeon_types?: DungeonType;
    player_classes?: Record<string, Record<string, number>>;
    dungeon_journal?: DungeonJournal;
    /** TODO enum */
    dungeons_blah_blah?: string[];
    selected_dungeon_class?: string;
    daily_runs?: DailyRuns;
    treasures?: Treasures;
    dungeon_hub_race_settings?: DungeonHubRaceSettings;
    last_dungeon_run?: string;
    secrets?: number;
}

export interface DungeonType {
    catacombs?: Catacombs;
    master_catacombs?: MasterCatacombs;
}

export interface Catacombs {
    times_played?: Record<string, number>;
    experience?: number;
    tier_completions?: Record<string, number>;
    fastest_time?: Record<string, number>;
    best_runs?: Record<string, BestRun>;
    best_score?: Record<string, number>;
    mobs_killed?: Record<string, number>;
    most_mobs_killed?: Record<string, number>;
    most_damage_tank?: Record<string, number>;
    most_healing?: Record<string, number>;
    watcher_kills?: Record<string, number>;
    highest_tier_completed?: number;
    fastest_time_s?: Record<string, number>;
    fastest_time_s_plus?: Record<string, number>;
    most_damage_berserk?: Record<string, number>;
    most_damage_healer?: Record<string, number>;
    most_damage_mage?: Record<string, number>;
    milestone_completions?: Record<string, number>;
    most_damage_archer?: Record<string, number>;
}

export interface MasterCatacombs {
    times_played?: Record<string, number>;
    tier_completions?: Record<string, number>;
    fastest_time?: Record<string, number>;
    best_runs?: Record<string, BestRun>;
    best_score?: Record<string, number>;
    mobs_killed?: Record<string, number>;
    most_mobs_killed?: Record<string, number>;
    most_damage_tank?: Record<string, number>;
    most_healing?: Record<string, number>;
    watcher_kills?: Record<string, number>;
    highest_tier_completed?: number;
    fastest_time_s?: Record<string, number>;
    fastest_time_s_plus?: Record<string, number>;
    most_damage_berserk?: Record<string, number>;
    most_damage_healer?: Record<string, number>;
    most_damage_mage?: Record<string, number>;
    milestone_completions?: Record<string, number>;
    most_damage_archer?: Record<string, number>;
}

export interface BestRun {
    timestamp?: number;
    score_exploration?: number;
    score_speed?: number;
    score_skill?: number;
    score_bonus?: number;
    dungeon_class?: string;
    teammates?: string[];
    elapsed_time?: number;
    damage_dealt?: number;
    deaths?: number;
    mobs_killed?: number;
    secrets_found?: number;
    damage_mitigated?: number;
    ally_healing?: number;
}

export interface DungeonJournal {
    /** TODO enum */
    unlocked_journals?: string[];
}

export interface DailyRuns {
    current_day_stamp?: number;
    completed_runs_count?: number;
}

export interface Treasures {
    runs?: any[];
    chests?: any[];
}

export interface DungeonHubRaceSettings {
    selected_race?: string;
    selected_setting?: string;
    runback?: boolean;
}
