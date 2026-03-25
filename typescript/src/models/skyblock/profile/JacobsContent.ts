export interface JacobsContent {
    /** TODO enum */
    medals_inv?: Record<string, number>;
    perks?: JacobsPerks;
    talked?: boolean;
    contents?: Record<string, Content>;
    /** TODO enum */
    unique_brackets?: Record<string, string[]>;
    migration?: boolean;
    /** TODO enum */
    personal_bests?: Record<string, number>;
}

export interface JacobsPerks {
    double_drops?: number;
    farming_level_cap?: number;
    personal_bests?: boolean;
}

export interface Content {
    collected?: number;
    claimed_rewards?: boolean;
    claimed_position?: number;
    claimed_participants?: number;
}
