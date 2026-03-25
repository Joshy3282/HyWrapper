import { HypixelResponse } from "../../types";

export interface QuestsResponse extends HypixelResponse {
    lastUpdated?: number;
    quests?: Record<string, Quest[]>;
}

export interface Quest {
    id?: string;
    name?: string;
    description?: string;
    rewards?: QuestReward[];
    objectives?: QuestObjective[];
    requirements?: QuestRequirement[];
}

export interface QuestReward {
    type?: string;
    amount?: number;
}

export interface QuestObjective {
    id?: string;
    type?: string;
    integer?: number;
}

export interface QuestRequirement {
    type?: string;
}
