export enum HousingSetting {
    TIPS = "TIPS",
    VISIBILITY = "VISIBILITY",
    BORDER = "BORDER",
    PRO_TOOLS_PARTICLES = "PRO_TOOLS_PARTICLES",
    HOUSING_PLUS_PREFIX = "HOUSING_PLUS_PREFIX",
    JUKEBOX_MUSIC = "JUKEBOX_MUSIC",
}

export interface HousingSettingData {
    cleanName: string;
    type: "boolean" | "number";
}

export const HousingSettingInfo: Record<HousingSetting, HousingSettingData> = {
    [HousingSetting.TIPS]: { cleanName: "Tips", type: "boolean" },
    [HousingSetting.VISIBILITY]: { cleanName: "Visibility", type: "number" },
    [HousingSetting.BORDER]: { cleanName: "Border", type: "boolean" },
    [HousingSetting.PRO_TOOLS_PARTICLES]: { cleanName: "Pro Tools Particles", type: "boolean" },
    [HousingSetting.HOUSING_PLUS_PREFIX]: { cleanName: "Housing Plus Prefix", type: "boolean" },
    [HousingSetting.JUKEBOX_MUSIC]: { cleanName: "Jukebox Music", type: "boolean" },
};
