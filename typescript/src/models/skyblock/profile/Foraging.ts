export interface Foraging {
    starlyn?: Starlyn;
    /** TODO enum */
    fish_family?: string[];
    hina?: Hina;
    tree_gifts?: TreeGifts;
    songs?: Songs;
}

export interface Starlyn {
    /** TODO enum */
    personal_bests?: Record<string, number>;
}

export interface Hina {
    tasks?: HinaTasks;
}

export interface HinaTasks {
    /** TODO enum */
    completed_tasks?: string[];
    /** TODO enum */
    task_progress?: Record<string, number>;
    /** TODO enum */
    claimed_rewards?: string[];
    tier_claimed?: number;
}

export interface TreeGifts {
    FIG?: number;
    /** TODO enum */
    milestone_tier_claimed?: Record<string, number>;
    MANGROVE?: number;
}

export interface Songs {
    harp?: Harp;
}

export interface Harp {
    claimed_talisman?: boolean;
    selected_song?: string;
    selected_song_epoch?: number;

    // Joy to the World
    song_joy_world_completions?: number;
    song_joy_world_perfect_completions?: number;
    song_joy_world_best_completion?: number;

    // Jeopardy
    song_jeopardy_completions?: number;
    song_jeopardy_perfect_completions?: number;
    song_jeopardy_best_completion?: number;

    // Pure Imagination
    song_pure_imagination_completions?: number;
    song_pure_imagination_perfect_completions?: number;
    song_pure_imagination_best_completion?: number;

    // Through the Campfire (Fire and Flames)
    song_fire_and_flames_completions?: number;
    song_fire_and_flames_perfect_completions?: number;
    song_fire_and_flames_best_completion?: number;

    // Happy Birthday
    song_happy_birthday_completions?: number;
    song_happy_birthday_perfect_completions?: number;
    song_happy_birthday_best_completion?: number;

    // Minuet
    song_minuet_completions?: number;
    song_minuet_perfect_completions?: number;
    song_minuet_best_completion?: number;

    // Amazing Grace
    song_amazing_grace_completions?: number;
    song_amazing_grace_perfect_completions?: number;
    song_amazing_grace_best_completion?: number;

    // Greensleeves
    song_greensleeves_completions?: number;
    song_greensleeves_perfect_completions?: number;
    song_greensleeves_best_completion?: number;

    // La Vie en Rose
    song_vie_en_rose_completions?: number;
    song_vie_en_rose_perfect_completions?: number;
    song_vie_en_rose_best_completion?: number;

    // Brahms' Lullaby
    song_brahms_completions?: number;
    song_brahms_perfect_completions?: number;
    song_brahms_best_completion?: number;

    // Frere Jacques
    song_frere_jacques_completions?: number;
    song_frere_jacques_perfect_completions?: number;
    song_frere_jacques_best_completion?: number;

    // Pachelbel
    song_pachelbel_completions?: number;
    song_pachelbel_perfect_completions?: number;
    song_pachelbel_best_completion?: number;

    // Ode to Joy
    song_hymn_joy_completions?: number;
    song_hymn_joy_perfect_completions?: number;
    song_hymn_joy_best_completion?: number;
}
