import { HypixelResponse } from "../../types";

export interface VanityResponse extends HypixelResponse {
    lastUpdated?: number;
    types?: Type[];
    rarities?: Rarity[];
}

export interface Type {
    key?: string;
    name?: string;
    rarity?: string;
    package?: string;
}

export interface Rarity {
    name?: string;
    color?: string;
}
