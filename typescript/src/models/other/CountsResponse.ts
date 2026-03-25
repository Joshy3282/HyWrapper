import { HypixelResponse } from "../../types";

export interface CountsResponse extends HypixelResponse {
    games?: Record<string, GameCount>;
    playerCount?: number;
}

export interface GameCount {
    players?: number;
    modes?: Record<string, number>;
}
