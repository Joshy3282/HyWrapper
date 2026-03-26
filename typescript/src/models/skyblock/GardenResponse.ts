import { HypixelResponse } from "../../types";
import { GardenPlot } from "../../data/skyblock/GardenPlot";
import { GardenResource } from "../../data/skyblock/GardenResource";
import { GardenUpgrade } from "../../data/skyblock/GardenUpgrade";
import { Visitor } from "../../data/skyblock/Visitor";

/**
 * Information about a player's Garden.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property garden Information about the Garden.
 */
export interface GardenResponse extends HypixelResponse {
    garden?: Garden;
}

/**
 * Information about a player's Garden.
 *
 * @property uuid Garden UUID.
 * @property unlockedPlots A list of [GardenPlot] that have been unlocked.
 * @property commissionData Information about visitor commissions.
 * @property resourcesCollected The amount of each [GardenResource] collected.
 * @property gardenExperience The amount of garden experience gained.
 * @property activeCommissions A list of active visitor commissions.
 * @property composterData Information about the Garden's composter.
 * @property selectedBarnSkin The current selected Barn skin.
 * @property cropUpgradeLevels The upgrade level of each [GardenResource].
 * @property gardenUpgrades The upgrade level of each [GardenUpgrade].
 * @property unlockedBarnSkins A list of all unlocked Barn skins.
 * @property greenhouseSlots Unknown.
 * @property lastGrowthStageTime Timestamp of the last Greenhouse growth.
 */
export interface Garden {
    uuid?: string;
    unlockedPlots?: GardenPlot[];
    commissionData?: CommissionData;
    resourcesCollected?: Record<GardenResource, number>;
    gardenExperience?: number;
    activeCommissions?: any[]; // TODO empty in tests
    composterData?: ComposterData;
    selectedBarnSkin?: string; // TODO change to enum
    cropUpgradeLevels?: Record<GardenResource, number>;
    gardenUpgrades?: Record<GardenUpgrade, number>;
    unlockedBarnSkins?: string[]; // TODO change to enum
    greenhouseSlots?: GreenhouseCoordinate[]; // TODO unknown
    lastGrowthStageTime?: number;
}

/**
 * Information about visitor commissions.
 *
 * @property visits A list of how many times each visitor has visited.
 * @property completed A list of how many times each visitor's commission has been completed.
 * @property totalCompleted Total amount of visitor commissions completed.
 * @property uniqueVisitorsServed How many unique visitors' commissions have been completed.
 */
export interface CommissionData {
    visits?: Record<Visitor, number>;
    completed?: Record<Visitor, number>;
    totalCompleted?: number;
    uniqueVisitorsServed?: number;
}

/**
 * Information about the Garden's composter.
 *
 * @property organicMatter The amount of organic matter currently in the composter.
 * @property fuel The amount of fuel currently in the composter.
 * @property compostUnits Either this or compostItems are the amount of compost in the composter, the other is unknown.
 * @property compostItems Either this or compostUnits are the amount of compost in the composter, the other is unknown.
 * @property conversionTicks Unknown.
 * @property lastSave The timestamp the composter was last modified (eg; fuel put in, compost taken).
 * @property upgrades Upgrades levels for the composter.
 */
export interface ComposterData {
    organicMatter?: number;
    fuel?: number;
    compostUnits?: number;
    compostItems?: number;
    conversionTicks?: number;
    lastSave?: number;
    upgrades?: ComposterUpgrades;
}

/**
 * Upgrade levels for the composter.
 *
 * @property speed The speed upgrade of the composter.
 * @property multiDrop The multi drop upgrade of the composter.
 * @property fuelCap The fuel cap upgrade of the composter.
 * @property organicMatterCap The organic matter cap of the composter.
 * @property costReduction The cost reduction cap of the composter.
 */
export interface ComposterUpgrades {
    speed?: number;
    multiDrop?: number;
    fuelCap?: number;
    organicMatterCap?: number;
    costReduction?: number;
}

export interface GreenhouseCoordinate {
    x?: number;
    y?: number;
}
