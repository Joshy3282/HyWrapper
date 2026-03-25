export interface MiningCore {
    received_free_tier?: boolean;
    tokens?: number;
    powder_mithril?: number;
    powder_mithril_total?: number;
    powder_spent_mithril?: number;
    retroactive_tier2_token?: boolean;
    daily_ores_mined_day?: number;
    daily_ores_mined?: number;
    crystals?: Record<string, Crystal>;
    greater_mines_last_access?: number;
    biomes?: Biomes;
    powder_gemstone?: number;
    powder_gemstone_total?: number;
    powder_spent_gemstone?: number;
    daily_ores_mined_day_gemstone?: number;
    daily_ores_mined_gemstone?: number;
    daily_ores_mined_day_mithril_ore?: number;
    daily_ores_mined_mithril_ore?: number;
    daily_ores_mined_day_glacite?: number;
    daily_ores_mined_glacite?: number;
    powder_glacite?: number;
    powder_glacite_total?: number;
    powder_spent_glacite?: number;
    /** TODO enum */
    current_daily_effect?: string;
    current_daily_effect_last_changed?: number;
}

export interface Crystal {
    state?: string;
    total_placed?: number;
    total_found?: number;
}

export interface Biomes {
    precursor?: Precursor;
    dwarven?: Record<string, any>;
    goblin?: Goblin;
    jungle?: Jungle;
}

export interface Precursor {
    claiming_with_precursor_apparatus?: boolean;
    talked_to_professor?: boolean;
}

export interface Goblin {
    king_quest_active?: boolean;
    king_quests_completed?: number;
}

export interface Jungle {
    jungle_temple_open?: boolean;
    jungle_temple_chest_uses?: number;
}
