import { HypixelResponse } from "../../types";
import { GardenPlot } from "../../data/skyblock/GardenPlot";
import { GardenResource } from "../../data/skyblock/GardenResource";
import { GardenUpgrade } from "../../data/skyblock/GardenUpgrade";
import { Visitor } from "../../data/skyblock/Visitor";

export interface GardenResponse extends HypixelResponse {
    garden?: Garden;
}

export interface Garden {
    uuid?: string;
    unlocked_plots_ids?: GardenPlot[];
    commission_data?: CommissionData;
    resources_collected?: Record<GardenResource, number>;
    garden_experience?: number;
    active_commissions?: any[];
    composter_data?: ComposterData;
    selected_barn_skin?: string;
    crop_upgrade_levels?: Record<GardenResource, number>;
    garden_upgrades?: Record<GardenUpgrade, number>;
    unlocked_barn_skins?: string[];
    greenhouse_slots?: GreenhouseCoordinate[];
    last_growth_stage_time?: number;
}

export interface CommissionData {
    visits?: Record<Visitor, number>;
    completed?: Record<Visitor, number>;
    total_completed?: number;
    unique_npcs_served?: number;
}

export interface ComposterData {
    organic_matter?: number;
    fuel_units?: number;
    compost_units?: number;
    compost_items?: number;
    conversion_ticks?: number;
    last_save?: number;
    upgrades?: ComposterUpgrades;
}

export interface ComposterUpgrades {
    speed?: number;
    multi_drop?: number;
    fuel_cap?: number;
    organic_matter_cap?: number;
    cost_reduction?: number;
}

export interface GreenhouseCoordinate {
    x?: number;
    y?: number;
}
