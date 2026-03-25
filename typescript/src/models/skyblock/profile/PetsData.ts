export interface PetsData {
    pet_care?: PetCare;
    autopet?: Autopet;
    pets?: PetData[];
}

export interface PetCare {
    coins_spent?: number;
    /** TODO enum */
    pet_types_sacrificed?: string[];
}

export interface Autopet {
    rules_limit?: number;
    rules?: AutopetRule[];
    migrated?: boolean;
    migrated_2?: boolean;
}

export interface AutopetRule {
    uuid?: string;
    /** TODO enum */
    id?: string;
    name?: string;
    uniqueId?: string;
    exceptions?: AutopetException[];
    disabled?: boolean;
    /** TODO enums */
    data?: Record<string, string>;
}

export interface AutopetException {
    id?: string;
    /** TODO enums */
    data?: Record<string, string>;
}

export interface PetData {
    uuid?: string;
    uniqueId?: string;
    /** TODO enum */
    type?: string;
    exp?: number;
    active?: boolean;
    /** TODO enum */
    tier?: string;
    /** TODO enum */
    heldItem?: string;
    candyUsed?: number;
    petSoulbound?: boolean;
    /** TODO enum */
    skin?: string;
    /** TODO enum */
    extra?: Record<string, number>;
}
