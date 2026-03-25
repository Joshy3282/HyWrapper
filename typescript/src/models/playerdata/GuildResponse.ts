import { HypixelResponse } from "../../types";

export interface GuildResponse extends HypixelResponse {
    guild?: Guild;
}

export interface Guild {
    _id?: string;
    name?: string;
    name_lower?: string;
    coins?: number;
    coinsEver?: number;
    created?: number;
    members?: GuildMember[];
    ranks?: Rank[];
    achievements?: Record<string, number>;
    exp?: number;
    tagColor?: string;
    banner?: Banner;
    publiclyListed?: boolean;
    preferredGames?: string[];
    description?: string;
    chatMute?: number;
    tag?: string;
    guildExpByGameType?: Record<string, number>;
}

export interface GuildMember {
    uuid?: string;
    rank?: string;
    joined?: number;
    questParticipation?: number;
    mutedTill?: number;
    expHistory?: Record<string, number>;
}

export interface Rank {
    name?: string;
    default?: boolean;
    tag?: string;
    created?: number;
    priority?: number;
}

export interface Banner {
    Base?: string;
    Patterns?: Pattern[];
}

export interface Pattern {
    Pattern?: string;
    Color?: string;
}
