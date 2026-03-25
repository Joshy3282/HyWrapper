import { HypixelResponse } from "../../types";

export interface OnlineResponse extends HypixelResponse {
    uuid?: string;
    session?: Session;
}

export interface Session {
    online?: boolean;
}
