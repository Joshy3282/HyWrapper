import { HypixelResponse } from "../../types";

/**
 * List of all active Houses.
 */
export interface HousingActiveResponse extends HypixelResponse {
    /**
     * A list of {@link House}.
     */
    houses?: House[];
}

/**
 * Information about a House.
 */
export interface HousingHouseResponse extends HypixelResponse {
    /**
     * The {@link House} details.
     */
    house?: House;
}

/**
 * House information
 */
export interface House {
    /**
     * The UUID of the house.
     */
    uuid?: string;
    /**
     * The UUID of the player who owns the house.
     */
    owner?: string;
    /**
     * The display name of the house.
     */
    name?: string;
    /**
     * The timestamp when the house was created.
     */
    createdAt?: number;
    /**
     * The current number of players in the house.
     */
    players?: number;
    /**
     * The {@link Cookies} statistics for the house.
     */
    cookies?: Cookies;
}

/**
 * Cookie information.
 */
export interface Cookies {
    /**
     * The current number of cookies the house has received.
     */
    current?: number;
}

/**
 * List of a player's houses.
 */
export interface HousingHousesResponse extends HypixelResponse {
    /**
     * A list of {@link House} belonging to the player.
     */
    houses?: House[];
}
