from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class HousingMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tutorial_step: str = Field(default="", alias="tutorialStep")
    packages: List[str] = Field(default_factory=list)
    plot_size: str = Field(default="", alias="plotSize")
    allowed_blocks: List[str] = Field(default_factory=list, alias="allowedBlocks")
    player_settings: Dict[str, str] = Field(default_factory=dict, alias="playerSettings")
    selected_channels_v3: List[str] = Field(default_factory=list, alias="selectedChannels_v3")


class Eugene(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    daily_two_k_exp: Optional[int] = Field(default=0, alias="dailyTwoKExp")


class VanityMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    packages: List[str] = Field(default_factory=list)


class Leveling(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    claimed_rewards: List[int] = Field(default_factory=list, alias="claimedRewards")


class QuestSettings(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    auto_activate: Optional[bool] = Field(default=None, alias="autoActivate")


class Tourney(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    first_join_lobby: Optional[int] = Field(default=0, alias="first_join_lobby")


class GiftedMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    ranks_given: Optional[int] = Field(default=0, alias="ranksGiven")
    rank_gifting_milestones: List[str] = Field(default_factory=list, alias="rankgiftingmilestones")


class AchievementSync(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    quake_tiered: Optional[int] = Field(default=0, alias="quake_tiered")


class Player(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(default="", alias="_id")
    uuid: str = ""
    displayname: str = ""
    first_login: Optional[int] = Field(default=0, alias="firstLogin")
    playername: str = ""
    achievements_one_time: List[str] = Field(default_factory=list, alias="achievementsOneTime")
    achievement_points: Optional[int] = Field(default=0, alias="achievementPoints")
    housing_meta: Optional[HousingMeta] = Field(default=None, alias="housingMeta")
    achievement_tracking: List[str] = Field(default_factory=list, alias="achievementTracking")
    new_package_rank: str = Field(default="", alias="newPackageRank")
    network_exp: Optional[int] = Field(default=0, alias="networkExp")
    eugene: Optional[Eugene] = None
    channel: str = ""
    last_adsense_generate_time: Optional[int] = Field(default=0, alias="lastAdsenseGenerateTime")
    last_claimed_reward: Optional[int] = Field(default=0, alias="lastClaimedReward")
    reward_high_score: Optional[int] = Field(default=0, alias="rewardHighScore")
    reward_streak: Optional[int] = Field(default=0, alias="rewardStreak")
    total_daily_rewards: Optional[int] = Field(default=0, alias="totalDailyRewards")
    total_rewards: Optional[int] = Field(default=0, alias="totalRewrads")
    karma: Optional[int] = Field(default=0, alias="karma")
    monthly_package_rank: str = Field(default="", alias="monthlyPackageRank")
    most_recent_monthly_package_rank: str = Field(default="", alias="mostRecentMonthlyPackageRank")
    vanity_meta: Optional[VanityMeta] = Field(default=None, alias="vanityMeta")
    leveling: Optional[Leveling] = None
    rank_plus_color: str = Field(default="", alias="rankPlusColor")
    quest_settings: Optional[QuestSettings] = Field(default=None, alias="questSettings")
    tourney: Optional[Tourney] = None
    fortune_buff: Optional[int] = Field(default=0, alias="fortuneBuff")
    gifted_meta: Optional[GiftedMeta] = Field(default=None, alias="giftedMeta")
    achievement_rewards_new: Dict[str, int] = Field(
        default_factory=dict, alias="achievementRewardsNew"
    )
    main_2017_tutorial: Optional[bool] = Field(default=None, alias="main2017Tutorial")
    current_gadget: str = Field(default="", alias="currentGadget")
    achievement_sync: Optional[AchievementSync] = Field(default=None, alias="achievementSync")
    monthly_rank_color: str = Field(default="", alias="monthylRankColor")
    adsense_tokens: int = Field(default=0, alias="adsense_tokens")


class PlayerResponse(HypixelResponse):
    player: Optional[Player] = None
