import { GameType } from "../../data/GameType";
import { HypixelResponse } from "../../types";

export interface BoostersResponse extends HypixelResponse {
    boosters?: Booster[];
    boosterState?: BoosterState;
}

export interface Booster {
    _id?: string;
    purchaserUuid?: string;
    amount?: number;
    originalLength?: number;
    length?: number;
    gameType?: GameType;
    dateActivated?: number;
    stacked?: string[];
}

export interface BoosterState {
    decrementing?: boolean;
}
