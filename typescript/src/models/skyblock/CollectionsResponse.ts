import { HypixelResponse } from "../../types";
import { SkillType } from "../../data/skyblock/SkillType";

export interface CollectionsResponse extends HypixelResponse {
    lastUpdated?: number;
    version?: string;
    collections?: Record<string, Collection>;
}

export interface Collection {
    name?: string;
    items?: Record<string, CollectionItem>;
}

export interface CollectionItem {
    name?: string;
    maxTiers?: number;
    tiers?: CollectionTier[];
}

export interface CollectionTier {
    tier?: number;
    amountRequired?: number;
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
