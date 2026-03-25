export enum GardenUpgrade {
    GROWTH_SPEED = "GROWTH_SPEED",
    CROP_UPGRADE = "YIELD",
    PLOT_LIMIT = "PLOT_LIMIT",
}

export const GardenUpgradeInfo: Record<GardenUpgrade, string> = {
    [GardenUpgrade.GROWTH_SPEED]: "Crop Growth Speed",
    [GardenUpgrade.CROP_UPGRADE]: "Crop Upgrade",
    [GardenUpgrade.PLOT_LIMIT]: "Plot Limit",
};
