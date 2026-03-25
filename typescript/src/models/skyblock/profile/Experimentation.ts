export interface Experimentation {
    simon?: Simon;
    pairings?: Pairings;
    numbers?: Numbers;
    claims_resets?: number;
    claims_resets_timestamp?: number;
    serums_drank?: number;
    claimed_retroactive_rng?: boolean;
    charge_track_timestamp?: number;
}

export interface Simon {
    last_attempt?: number;
    last_claimed?: number;
    bonus_clicks?: number;
    claimed?: boolean;

    attempts_0?: number;
    claims_0?: number;
    best_score_0?: number;

    attempts_1?: number;
    claims_1?: number;
    best_score_1?: number;

    attempts_2?: number;
    claims_2?: number;
    best_score_2?: number;

    attempts_3?: number;
    claims_3?: number;
    best_score_3?: number;

    attempts_4?: number;
    claims_4?: number;
    best_score_4?: number;

    attempts_5?: number;
    claims_5?: number;
    best_score_5?: number;
}

export interface Pairings {
    last_attempt?: number;
    last_claimed?: number;
    bonus_clicks?: number;
    claimed?: boolean;

    attempts_0?: number;
    claims_0?: number;
    best_score_0?: number;

    attempts_1?: number;
    claims_1?: number;
    best_score_1?: number;

    attempts_2?: number;
    claims_2?: number;
    best_score_2?: number;

    attempts_3?: number;
    claims_3?: number;
    best_score_3?: number;

    attempts_4?: number;
    claims_4?: number;
    best_score_4?: number;

    attempts_5?: number;
    claims_5?: number;
    best_score_5?: number;
}

export interface Numbers {
    last_attempt?: number;
    last_claimed?: number;
    bonus_clicks?: number;
    claimed?: boolean;

    attempts_0?: number;
    claims_0?: number;
    best_score_0?: number;

    attempts_1?: number;
    claims_1?: number;
    best_score_1?: number;

    attempts_2?: number;
    claims_2?: number;
    best_score_2?: number;

    attempts_3?: number;
    claims_3?: number;
    best_score_3?: number;

    attempts_4?: number;
    claims_4?: number;
    best_score_4?: number;

    attempts_5?: number;
    claims_5?: number;
    best_score_5?: number;
}
