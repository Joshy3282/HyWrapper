import { HypixelResponse } from "../../types";

export interface RecentGamesResponse extends HypixelResponse {
    uuid?: string;
    games?: RecentGame[];
}

export interface RecentGame {
    date?: number;
    gameType?: string;
    mode?: string;
    map?: string;
    ended?: number;
}
