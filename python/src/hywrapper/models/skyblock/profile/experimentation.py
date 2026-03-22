from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Experimentation(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    simon: Optional[ExperimentationGame] = None
    pairings: Optional[ExperimentationGame] = None
    numbers: Optional[ExperimentationGame] = None
    claims_reset: Optional[int] = Field(default=None, alias="claims_resets")
    claims_resets_timestamp: Optional[int] = Field(default=None, alias="claims_resets_timestamp")
    serums_drank: Optional[int] = Field(default=None, alias="serums_drank")
    claimed_retroactive_rng: Optional[bool] = Field(default=None, alias="claimed_retroactive_rng")
    charge_track_timestamp: Optional[int] = Field(default=None, alias="charge_track_timestamp")


class ExperimentationGame(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    last_attempt: Optional[int] = Field(default=None, alias="last_attempt")
    last_claimed: Optional[int] = Field(default=None, alias="last_claimed")
    bonus_clicks: Optional[int] = Field(default=None, alias="bonus_clicks")
    claimed: Optional[bool] = None

    # Tier 0
    attempts0: Optional[int] = Field(default=None, alias="attempts_0")
    claims0: Optional[int] = Field(default=None, alias="claims_0")
    best_score0: Optional[int] = Field(default=None, alias="best_score_0")

    # Tier 1
    attempts1: Optional[int] = Field(default=None, alias="attempts_1")
    claims1: Optional[int] = Field(default=None, alias="claims_1")
    best_score1: Optional[int] = Field(default=None, alias="best_score_1")

    # Tier 2
    attempts2: Optional[int] = Field(default=None, alias="attempts_2")
    claims2: Optional[int] = Field(default=None, alias="claims_2")
    best_score2: Optional[int] = Field(default=None, alias="best_score_2")

    # Tier 3
    attempts3: Optional[int] = Field(default=None, alias="attempts_3")
    claims3: Optional[int] = Field(default=None, alias="claims_3")
    best_score3: Optional[int] = Field(default=None, alias="best_score_3")

    # Tier 4
    attempts4: Optional[int] = Field(default=None, alias="attempts_4")
    claims4: Optional[int] = Field(default=None, alias="claims_4")
    best_score4: Optional[int] = Field(default=None, alias="best_score_4")

    # Tier 5
    attempts5: Optional[int] = Field(default=None, alias="attempts_5")
    claims5: Optional[int] = Field(default=None, alias="claims_5")
    best_score5: Optional[int] = Field(default=None, alias="best_score_5")
