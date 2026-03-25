import { HypixelResponse } from "../../types";

/**
 * Information about the current election and next election.
 */
export interface ElectionResponse extends HypixelResponse {
    /** Timestamp of when the information was last updated. */
    lastUpdated?: number;
    /** Information about the current mayor and election results. */
    mayor?: Mayor;
    /** Information about the next election. */
    current?: Election;
}

/**
 * Information about the current Mayor.
 */
export interface Mayor {
    /** Type of mayor (eg; economist {Diaz}, farming {Finnegan}). */
    key?: string;
    /** Name of the mayor. */
    name?: string;
    /** A list of the current mayor's perks. */
    perks?: Perk[];
    /** Information about the current Minister. */
    minister?: Minister;
    /** Information about the past election. */
    election?: Election;
}

/**
 * Information about the current Minister.
 */
export interface Minister {
    /** Type of minister (eg; economist {Diaz}, farming {Finnegan}). */
    key?: string;
    /** Name of the minister. */
    name?: string;
    /** The minister's current perk. */
    perk?: Perk;
}

/**
 * Information about a mayor perk.
 */
export interface Perk {
    /** Name of the perk (eg; Pest Eradicator, Volume Trading). */
    name?: string;
    /** Description about the perk. */
    description?: string;
    /** Whether or not the perk is the mayor's minister perk. */
    minister?: boolean;
}

/**
 * Information about an election.
 */
export interface Election {
    /** What year the election is for. */
    year?: number;
    /** A list of {@link Candidate} for this election. */
    candidates?: Candidate[];
}

/**
 * Information about a candidate
 */
export interface Candidate {
    /** Type of candidate (eg; economist {Diaz}, farming {Finnegan}). */
    key?: string;
    /** Name of the candidate. */
    name?: string;
    /** A list of the candidate perks. */
    perks?: Perk[];
    /** The amount of votes the candidate has. */
    votes?: number;
}
