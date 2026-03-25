import { HypixelResponse } from "../../types";

export interface PlayerResponse extends HypixelResponse {
    player?: Player;
}

export interface Player {
    _id?: string;
    uuid?: string;
    displayname?: string;
    firstLogin?: number;
    playername?: string;
    achievementsOneTime?: string[];
    achievementPoints?: number;
    // TODO stats. See player/Stats
    housingMeta?: HousingMeta;
    achievementTracking?: string[];
    // TODO achievements. enum needed?
    newPackageRank?: string;
    networkExp?: number;
    // TODO monthly crates. enum needed? done every month? futureproof?
    eugene?: Eugene;
    channel?: string;
    lastAdsenseGenerateTime?: number;
    lastClaimedReward?: number;
    rewardHighScore?: number;
    rewardStreak?: number;
    totalDailyRewards?: number;
    totalRewrads?: number;
    // TODO socialMedia. enum needed?
    // TODO petConsumables. enum needed?
    karma?: number;
    monthlyPackageRank?: string;
    mostRecentMonthlyPackageRank?: string;
    // TODO seasonal. bunch of bullshit here
    // TODO challenges. more bullshit
    vanityMeta?: VanityMeta;
    leveling?: PlayerLeveling;
    rankPlusColor?: string;
    questSettings?: QuestSettings;
    // TODO quests. enum
    tourney?: Tourney;
    fortuneBuff?: number;
    giftedMeta?: GiftedMeta;
    achievementRewardsNew?: Record<string, number>;
    main2017Tutorial?: boolean;
    currentGadget?: string;
    achievementSync?: AchievementSync;
    monthylRankColor?: string;
    // TODO cachedData. enum?
    adsense_tokens?: number;
}

export interface HousingMeta {
    tutorialStep?: string;
    packages?: string[];
    plotSize?: string;
    allowedBlocks?: string[];
    playerSettings?: Record<string, string>;
    // TODO given cookies
    selectedChannels_v3?: string[];
}

export interface Eugene {
    dailyTwoKExp?: number;
}

export interface VanityMeta {
    packages?: string[];
}

export interface PlayerLeveling {
    claimedRewards?: number[];
}

export interface QuestSettings {
    autoActivate?: boolean;
}

export interface Tourney {
    first_join_lobby?: number;
}

export interface GiftedMeta {
    ranksGiven?: number;
    rankgiftingmilestones?: string[];
}

export interface AchievementSync {
    quake_tiered?: number;
}
