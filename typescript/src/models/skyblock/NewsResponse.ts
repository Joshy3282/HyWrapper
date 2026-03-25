import { HypixelResponse } from "../../types";

/**
 * Lists all current news entries. These are viewable through Jerry on the island.
 */
export interface NewsResponse extends HypixelResponse {
    /** The list of current news' information. */
    items?: NewsItem[];
}

/**
 * Information about a news entry
 */
export interface NewsItem {
    /** Title of the entry, usually a version. */
    title?: string;
    /** Description of the entry. */
    text?: string;
    /** The link that opens when clicked. */
    link?: string;
    /** The item in the menu. */
    item?: NewsMaterial;
}

/**
 * Material of the item.
 */
export interface NewsMaterial {
    /** The material of the item. */
    material?: string;
}
