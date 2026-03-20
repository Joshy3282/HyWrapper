from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class InventoryData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: int = 0
    data: str = ""


class Inventory(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    inv_contents: Optional[InventoryData] = Field(default=None, alias="inv_contents")
    inv_armor: Optional[InventoryData] = Field(default=None, alias="inv_armor")
    ender_chest_contents: Optional[InventoryData] = Field(
        default=None, alias="ender_chest_contents"
    )
    # TODO all null?
    ender_chest_page_icons: List[InventoryData] = Field(
        default_factory=list, alias="ender_chest_page_icons"
    )
    equipment_contents: Optional[InventoryData] = Field(default=None, alias="equipment_contents")


class Dreadfarm(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    shania_stage: int = Field(default=0, alias="shania_stage")
    caducous_feeder_uses: List[int] = Field(default_factory=list, alias="caducous_feeder_uses")


class Access(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    last_free: int = Field(default=0, alias="last_free")
    consumed_prism: Optional[bool] = Field(default=None, alias="consumed_prism")
    charge_track_timestamp: int = Field(default=0, alias="charge_track_timestamp")


class Castle(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    unlocked_pathway_skip: Optional[bool] = Field(default=None, alias="unlocked_pathway_skip")
    fairy_step: int = Field(default=0, alias="fairy_step")
    grubber_stacks: int = Field(default=0, alias="grubber_stacks")


class WyldWoods(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    sirius_started_q_a: Optional[bool] = Field(default=None, alias="sirius_started_q_a")
    sirius_q_a_chain_done: Optional[bool] = Field(default=None, alias="sirius_q_a_chain_done")
    sirius_completed_q_a: Optional[bool] = Field(default=None, alias="sirius_completed_q_a")
    sirius_claimed_doubloon: Optional[bool] = Field(default=None, alias="sirius_claimed_doubloon")
    # TODO enum?
    talked_three_brothers: List[str] = Field(default_factory=list, alias="talked_threebrothers")
    bughunter_step: int = Field(default=0, alias="bughunter_step")


class KatHouse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bin_collected_silverfish: int = Field(default=0, alias="bin_collected_silverfish")
    bin_collected_spider: int = Field(default=0, alias="bin_collected_spider")
    bin_collected_mosquito: int = Field(default=0, alias="bin_collected_mosquito")


class Mirrorverse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    visited_rooms: List[str] = Field(default_factory=list, alias="visited_rooms")
    upside_down_hard: Optional[bool] = Field(default=None, alias="upside_down_hard")
    # TODO item enum
    claimed_chest_items: List[str] = Field(default_factory=list, alias="claimed_chest_items")
    claimed_reward: Optional[bool] = Field(default=None, alias="claimed_reward")


class CrazyKloon(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    selected_colors: Dict[str, str] = Field(default_factory=dict, alias="selected_colors")
    talked: Optional[bool] = None
    # TODO enum??? its just numbers
    hacked_terminals: List[str] = Field(default_factory=list, alias="hacked_terminals")
    quest_complete: Optional[bool] = Field(default=None, alias="quest_complete")


class Glyph(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    claimed_wand: Optional[bool] = Field(default=None, alias="claimed_wand")
    current_glyph_delivered: Optional[bool] = Field(default=None, alias="current_glyph_delivered")
    current_glyph_completed: Optional[bool] = Field(default=None, alias="current_glyph_completed")
    current_glyph: int = Field(default=0, alias="current_glyph")
    completed: Optional[bool] = None
    claimed_bracelet: Optional[bool] = Field(default=None, alias="claimed_bracelet")


class WestVillage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    crazy_kloon: Optional[CrazyKloon] = Field(default=None, alias="crazy_kloon")
    mirrorverse: Optional[Mirrorverse] = None
    kat_house: Optional[KatHouse] = Field(default=None, alias="kat_house")
    glyph: Optional[Glyph] = None


class RecentMobKill(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    xp: float = 0.0
    timestamp: int = 0


class SlayerQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = ""
    tier: int = 0
    start_timestamp: int = Field(default=0, alias="start_timestamp")
    completion_state: int = Field(default=0, alias="completion_state")
    used_armor: Optional[bool] = Field(default=None, alias="used_armor")
    solo: Optional[bool] = None
    combat_xp: int = Field(default=0, alias="combat_xp")
    recent_mob_kills: List[RecentMobKill] = Field(default_factory=list, alias="recent_mob_kills")
    last_killed_mob_island: str = Field(default="", alias="last_killed_mob_island")
    spawn_timestamp: int = Field(default=0, alias="spawn_timestamp")


class SecuredTrophy(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = ""
    timestamp: int = 0
    visits: int = 0


class Gallery(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    elise_step: int = Field(default=0, alias="elise_step")
    secured_trophies: List[SecuredTrophy] = Field(default_factory=list, alias="secured_trophies")
    # TODO enum maybe? not too helpful
    sent_trophy_dialogues: List[str] = Field(default_factory=list, alias="sent_trophy_dialogues")


class Enigma(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bought_cloak: Optional[bool] = Field(default=None, alias="bought_cloak")
    # TODO enum
    found_souls: List[str] = Field(default_factory=list, alias="found_souls")
    claimed_bonus_index: int = Field(default=0, alias="claimed_bonus_index")


class WizardTower(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    wizard_quest_step: int = Field(default=0, alias="wizard_quest_step")
    crumbs_laid_out: int = Field(default=0, alias="crumbs_laid_out")


class Montezuma(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO says null so what is this
    uuid: Optional[str] = None
    unique_id: str = Field(default="", alias="uniqueId")
    type: str = ""
    exp: float = 0.0
    active: Optional[bool] = None
    tier: str = ""
    # TODO same as uuid
    held_item: Optional[str] = Field(default=None, alias="heldItem")
    # TODO
    candy_used: int = Field(default=0, alias="candyUsed")
    pet_soulbound: Optional[bool] = Field(default=None, alias="petSoulbound")
    # TODO
    skin: Optional[str] = None
    # TODO
    extra: Optional[str] = None


class DeadCats(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    talked_to_jacquelle: Optional[bool] = Field(default=None, alias="talked_to_jacquelle")
    picked_up_detector: Optional[bool] = Field(default=None, alias="picked_up_detector")
    found_cats: List[str] = Field(default_factory=list, alias="found_cats")
    unlocked_pet: Optional[bool] = Field(default=None, alias="unlocked_pet")
    montezuma: Optional[Montezuma] = None


class BlackLagoon(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    talked_to_edwin: Optional[bool] = Field(default=None, alias="talked_to_edwin")
    received_science_paper: Optional[bool] = Field(default=None, alias="received_science_paper")
    completed_step: int = Field(default=0, alias="completed_step")
    delivered_science_paper: Optional[bool] = Field(default=None, alias="delivered_science_paper")


class WitherCage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    killed_eyes: List[str] = Field(default_factory=list, alias="killed_eyes")


class Seraphine(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    step_index: int = Field(default=0, alias="step_index")


class Lonely(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    seconds_sitting: int = Field(default=0, alias="seconds_sitting")


class Cowboy(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    stage: int = 0
    hay_eaten: int = Field(default=0, alias="hay_eaten")
    rabbit_name: str = Field(default="", alias="rabbit_name")
    exported_carrots: int = Field(default=0, alias="exported_carrots")


class BarryCenter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    first_talk_to_barry: Optional[bool] = Field(default=None, alias="first_talk_to_barry")
    convinced: List[str] = Field(default_factory=list)
    received_reward: Optional[bool] = Field(default=None, alias="received_reward")


class Murder(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    step_index: int = Field(default=0, alias="step_index")
    room_clues: List[str] = Field(default_factory=list, alias="room_clues")
    step_index_pt2: int = Field(default=0, alias="step_index_pt2")
    step_index_pt3: int = Field(default=0, alias="step_index_pt3")


class VillagePlaza(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    murder: Optional[Murder] = None
    barry_center: Optional[BarryCenter] = Field(default=None, alias="barryCenter")
    cowboy: Optional[Cowboy] = None
    # TODO barter_bank ??
    lonely: Optional[Lonely] = None
    seraphine: Optional[Seraphine] = None
    got_scammed: Optional[bool] = Field(default=None, alias="got_scammed")


class Rift(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    village_plaza: Optional[VillagePlaza] = Field(default=None, alias="village_plaza")
    wither_cage: Optional[WitherCage] = Field(default=None, alias="wither_cage")
    black_lagoon: Optional[BlackLagoon] = Field(default=None, alias="black_lagoon")
    dead_cats: Optional[DeadCats] = Field(default=None, alias="dead_cats")
    wizard_tower: Optional[WizardTower] = Field(default=None, alias="wizard_tower")
    enigma: Optional[Enigma] = None
    slayer_quest: Optional[SlayerQuest] = Field(default=None, alias="slayer_quest")
    # TODO enum?
    lifetime_purchased_boundaries: List[str] = Field(
        default_factory=list, alias="lifetime_purchased_boundaries"
    )
    west_village: Optional[WestVillage] = Field(default=None, alias="west_village")
    wyld_woods: Optional[WyldWoods] = Field(default=None, alias="wyld_woods")
    castle: Optional[Castle] = None
    access: Optional[Access] = None
    dreadfarm: Optional[Dreadfarm] = None
    inventory: Optional[Inventory] = None
