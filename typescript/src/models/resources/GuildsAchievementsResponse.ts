import { HypixelResponse } from "../../types";

export interface GuildsAchievementsResponse extends HypixelResponse {
    lastUpdated?: number;
    one_time?: Record<string, GuildOneTimeAchievement>;
    tiered?: Record<string, GuildTieredAchievement>;
}

export interface GuildOneTimeAchievement {
    name?: string;
    description?: string;
}

export interface GuildTieredAchievement {
    name?: string;
    description?: string;
    tiers?: GuildAchievementTier[];
}

export interface GuildAchievementTier {
    tier?: number;
    amount?: number;
}
