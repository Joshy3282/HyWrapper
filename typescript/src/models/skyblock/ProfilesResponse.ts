import { HypixelResponse } from "../../types";
import { Profile } from "./ProfileResponse";

export interface ProfilesResponse extends HypixelResponse {
    profiles?: Profile[];
}
