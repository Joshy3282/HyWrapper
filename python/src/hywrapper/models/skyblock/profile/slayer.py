from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field


class Slayer(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    slayerQuest: Optional[OngoingSlayerQuest] = Field(default=None, alias="slayer_quest")
    slayerBosses: Optional[Dict[str, SlayerData]] = Field(default=None, alias="slayer_bosses")


class OngoingSlayerQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None
    tier: Optional[int] = None
    startTimestamp: Optional[int] = Field(default=None, alias="start_timestamp")
    completionState: Optional[int] = Field(default=None, alias="completion_state")
    usedArmor: Optional[bool] = Field(default=None, alias="used_armor")
    solo: Optional[bool] = None


class SlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    claimedLevels: Optional[Dict[str, bool]] = Field(default_factory=dict, alias="claimed_levels")
    xp: Optional[int] = None
    bossKillsTier0: Optional[int] = Field(default=None, alias="boss_kills_tier_0")
    bossKillsTier1: Optional[int] = Field(default=None, alias="boss_kills_tier_1")
    bossKillsTier2: Optional[int] = Field(default=None, alias="boss_kills_tier_2")
    bossKillsTier3: Optional[int] = Field(default=None, alias="boss_kills_tier_3")
    bossKillsTier4: Optional[int] = Field(default=None, alias="boss_kills_tier_4")
    bossAttemptsTier0: Optional[int] = Field(default=None, alias="boss_attempts_tier_0")
    bossAttemptsTier1: Optional[int] = Field(default=None, alias="boss_attempts_tier_1")
    bossAttemptsTier2: Optional[int] = Field(default=None, alias="boss_attempts_tier_2")
    bossAttemptsTier3: Optional[int] = Field(default=None, alias="boss_attempts_tier_3")
    bossAttemptsTier4: Optional[int] = Field(default=None, alias="boss_attempts_tier_4")
