import { HypixelResponse } from "../../types";
import { MuseumItem as MuseumItemEnum } from "../../data/skyblock/MuseumItem";

/**
 * Information about a player's museum.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property members Information about each members museum in a coop.
 */
export interface MuseumResponse extends HypixelResponse {
    members?: Record<string, MuseumMember>;
}

/**
 * Information about a coop member's museum.
 *
 * @property value The museums valuation when apprased.
 * @property appraisal Whether or not the museum has been appraised.
 * @property items A list of information about each donatable item.
 * @property special A list of special items donated (eg; minion skins, the fishes').
 */
export interface MuseumMember {
    value?: number;
    appraisal?: boolean;
    items?: Record<MuseumItemEnum, MuseumItemInfo>;
    special?: SpecialItemInfo[];
}

/**
 * Information about a specific donatable item
 *
 * @property timeDonated The timestamp the item was donated to museum.
 * @property featuredSlot Slot id of where the item is being featured.
 * @property borrowing Whether the item is donated to museum, but not currently in museum.
 * @property itemData Item data for the donated item.
 */
export interface MuseumItemInfo {
    timeDonated?: number;
    featuredSlot?: string; // TODO enum
    borrowing?: boolean;
    itemData?: MuseumItemData;
}

/**
 * Information about an item donated to the special category
 *
 * @property timeDonated The timestamp the item was donated to museum.
 * @property itemData Item data for the donated item.
 */
export interface SpecialItemInfo {
    timeDonated?: number;
    itemData?: MuseumItemData;
}

/**
 * Item data for a donated item.
 *
 * @property type Unknown
 * @property data gzipped nbt data.
 */
export interface MuseumItemData {
    type?: number; // TODO what is this
    data?: string;
}
