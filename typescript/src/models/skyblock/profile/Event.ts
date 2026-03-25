export interface Event {
    easter?: Easter;
}

export interface Easter {
    rabbits?: Record<string, any>;
    time_tower?: TimeTower;
    /** TODO enum */
    employees?: Record<string, number>;
    chocolate?: number;
    total_chocolate?: number;
    chocolate_since_prestige?: number;
    last_viewed_chocolate_factory?: number;
    shop?: Shop;
    rabbit_barn_capacity_level?: number;
    chocolate_level?: number;
    rabbit_sort?: string;
    rabbit_filter?: string;
    supreme_chocolate_bars?: number;
    click_upgrades?: number;
    chocolate_multiplier_upgrades?: number;
    rabbit_rarity_upgrades?: number;
    refined_dark_cacao_truffles?: number;
    el_dorado_progress?: number;
    rabbit_hitmen?: RabbitHitmen;
    golden_click_amount?: number;
    golden_click_year?: number;
    rabbit_hotspot_filer?: string;
}

export interface TimeTower {
    charges?: number;
    activation_time?: number;
    level?: number;
}

export interface Shop {
    year?: number;
    /** TODO enum */
    rabbits?: string[];
    chocolate_spent?: number;
    cocoa_fortune_upgrades?: number;
}

export interface RabbitHitmen {
    rabbit_hitmen_slots?: number;
    missed_uncollected_eggs?: number;
    egg_slot_cooldown_mark?: number;
    egg_slot_cooldown_sum?: number;
}
