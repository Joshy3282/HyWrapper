export interface CrimsonIslePlayerData {
    quests?: CrimsonIsleQuests;
    /** TODO enum */
    kuudra_completed_tiers?: Record<string, number>;
    /** TODO enum */
    dojo?: Record<string, number>;
    abiphone?: Abiphone;
    matriarch?: Matriarch;
    barbarians_reputation?: number;
    mages_reputation?: number;
    /** TODO enum */
    selected_faction?: string;
    /** TODO enum */
    last_minibosses_killed?: string[];
    kuudra_party_finder?: KuudraPartyFinder;
    barbarians_reputation_highest?: number;
}

export interface CrimsonIsleQuests {
    quest_data?: Record<string, any>;
    miniboss_daily?: Record<string, any>;
    kuudra_boss_daily?: Record<string, any>;
    quest_rewards?: QuestRewards;
    alchemist_quest?: AlchemistQuest;
    rulenor?: Record<string, any>;
    chicken_quest?: ChickenQuest;
    pomtair_quest?: PomtairQuest;
    suus_quest?: SuusQuest;
    pablo_quest?: PabloQuest;
    duel_training_quest?: DuelTrainingQuest;
    sirih_quest?: SirihQuest;
    edelis_quest?: Record<string, any>;
    mollim_quest?: Record<string, any>;
    aranya_quest?: Record<string, any>;
    last_reset?: number;
    paid_bruuh?: boolean;
    /** TODO enum */
    miniboss_data?: Record<string, boolean>;
    found_kuudra_book?: boolean;
    kuudra_loremaster?: boolean;
    found_kuudra_chestplate?: boolean;
    found_kuudra_boots?: boolean;
    last_believer_blessing?: number;
    fished_wet_napkin?: boolean;
    weird_sailor?: boolean;
    found_kuudra_helmet?: boolean;
    found_kuudra_leggings?: boolean;
    last_kuudra_relic?: number;
    /** TODO enum */
    unlocked_cavity_npcs?: string[];
    /** TODO enum */
    cavity_rarity?: string;
}

export interface QuestRewards {
    WITHER_SOUL?: number;
    BEZOS?: number;
    FLAMING_HEART?: number;
    CORRUPTED_FRAGMENT?: number;
    LUMINO_FIBER?: number;
    crimson_isle_dojo_test_of_mob_kb_drating_c?: string;
    crimson_isle_fetch_tentacle_meat_c?: string;
    crimson_isle_soulfish_b?: string;
    crimson_isle_kill_ashfang_a?: string;
    crimson_isle_rescue_s?: string;
}

export interface AlchemistQuest {
    alchemist_quest_start?: boolean;
    alchemist_quest_progress?: number;
}

export interface ChickenQuest {
    chicken_quest_progress?: number;
    chicken_quest_start?: boolean;
    chicken_quest_collected?: any[];
}

export interface PomtairQuest {
    talked_to_npc?: boolean;
}

export interface SuusQuest {
    talked_to_npc?: boolean;
    last_toy_drop?: number;
    last_completion?: number;
}

export interface PabloQuest {
    pablo_active?: boolean;
    pablo_item?: string;
}

export interface DuelTrainingQuest {
    duel_training_phase_barbarians?: number;
    duel_training_last_complete_barbarians?: number;
}

export interface SirihQuest {
    sulphur_given?: number;
    last_give?: number;
}

export interface Abiphone {
    contact_data?: Record<string, any>;
    games?: Record<string, any>;
    operator_chip?: OperatorChip;
    /** TODO enum */
    active_contacts?: string[];
    trio_contact_addons?: number;
    selected_sort?: string;
    has_used_sirius_personal_phone_number_item?: boolean;
    last_dye_called_year?: number;
}

export interface OperatorChip {
    repaired_index?: number;
}

export interface Matriarch {
    pearls_collected?: number;
    last_attempt?: number;
    recent_refreshes?: number[];
}

export interface KuudraPartyFinder {
    search_settings?: SearchSettings;
    group_builder?: GroupBuilder;
}

export interface SearchSettings {
    tier?: string;
}

export interface GroupBuilder {
    tier?: string;
    note?: string;
    combat_level_required?: number;
}
