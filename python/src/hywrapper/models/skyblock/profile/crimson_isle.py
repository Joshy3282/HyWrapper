from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class GroupBuilder(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tier: Optional[str] = Field(default=None)
    note: Optional[str] = Field(default=None)
    combat_level_required: Optional[int] = Field(default=None, alias="combat_level_required")


class SearchSettings(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tier: Optional[str] = Field(default=None)


class KuudraPartyFinder(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    search_settings: Optional[SearchSettings] = Field(default=None, alias="search_settings")
    group_builder: Optional[GroupBuilder] = Field(default=None, alias="group_builder")


class Matriarch(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    pearls_collected: Optional[int] = Field(default=None, alias="pearls_collected")
    last_attempt: Optional[int] = Field(default=None, alias="last_attempt")
    recent_refreshes: Optional[List[int]] = Field(default=None, alias="recent_refreshes")


class OperatorChip(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    repaired_index: Optional[int] = Field(default=None, alias="repaired_index")


class Abiphone(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    contact_data: Optional[Dict[str, Any]] = Field(default=None, alias="contact_data")
    games: Optional[Dict[str, Any]] = None
    operator_chip: Optional[OperatorChip] = Field(default=None, alias="operator_chip")
    active_contacts: Optional[List[str]] = Field(default=None, alias="active_contacts")
    trio_contact_addons: Optional[int] = Field(default=None, alias="trio_contact_addons")
    selected_sort: Optional[str] = Field(default=None, alias="selected_sort")
    has_used_sirius_personal_phone_number_item: Optional[bool] = Field(
        default=None, alias="has_used_sirius_personal_phone_number_item"
    )
    last_dye_called_year: Optional[int] = Field(default=None, alias="last_dye_called_year")


class SirihQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    sulphur_given: Optional[int] = Field(default=None, alias="sulphur_given")
    last_give: Optional[int] = Field(default=None, alias="last_give")


class DuelTrainingQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    duel_training_phase_barbarians: Optional[int] = Field(
        default=None, alias="duel_training_phase_barbarians"
    )
    duel_training_last_complete_barbarians: Optional[int] = Field(
        default=None, alias="duel_training_last_complete_barbarians"
    )


class PabloQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    pablo_active: Optional[bool] = Field(default=None, alias="pablo_active")
    pablo_item: Optional[str] = Field(default=None, alias="pablo_item")


class SuusQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    talked_to_npc: Optional[bool] = Field(default=None, alias="talked_to_npc")
    last_toy_drop: Optional[int] = Field(default=None, alias="last_toy_drop")
    last_completion: Optional[int] = Field(default=None, alias="last_completion")


class PomtairQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    talked_to_npc: Optional[bool] = Field(default=None, alias="talked_to_npc")


class ChickenQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    chicken_quest_progress: Optional[int] = Field(default=None, alias="chicken_quest_progress")
    chicken_quest_start: Optional[bool] = Field(default=None, alias="chicken_quest_start")
    chicken_quest_collected: Optional[List[Any]] = Field(
        default=None, alias="chicken_quest_collected"
    )


class AlchemistQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    alchemist_quest_start: Optional[bool] = Field(default=None, alias="alchemist_quest_start")
    alchemist_quest_progress: Optional[int] = Field(default=None, alias="alchemist_quest_progress")


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


class Quests(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    quest_data: Optional[Dict[str, Any]] = Field(default=None, alias="quest_data")
    miniboss_daily: Optional[Dict[str, Any]] = Field(default=None, alias="miniboss_daily")
    kuudra_boss_daily: Optional[Dict[str, Any]] = Field(default=None, alias="kuuda_boss_daily")
    quest_rewards: Optional[QuestRewards] = Field(default=None, alias="quest_rewards")
    alchemist_quest: Optional[AlchemistQuest] = Field(default=None, alias="alchemist_quest")
    rulenor: Optional[Dict[str, Any]] = None
    chicken_quest: Optional[ChickenQuest] = Field(default=None, alias="chicken_quest")
    pomtair_quest: Optional[PomtairQuest] = Field(default=None, alias="pomtair_quest")
    suus_quest: Optional[SuusQuest] = Field(default=None, alias="suus_quest")
    pablo_quest: Optional[PabloQuest] = Field(default=None, alias="pablo_quest")
    duel_training_quest: Optional[DuelTrainingQuest] = Field(
        default=None, alias="duel_training_quest"
    )
    sirih_quest: Optional[SirihQuest] = Field(default=None, alias="sirih_quest")
    edelis_quest: Optional[Dict[str, Any]] = Field(default=None, alias="edelis_quest")
    mollim_quest: Optional[Dict[str, Any]] = Field(default=None, alias="mollim_quest")
    aranya_quest: Optional[Dict[str, Any]] = Field(default=None, alias="aranya_quest")
    last_reset: Optional[int] = Field(default=None, alias="last_reset")
    paid_bruuh: Optional[bool] = Field(default=None, alias="paid_bruuh")
    miniboss_data: Optional[Dict[str, bool]] = Field(default=None, alias="miniboss_data")
    found_kuudra_book: Optional[bool] = Field(default=None, alias="found_kuudra_book")
    kuudra_loremaster: Optional[bool] = Field(default=None, alias="kuudra_loremaster")
    found_kuudra_chestplate: Optional[bool] = Field(default=None, alias="found_kuudra_chestplate")
    found_kuudra_boots: Optional[bool] = Field(default=None, alias="found_kuudra_boots")
    last_believer_blessing: Optional[int] = Field(default=None, alias="last_believer_blessing")
    fished_wet_napkin: Optional[bool] = Field(default=None, alias="fished_wet_napkin")
    weird_sailor: Optional[bool] = Field(default=None, alias="weird_sailor")
    found_kuudra_helmet: Optional[bool] = Field(default=None, alias="found_kuudra_helmet")
    found_kuudra_leggings: Optional[bool] = Field(default=None, alias="found_kuudra_leggings")
    last_kuudra_relic: Optional[int] = Field(default=None, alias="last_kuudra_relic")
    unlocked_cavity_npcs: Optional[List[str]] = Field(default=None, alias="unlocked_cavity_npcs")
    cavity_rarity: Optional[str] = Field(default=None, alias="cavity_rarity")


class CrimsonIslePlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    quests: Optional[Quests] = None
    kuudra_completed_tiers: Optional[Dict[str, int]] = Field(
        default=None, alias="kuudra_completed_tiers"
    )
    dojo: Optional[Dict[str, int]] = Field(default=None)
    abiphone: Optional[Abiphone] = None
    matriarch: Optional[Matriarch] = None
    barbarians_reputation: Optional[float] = Field(default=None, alias="barbarians_reputation")
    mages_reputation: Optional[float] = Field(default=None, alias="mages_reputation")
    selected_faction: Optional[str] = Field(default=None, alias="selected_faction")
    last_minibosses_killed: Optional[List[str]] = Field(
        default=None, alias="last_minibosses_killed"
    )
    kuudra_party_finder: Optional[KuudraPartyFinder] = Field(
        default=None, alias="kuudra_party_finder"
    )
    barbarians_reputation_highest: Optional[int] = Field(
        default=None, alias="barbarians_reputation_highest"
    )
