from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit

if TYPE_CHECKING:
    from hywrapper.data.skyblock.skill_type import SkillType


class CollectionsResponse(HypixelResponse):
    """
    Information about collections.

    Attributes:
        success: Whether the request was successful.
        cause: The cause of the error, if the request failed.
        last_updated: Timestamp when collections were last modified.
        version: Skyblock version.
        collections: The list of [Collection] information.
    """

    model_config = ConfigDict(populate_by_name=True)
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    version: Optional[str] = Field(default=None)
    collections: Optional[Dict[str, Collection]] = Field(default=None)
    rate_limit: Optional[RateLimit] = Field(default=None, exclude=True, alias="rateLimit")

    def get_collection(self, skill: SkillType) -> Optional[Collection]:
        """
        Retrieves a collection from the collections response by skill type.

        Args:
            skill: The skill type.

        Returns:
            The collection data, or None if not found.
        """
        if self.collections:
            return self.collections.get(skill.name)
        return None


class Collection(BaseModel):
    """
    List of all collections.

    Attributes:
        name: Skill name of the collection.
        items: List of collection items for the skill.
    """

    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = Field(default=None)  # TODO change this to skill enum
    items: Optional[Dict[str, CollectionItem]] = Field(default=None)


class CollectionItem(BaseModel):
    """
    Information about a collection.

    Attributes:
        name: Name of the collection.
        max_tiers: Max amount of tiers in the collection.
        tiers: List of tiers information.
    """

    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = Field(default=None)
    max_tiers: Optional[int] = Field(default=None, alias="maxTiers")
    tiers: Optional[List[CollectionTier]] = Field(default=None)


class CollectionTier(BaseModel):
    """
    Information about a collection item tier.

    Attributes:
        tier: What tier it is.
        amount_required: The collected amount required for the tier.
        unlocks: A list of what the tier unlocks once reached.
    """

    model_config = ConfigDict(populate_by_name=True)
    tier: Optional[int] = Field(default=None)
    amount_required: Optional[int] = Field(default=None, alias="amountRequired")
    unlocks: Optional[List[str]] = Field(default=None)
