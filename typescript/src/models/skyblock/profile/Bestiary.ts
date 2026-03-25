export interface Bestiary {
    migrated_stats?: boolean;
    migration?: boolean;
    /** TODO enum */
    kills?: Record<string, number>;
    /** TODO enum */
    deaths?: Record<string, number>;
    milestone?: Milestone;
    miscellaneous?: Miscellaneous;
}

export interface Milestone {
    last_claimed_milestone?: number;
}

export interface Miscellaneous {
    max_kills_visible?: boolean;
    milestones_notifications?: boolean;
}
