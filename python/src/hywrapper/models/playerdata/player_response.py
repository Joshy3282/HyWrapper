from __future__ import annotations

from typing import Any, Dict, List, Optional, Type, TypeVar

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.playerdata.housing_setting import HousingSetting
from hywrapper.models.hypixel_response import HypixelResponse

T = TypeVar("T")


class HousingMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tutorial_step: Optional[str] = Field(default=None, alias="tutorialStep")
    packages: Optional[List[str]] = Field(default=None)
    plot_size: Optional[str] = Field(default=None, alias="plotSize")
    allowed_blocks: Optional[List[str]] = Field(default=None, alias="allowedBlocks")
    player_settings: Optional[Dict[str, str]] = Field(default=None, alias="playerSettings")
    selected_channels_v3: Optional[List[str]] = Field(default=None, alias="selectedChannels_v3")

    def get_housing_setting(self, setting: HousingSetting) -> Optional[T]:
        if not self.player_settings:
            return None

        raw = self.player_settings.get(setting.name)
        if not raw:
            return None

        # Value is usually "SettingName-Value"
        if "-" not in raw:
            value_str = raw
        else:
            value_str = raw.split("-", 1)[1]

        target_type = setting.type
        if target_type is bool:
            parsed: Any = value_str.lower() == "true"
        elif target_type is int:
            try:
                parsed = int(value_str)
            except ValueError:
                parsed = value_str
        else:
            parsed = value_str

        return parsed  # type: ignore


class Eugene(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    daily_two_k_exp: Optional[int] = Field(default=None, alias="dailyTwoKExp")


class VanityMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    packages: Optional[List[str]] = Field(default=None)


class Leveling(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    claimed_rewards: Optional[List[int]] = Field(default=None, alias="claimedRewards")


class QuestSettings(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    auto_activate: Optional[bool] = Field(default=None, alias="autoActivate")


class Tourney(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    first_join_lobby: Optional[int] = Field(default=None, alias="first_join_lobby")


class GiftedMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    ranks_given: Optional[int] = Field(default=None, alias="ranksGiven")
    rank_gifting_milestones: Optional[List[str]] = Field(
        default=None, alias="rankgiftingmilestones"
    )


class AchievementSync(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    quake_tiered: Optional[int] = Field(default=None, alias="quake_tiered")


class Player(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = Field(default=None, alias="_id")
    uuid: Optional[str] = None
    displayname: Optional[str] = None
    first_login: Optional[int] = Field(default=None, alias="firstLogin")
    playername: Optional[str] = None
    achievements_one_time: Optional[List[str]] = Field(default=None, alias="achievementsOneTime")
    achievement_points: Optional[int] = Field(default=None, alias="achievementPoints")
    housing_meta: Optional[HousingMeta] = Field(default=None, alias="housingMeta")
    achievement_tracking: Optional[List[str]] = Field(default=None, alias="achievementTracking")
    new_package_rank: Optional[str] = Field(default=None, alias="newPackageRank")
    network_exp: Optional[int] = Field(default=None, alias="networkExp")
    eugene: Optional[Eugene] = None
    channel: Optional[str] = None
    last_adsense_generate_time: Optional[int] = Field(default=None, alias="lastAdsenseGenerateTime")
    last_claimed_reward: Optional[int] = Field(default=None, alias="lastClaimedReward")
    reward_high_score: Optional[int] = Field(default=None, alias="rewardHighScore")
    reward_streak: Optional[int] = Field(default=None, alias="rewardStreak")
    total_daily_rewards: Optional[int] = Field(default=None, alias="totalDailyRewards")
    total_rewards: Optional[int] = Field(default=None, alias="totalRewrads")
    karma: Optional[int] = Field(default=None, alias="karma")
    monthly_package_rank: Optional[str] = Field(default=None, alias="monthlyPackageRank")
    most_recent_monthly_package_rank: Optional[str] = Field(
        default=None, alias="mostRecentMonthlyPackageRank"
    )
    vanity_meta: Optional[VanityMeta] = Field(default=None, alias="vanityMeta")
    leveling: Optional[Leveling] = None
    rank_plus_color: Optional[str] = Field(default=None, alias="rankPlusColor")
    quest_settings: Optional[QuestSettings] = Field(default=None, alias="questSettings")
    tourney: Optional[Tourney] = None
    fortune_buff: Optional[int] = Field(default=None, alias="fortuneBuff")
    gifted_meta: Optional[GiftedMeta] = Field(default=None, alias="giftedMeta")
    achievement_rewards_new: Optional[Dict[str, int]] = Field(
        default=None, alias="achievementRewardsNew"
    )
    main_2017_tutorial: Optional[bool] = Field(default=None, alias="main2017Tutorial")
    current_gadget: Optional[str] = Field(default=None, alias="currentGadget")
    achievement_sync: Optional[AchievementSync] = Field(default=None, alias="achievementSync")
    monthly_rank_color: Optional[str] = Field(default=None, alias="monthylRankColor")
    adsense_tokens: Optional[int] = Field(default=None, alias="adsense_tokens")


class PlayerResponse(HypixelResponse):
    player: Optional[Player] = None
