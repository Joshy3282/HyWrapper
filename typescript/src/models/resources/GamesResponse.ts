import { HypixelResponse } from "../../types";

export interface GamesResponse extends HypixelResponse {
    lastUpdated?: number;
    games?: Record<string, Game>;
}

export interface Game {
    id?: number;
    name?: string;
    databaseName?: string;
    modeNames?: Record<string, string>;
    legacy?: boolean;
    retired?: boolean;
}
