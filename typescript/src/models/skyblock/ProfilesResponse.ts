import { HypixelResponse } from "../../types";
import { Profile } from "./ProfileResponse";

/**
 * Information about a player's profiles
 */
export interface ProfilesResponse extends HypixelResponse {
    /** A list of the player's profiles */
    profiles?: Profile[];
}
