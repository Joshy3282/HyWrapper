export interface Slayer {
    slayer_quest?: OngoingSlayerQuest;
    /** TODO enum */
    slayer_bosses?: Record<string, SlayerData>;
}

export interface OngoingSlayerQuest {
    /** TODO enum */
    type?: string;
    /** TODO enum */
    tier?: number;
    start_timestamp?: number;
    completion_state?: number;
    used_armor?: boolean;
    solo?: boolean;
}

export interface SlayerData {
    claimed_levels?: Record<string, boolean>;
    xp?: number;
    boss_kills_tier_0?: number;
    boss_kills_tier_1?: number;
    boss_kills_tier_2?: number;
    boss_kills_tier_3?: number;
    boss_kills_tier_4?: number;
    boss_attempts_tier_0?: number;
    boss_attempts_tier_1?: number;
    boss_attempts_tier_2?: number;
    boss_attempts_tier_3?: number;
    boss_attempts_tier_4?: number;
}
