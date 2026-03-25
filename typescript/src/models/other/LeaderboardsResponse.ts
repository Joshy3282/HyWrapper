import { HypixelResponse } from "../../types";

export interface LeaderboardsResponse extends HypixelResponse {
    leaderboards?: Record<string, Leaderboard[]>;
}

export interface Leaderboard {
    path?: string;
    prefix?: string;
    title?: string;
    location?: string;
    count?: number;
    leaders?: string[];
}
