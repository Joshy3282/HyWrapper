from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class AlchemistQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    alchemist_quest_start: Optional[bool] = Field(default=None, alias="alchemist_quest_start")
    alchemist_quest_progress: int = Field(default=0, alias="alchemist_quest_progress")


class QuestRewards(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    wither_soul: Optional[int] = Field(default=None, alias="WITHER_SOUL")
    bezos: Optional[int] = Field(default=None, alias="BEZOS")
    flaming_heart: Optional[int] = Field(default=None, alias="FLAMING_HEART")
    corrupted_fragment: Optional[int] = Field(default=None, alias="CORRUPTED_FRAGMENT")
    lumino_fiber: Optional[int] = Field(default=None, alias="LUMINO_FIBER")
    crimson_isle_dojo_test_of_mob_kb_drating_c: Optional[str] = Field(
        default=None, alias="crimson_isle_dojo_test_of_mob_kb_drating_c"
    )
    crimson_isle_fetch_tentacle_meat_c: Optional[str] = Field(
        default=None, alias="crimson_isle_fetch_tentacle_meat_c"
    )
    crimson_isle_soulfish_b: Optional[str] = Field(default=None, alias="crimson_isle_soulfish_b")
    crimson_isle_kill_ashfang_a: Optional[str] = Field(
        default=None, alias="crimson_isle_kill_ashfang_a"
    )
    crimson_isle_rescue_s: Optional[str] = Field(default=None, alias="crimson_isle_rescue_s")


class QuestDataData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: str = Field(default="")
    progress: int = Field(default=0)
    completed_at: int = Field(default=0, alias="completed_at")


class QuestData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    quest_list: List[str] = Field(default_factory=list, alias="quest_list")
    quests: List[QuestDataData] = Field(default_factory=list)


class Quests(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    quest_data: Optional[QuestData] = Field(default=None, alias="quest_data")
    quest_rewards: Optional[QuestRewards] = Field(default=None, alias="quest_rewards")
    alchemist_quest: Optional[AlchemistQuest] = Field(default=None, alias="alchemist_quest")


class CrimsonIslePlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    quests: Optional[Quests] = None
