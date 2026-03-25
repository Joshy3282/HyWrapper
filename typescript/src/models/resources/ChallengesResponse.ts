import { HypixelResponse } from "../../types";

export interface ChallengesResponse extends HypixelResponse {
    lastUpdated?: number;
    challenges?: Record<string, Challenge[]>;
}

export interface Challenge {
    id?: string;
    name?: string;
    rewards?: Reward[];
}

export interface Reward {
    type?: string;
    amount?: number;
}
