from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.skyblock.skill_type import SkillType
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class SkillsResponse(HypixelResponse):
    """
    Lists information about skills.

    :param success: Whether the request was successful.
    :param cause: The cause of the error, if the request failed.
    :param lastUpdated: The timestamp skills was last updated.
    :param version: SkyBlocks current version.
    :param skills: A list of [SkillType] containing information.
    """

    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: Optional[int] = Field(default=None)
    version: Optional[str] = Field(default=None)
    skills: Optional[Dict[SkillType, Skill]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)

    def get_skill(self, skill_type: SkillType) -> Optional[Skill]:
        """
        Get [Skill] information from a [SkillType]

        :param skillType: The [SkillType] to get.
        """
        if self.skills is None:
            return None
        return self.skills.get(skill_type)


class Skill(BaseModel):
    """
    Information about a skill

    :param name: The name of the skill (eg; Farming, Mining)
    :param description: The skills description
    :param maxLevel: Maximum level possible for the skill, including level cap increases.
    :param levels: A list of information and rewards about each level for a skill
    """

    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    maxLevel: Optional[int] = Field(default=None)
    levels: Optional[List[Level]] = Field(default=None)


class Level(BaseModel):
    """
    Information and rewards about a level

    :param level: The skill level
    :param totalExpRequired: The total amount of experience required for the level
    :param unlocks: A list of rewards for the level (eg; +250 Coins, +5 SkyBlock XP)
    """

    model_config = ConfigDict(populate_by_name=True)
    level: Optional[int] = Field(default=None)
    totalExpRequired: Optional[float] = Field(default=None)
    unlocks: Optional[List[str]] = Field(default=None)
