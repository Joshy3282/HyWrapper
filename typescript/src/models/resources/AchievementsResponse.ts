import { HypixelResponse } from "../../types";

export interface AchievementsResponse extends HypixelResponse {
    lastUpdated?: number;
    achievements?: Record<string, GameAchievement>;
}

export interface GameAchievement {
    one_time?: Record<string, OneTimeAchievement>;
    tiered?: Record<string, TieredAchievement>;
    total_points?: number;
    total_legacy_points?: number;
}

export interface OneTimeAchievement {
    name?: string;
    description?: string;
    points?: number;
    gamePercentUnlocked?: number;
    globalPercentUnlocked?: number;
}

export interface TieredAchievement {
    name?: string;
    description?: string;
    tiers?: AchievementTier[];
}

export interface AchievementTier {
    tier?: number;
    points?: number;
    amount?: number;
}
