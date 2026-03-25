import { HypixelResponse } from "../../types";
import { MuseumItem } from "../../data/skyblock/MuseumItem";
import { StatType } from "../../data/skyblock/StatType";

export interface ItemsResponse extends HypixelResponse {
    lastUpdated?: number;
    items?: Item[];
}

export interface Item {
    material?: string;
    durability?: number;
    skin?: Skin;
    name?: string;
    category?: string;
    tier?: string;
    npc_sell_price?: number;
    id?: string;
    salvages?: Salvage[];
    rarity_salvageable?: boolean;
    description?: string;
    item_model?: string;
    stats?: Record<StatType, number>;
    unstackable?: boolean;
    dungeon_item_conversion_cost?: DungeonItemConversionCost;
    upgrade_costs?: UpgradeCost[][];
    museum_data?: MuseumData;
    requirements?: Requirement[];
    color?: string;
    soulbound?: string;
    has_uuid?: boolean;
    can_auction?: boolean;
    gemstone_slots?: GemstoneSlot[];
    glowing?: boolean;
    can_trade?: boolean;
    can_place?: boolean;
    museum?: boolean;
    generator?: string;
    generator_tier?: number;
    furniture?: string;
    item_specific?: Record<string, any>;
    editioned?: boolean;
    gear_score?: number;
    dungeon_item?: boolean;
    catacombs_requirements?: CatacombsRequirement;
    can_have_booster?: boolean;
    hide_from_api?: boolean;
    can_recombobulate?: boolean;
    salvageable_from_recipe?: boolean;
    motes_sell_price?: number;
    double_tap_to_drop?: boolean;
    enchantments?: Record<string, number>;
    rift_transferrable?: boolean;
    origin?: string;
    hide_from_viewrecipe_command?: boolean;
    force_wipe_recomb?: boolean;
    ability_damage_scaling?: number;
    tiered_stats?: Record<StatType, number[]>;
    crystal?: string;
    can_burn_in_furnace?: boolean;
    salvage?: SalvageData;
    serializable?: boolean;
    can_have_attributes?: boolean;
    can_interact?: boolean;
    can_interact_right_click?: boolean;
    private_island?: string;
    can_have_power_scroll?: boolean;
    can_interact_entity?: boolean;
    MINING_FORTUNE?: number;
    rarity?: string;
    sword_type?: string;
    is_upgradeable_without_soulbinding?: boolean;
    recipes?: Recipe[];
    cannot_reforge?: boolean;
    lose_motes_value_on_transfer?: boolean;
    prestige?: Prestige;
}

export interface Skin {
    value?: string;
    signature?: string;
}

export interface Salvage {
    type?: string;
    essence_type?: string;
    amount?: number;
}

export interface SalvageData {
    item_id?: string;
    amount?: number;
}

export interface DungeonItemConversionCost {
    essence_type?: string;
    amount?: number;
}

export interface UpgradeCost {
    type?: string;
    essence_type?: string;
    amount?: number;
    item_id?: string;
}

export interface MuseumData {
    category?: string;
    parent?: Record<MuseumItem, MuseumItem>;
    armor_set_donation_xp?: Record<MuseumItem, number>;
    game_stage?: string;
}

export interface CatacombsRequirement {
    type?: string;
    dungeon_type?: string;
    level?: number;
}

export interface Requirement {
    type?: string;
    skill?: string;
    slayer_boss_type?: string;
    level?: number;
    dungeon_type?: string;
}

export interface GemstoneSlot {
    slot_type?: string;
    costs?: GemstoneCost[];
    requirements?: GemstoneRequirement[];
}

export interface GemstoneCost {
    type?: string;
    item_id?: string;
    amount?: number;
    coins?: number;
    essence_type?: string;
}

export interface GemstoneRequirement {
    type?: string;
    data_key?: string;
    value?: string;
    operator?: string;
}

export interface Recipe {
    output?: RecipeOutput;
    ingredient_symbols?: Record<string, string>;
    matrix?: (string | null)[];
}

export interface RecipeOutput {
    item_id?: string;
}

export interface Prestige {
    item_id?: string;
    costs?: GemstoneCost[];
}
