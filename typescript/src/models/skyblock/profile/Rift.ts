export interface Rift {
    village_plaza?: VillagePlaza;
    wither_cage?: WitherCage;
    black_lagoon?: BlackLagoon;
    dead_cats?: DeadCats;
    wizard_tower?: WizardTower;
    enigma?: Enigma;
    slayer_quest?: SlayerQuest;
    /** TODO enum? */
    lifetime_purchased_boundaries?: string[];
    west_village?: WestVillage;
    wyld_woods?: WyldWoods;
    castle?: Castle;
    access?: Access;
    dreadfarm?: Dreadfarm;
    inventory?: RiftInventory;
}

export interface VillagePlaza {
    murder?: Murder;
    barryCenter?: BarryCenter;
    cowboy?: Cowboy;
    barter_bank?: Record<string, any>;
    lonely?: Lonely;
    seraphine?: Seraphine;
    got_scammed?: boolean;
}

export interface Murder {
    step_index?: number;
    room_clues?: string[];
    step_index_pt2?: number;
    step_index_pt3?: number;
}

export interface BarryCenter {
    first_talk_to_barry?: boolean;
    convinced?: string[];
    received_reward?: boolean;
}

export interface Cowboy {
    stage?: number;
    hay_eaten?: number;
    rabbit_name?: string;
    exported_carrots?: number;
}

export interface Lonely {
    seconds_sitting?: number;
}

export interface Seraphine {
    step_index?: number;
}

export interface WitherCage {
    killed_eyes?: string[];
}

export interface BlackLagoon {
    talked_to_edwin?: boolean;
    received_science_paper?: boolean;
    completed_step?: number;
    delivered_science_paper?: boolean;
}

export interface DeadCats {
    talked_to_jacquelle?: boolean;
    picked_up_detector?: boolean;
    found_cats?: string[];
    unlocked_pet?: boolean;
    montezuma?: Montezuma;
}

export interface Montezuma {
    uuid?: string;
    uniqueId?: string;
    type?: string;
    exp?: number;
    active?: boolean;
    tier?: string;
    held_item?: string;
    candy_used?: number;
    pet_soulbound?: boolean;
    skin?: string;
    extra?: Record<string, any>;
}

export interface WizardTower {
    wizard_quest_step?: number;
    crumbs_laid_out?: number;
}

export interface Enigma {
    bought_cloak?: boolean;
    /** TODO enum */
    found_souls?: string[];
    claimed_bonus_index?: number;
}

export interface Gallery {
    elise_step?: number;
    secured_trophies?: SecuredTrophy[];
    /** TODO enum maybe? not too helpful */
    sent_trophy_dialogues?: string[];
}

export interface SecuredTrophy {
    type?: string;
    timestamp?: number;
    visits?: number;
}

export interface SlayerQuest {
    type?: string;
    tier?: number;
    start_timestamp?: number;
    completion_state?: number;
    used_armor?: boolean;
    solo?: boolean;
    combat_xp?: number;
    recent_mob_kills?: RecentMobKill[];
    last_killed_mob_island?: string;
    spawn_timestamp?: number;
}

export interface RecentMobKill {
    xp?: number;
    timestamp?: number;
}

export interface WestVillage {
    crazy_kloon?: CrazyKloon;
    mirrorverse?: Mirrorverse;
    kat_house?: KatHouse;
    glyph?: Glyph;
}

export interface CrazyKloon {
    /** TODO enum */
    selected_colors?: Record<string, string>;
    talked?: boolean;
    /** TODO enum??? its just numbers */
    hacked_terminals?: string[];
    quest_complete?: boolean;
}

export interface Mirrorverse {
    /** TODO enum */
    visited_rooms?: string[];
    upside_down_hard?: boolean;
    /** TODO item enum */
    claimed_chest_items?: string[];
    claimed_reward?: boolean;
}

export interface KatHouse {
    bin_collected_silverfish?: number;
    bin_collected_spider?: number;
    bin_collected_mosquito?: number;
}

export interface Glyph {
    claimed_wand?: boolean;
    current_glyph_delivered?: boolean;
    current_glyph_completed?: boolean;
    current_glyph?: number;
    completed?: boolean;
    claimed_bracelet?: boolean;
}

export interface WyldWoods {
    sirius_started_q_a?: boolean;
    sirius_q_a_chain_done?: boolean;
    sirius_completed_q_a?: boolean;
    sirius_claimed_doubloon?: boolean;
    /** TODO enum? */
    talked_threebrothers?: string[];
    bughunter_step?: number;
}

export interface Castle {
    unlocked_pathway_skip?: boolean;
    fairy_step?: number;
    grubber_stacks?: number;
}

export interface Access {
    last_free?: number;
    consumed_prism?: boolean;
    charge_track_timestamp?: number;
}

export interface Dreadfarm {
    shania_stage?: number;
    caducous_feeder_uses?: number[];
}

export interface RiftInventory {
    inv_contents?: InventoryData;
    inv_armor?: InventoryData;
    ender_chest_contents?: InventoryData;
    ender_chest_page_icons?: (InventoryData | null)[];
    equipment_contents?: InventoryData;
}

export interface InventoryData {
    type?: number;
    data?: string;
}
