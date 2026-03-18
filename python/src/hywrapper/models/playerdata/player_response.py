from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class PlayerResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    player: Optional[Player] = None
    rateLimit: Optional[RateLimit] = None


class Player(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(default="")
    uuid: str = Field(default="")
    displayname: str = Field(default="")
    firstLogin: Optional[int] = Field(default=0)
    playername: str = Field(default="")
    achievementsOneTime: List[str] = Field(default=[])
    achievementPoints: Optional[int] = Field(default=0)
    housingMeta: Optional[HousingMeta] = None
    achievementTracking: List[str] = Field(default=[])
    newPackageRank: str = Field(default="")
    networkExp: Optional[int] = Field(default=0)
    eugene: Optional[Eugene] = None
    channel: str = Field(default="")
    lastAdsenseGenerateTime: Optional[int] = Field(default=0)
    lastClaimedReward: Optional[int] = Field(default=0)
    rewardHighScore: Optional[int] = Field(default=0)
    rewardStreak: Optional[int] = Field(default=0)
    totalDailyRewards: Optional[int] = Field(default=0)
    totalRewrads: Optional[int] = Field(default=0)
    karma: Optional[int] = Field(default=0)
    monthlyPackageRank: str = Field(default="")
    mostRecentMonthlyPackageRank: str = Field(default="")
    vanityMeta: Optional[VanityMeta] = None
    leveling: Optional[Leveling] = None
    rankPlusColor: str = Field(default="")
    questSettings: Optional[QuestSettings] = None
    tourney: Optional[Tourney] = None
    fortuneBuff: Optional[int] = Field(default=0)
    giftedMeta: Optional[GiftedMeta] = None
    achievementRewardsNew: Dict[str, int] = Field(default={})
    main2017Tutorial: Optional[bool] = None
    currentGadget: str = Field(default="")
    achievementSync: Optional[AchievementSync] = None
    monthylRankColor: str = Field(default="")
    adsenseTokens: int = Field(default=0)


class HousingMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tutorialStep: str = Field(default="")
    packages: List[str] = Field(default=[])
    plotSize: str = Field(default="")
    allowedBlocks: List[str] = Field(default=[])
    playerSettings: Dict[str, str] = Field(default={})
    selectedChannelsV3: List[str] = Field(default=[])


class Eugene(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    dailyTwoKExp: Optional[int] = Field(default=0)


class VanityMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    packages: List[str] = Field(default=[])


class Leveling(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    claimedRewards: List[int] = Field(default=[])


class QuestSettings(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    autoActivate: Optional[bool] = None


class Tourney(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    firstJoinLobby: Optional[int] = Field(default=0)


class GiftedMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    ranksGiven: Optional[int] = Field(default=0)
    rankgiftingmilestones: List[str] = Field(default=[])


class AchievementSync(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    quakeTiered: Optional[int] = Field(default=0)
