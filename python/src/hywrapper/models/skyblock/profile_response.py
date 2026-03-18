from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit
from hywrapper.models.skyblock.news_response import NewsItem
from hywrapper.models.skyblock.profile.rift import Rift


class ProfileResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    items: List[NewsItem] = Field(default=[])
    rateLimit: Optional[RateLimit] = None


class Profile(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    profileId: str = Field(default="")
    communityUpgrades: Optional[CommunityUpgrades] = None
    members: Dict[str, MemberData] = Field(default={})
    banking: Optional[Banking] = None


class MemberData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rift: Optional[Rift] = None


class CommunityUpgrades(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    currentlyUpgrading: str = Field(default="")
    upgradeStates: List[UpgradeState] = Field(default=[])


class UpgradeState(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    upgrade: str = Field(default="")
    tier: int = Field(default=1)
    startedMs: int = Field(default=0)
    startedBy: str = Field(default="")
    claimedBy: str = Field(default="")


class Banking(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    balance: float = Field(default=0.0)
    transactions: List[Transaction] = Field(default=[])


class Transaction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    amount: float = Field(default=0.0)
    timestamp: int = Field(default=0)
    action: str = Field(default="")
    initiatorName: str = Field(default="")
