import { HypixelResponse } from "../../types";
import { SkillType } from "../../data/skyblock/SkillType";

/**
 * Information about collections.
 */
export interface CollectionsResponse extends HypixelResponse {
    /** Timestamp when collections were last modified. */
    lastUpdated?: number;
    /** Skyblock version. */
    version?: string;
    /** The list of collection information. */
    collections?: Record<string, Collection>;
}

/**
 * List of all collections.
 */
export interface Collection {
    /** Skill name of the collection. */
    name?: string; // TODO change this to skill enum
    /** List of collection items for the skill. */
    items?: Record<string, CollectionItem>;
}

/**
 * Information about a collection.
 */
export interface CollectionItem {
    /** Name of the collection. */
    name?: string;
    /** Max amount of tiers in the collection. */
    maxTiers?: number;
    /** List of tiers information. */
    tiers?: CollectionTier[];
}

/**
 * Information about a collection item tier.
 */
export interface CollectionTier {
    /** What tier it is. */
    tier?: number;
    /** The collected amount required for the tier. */
    amountRequired?: number;
    /** A list of what the tier unlocks once reached. */
    unlocks?: string[];
}

/**
 * Helper class to provide methods similar to the Kotlin version.
 */
export class CollectionsResponseHelper {
    /**
     * Retrieves a collection from the collections response by skill type.
     *
     * @param response The collections response.
     * @param skill The skill type.
     * @returns The collection data, or undefined if not found.
     */
    public static getCollection(response: CollectionsResponse, skill: SkillType): Collection | undefined {
        return response.collections?.[skill];
    }
}
