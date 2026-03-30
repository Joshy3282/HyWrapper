import { HypixelResponse } from "../../types";

/**
 * Information about the most recent Bingo.
 */
export interface BingoResponse extends HypixelResponse {
    /** Timestamp of when Bingo was last modified. */
    lastUpdated?: number;
    /** Integer ID of the Bingo event. */
    id?: number;
    /** Name of the Bingo event. */
    name?: string;
    /** Timestamp of the Bingo event's start. */
    start?: number;
    /** Timestamp of the Bingo event's end. */
    end?: number;
    /** What type of Bingo event it is. */
    modifier?: string; // TODO make this an enum
    /** A list of goal information. */
    goals?: Goal[];
}

/**
 * Information about a Bingo goal.
 */
export interface Goal {
    /** ID for the goal. */
    id?: string;
    /** Name of the goal. */
    name?: string;
    /** List of tiers for the goal. */
    tiers?: number[];
    /** Current progress for global goals. */
    progress?: number;
    /** Lore as a string. */
    lore?: string;
    /** Lore as a string list (no different?) // TODO find out */
    fullLore?: string[];
    /** Required amount to complete the goal. */
    requiredAmount?: number;
}
