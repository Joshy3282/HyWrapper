import { HypixelResponse } from "../../types";
import { SkillType } from "../../data/skyblock/SkillType";

/**
 * Lists information about skills.
 */
export interface SkillsResponse extends HypixelResponse {
    /**
     * The timestamp skills was last updated.
     */
    lastUpdated?: number;
    /**
     * SkyBlocks current version.
     */
    version?: string;
    /**
     * A list of {@link SkillType} containing information.
     */
    skills?: Record<SkillType, Skill>;
}

/**
 * Information about a skill
 */
export interface Skill {
    /**
     * The name of the skill (eg; Farming, Mining)
     */
    name?: string;
    /**
     * The skill's description
     */
    description?: string;
    /**
     * Maximum level possible for the skill, including level cap increases.
     */
    maxLevel?: number;
    /**
     * A list of information and rewards about each level for a skill
     */
    levels?: Level[];
}

/**
 * Information and rewards about a level
 */
export interface Level {
    /**
     * The skill level
     */
    level?: number;
    /**
     * The total amount of experience required for the level
     */
    totalExpRequired?: number;
    /**
     * A list of rewards for the level (eg; +250 Coins, +5 SkyBlock XP)
     */
    unlocks?: string[];
}
