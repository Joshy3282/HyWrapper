from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class InventoryData(BaseModel):
    """
    Used for inventory data

    :param type: TODO unknown
    :param data: Base64 encoded Gzipped inventory nbt data.
    """

    model_config = ConfigDict(populate_by_name=True)
    type: Optional[int] = None
    data: Optional[str] = None


class Inventory(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    inv_contents: Optional[InventoryData] = Field(default=None, alias="inv_contents")
    inv_armor: Optional[InventoryData] = Field(default=None, alias="inv_armor")
    ender_chest_contents: Optional[InventoryData] = Field(
        default=None, alias="ender_chest_contents"
    )
    ender_chest_page_icons: Optional[List[Optional[InventoryData]]] = Field(
        default=None, alias="ender_chest_page_icons"
    )
    equipment_contents: Optional[InventoryData] = Field(default=None, alias="equipment_contents")


class Dreadfarm(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    shania_stage: Optional[int] = Field(default=None, alias="shania_stage")
    caducous_feeder_uses: Optional[List[int]] = Field(default=None, alias="caducous_feeder_uses")


class Access(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    last_free: Optional[int] = Field(default=None, alias="last_free")
    consumed_prism: Optional[bool] = Field(default=None, alias="consumed_prism")
    charge_track_timestamp: Optional[int] = Field(default=None, alias="charge_track_timestamp")


class Castle(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    unlocked_pathway_skip: Optional[bool] = Field(default=None, alias="unlocked_pathway_skip")
    fairy_step: Optional[int] = Field(default=None, alias="fairy_step")
    grubber_stacks: Optional[int] = Field(default=None, alias="grubber_stacks")


class WyldWoods(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    sirius_started_q_a: Optional[bool] = Field(default=None, alias="sirius_started_q_a")
    sirius_q_a_chain_done: Optional[bool] = Field(default=None, alias="sirius_q_a_chain_done")
    sirius_completed_q_a: Optional[bool] = Field(default=None, alias="sirius_completed_q_a")
    sirius_claimed_doubloon: Optional[bool] = Field(default=None, alias="sirius_claimed_doubloon")
    # TODO enum?
    talked_three_brothers: Optional[List[str]] = Field(default=None, alias="talked_threebrothers")
    bughunter_step: Optional[int] = Field(default=None, alias="bughunter_step")


class KatHouse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bin_collected_silverfish: Optional[int] = Field(default=None, alias="bin_collected_silverfish")
    bin_collected_spider: Optional[int] = Field(default=None, alias="bin_collected_spider")
    bin_collected_mosquito: Optional[int] = Field(default=None, alias="bin_collected_mosquito")


class Mirrorverse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    visited_rooms: Optional[List[str]] = Field(default=None, alias="visited_rooms")
    upside_down_hard: Optional[bool] = Field(default=None, alias="upside_down_hard")
    # TODO item enum
    claimed_chest_items: Optional[List[str]] = Field(default=None, alias="claimed_chest_items")
    claimed_reward: Optional[bool] = Field(default=None, alias="claimed_reward")


class CrazyKloon(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    selected_colors: Optional[Dict[str, str]] = Field(default=None, alias="selected_colors")
    talked: Optional[bool] = None
    # TODO enum??? its just numbers
    hacked_terminals: Optional[List[str]] = Field(default=None, alias="hacked_terminals")
    quest_complete: Optional[bool] = Field(default=None, alias="quest_complete")


class Glyph(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    claimed_wand: Optional[bool] = Field(default=None, alias="claimed_wand")
    current_glyph_delivered: Optional[bool] = Field(default=None, alias="current_glyph_delivered")
    current_glyph_completed: Optional[bool] = Field(default=None, alias="current_glyph_completed")
    current_glyph: Optional[int] = Field(default=None, alias="current_glyph")
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
    xp: Optional[float] = None
    timestamp: Optional[int] = None


class SlayerQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None
    tier: Optional[int] = None
    start_timestamp: Optional[int] = Field(default=None, alias="start_timestamp")
    completion_state: Optional[int] = Field(default=None, alias="completion_state")
    used_armor: Optional[bool] = Field(default=None, alias="used_armor")
    solo: Optional[bool] = None
    combat_xp: Optional[int] = Field(default=None, alias="combat_xp")
    recent_mob_kills: Optional[List[RecentMobKill]] = Field(default=None, alias="recent_mob_kills")
    last_killed_mob_island: Optional[str] = Field(default=None, alias="last_killed_mob_island")
    spawn_timestamp: Optional[int] = Field(default=None, alias="spawn_timestamp")


class SecuredTrophy(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None
    timestamp: Optional[int] = None
    visits: Optional[int] = None


class Gallery(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    elise_step: Optional[int] = Field(default=None, alias="elise_step")
    secured_trophies: Optional[List[SecuredTrophy]] = Field(default=None, alias="secured_trophies")
    # TODO enum maybe? not too helpful
    sent_trophy_dialogues: Optional[List[str]] = Field(default=None, alias="sent_trophy_dialogues")


class Enigma(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bought_cloak: Optional[bool] = Field(default=None, alias="bought_cloak")
    # TODO enum
    found_souls: Optional[List[str]] = Field(default=None, alias="found_souls")
    claimed_bonus_index: Optional[int] = Field(default=None, alias="claimed_bonus_index")


class WizardTower(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    wizard_quest_step: Optional[int] = Field(default=None, alias="wizard_quest_step")
    crumbs_laid_out: Optional[int] = Field(default=None, alias="crumbs_laid_out")


class Montezuma(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: Optional[str] = None
    unique_id: Optional[str] = Field(default=None, alias="uniqueId")
    type: Optional[str] = None
    exp: Optional[float] = None
    active: Optional[bool] = None
    tier: Optional[str] = None
    held_item: Optional[str] = Field(default=None, alias="held_item")
    candy_used: Optional[int] = Field(default=None, alias="candy_used")
    pet_soulbound: Optional[bool] = Field(default=None, alias="pet_soulbound")
    skin: Optional[str] = None
    extra: Optional[Dict[str, Any]] = None


class DeadCats(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    talked_to_jacquelle: Optional[bool] = Field(default=None, alias="talked_to_jacquelle")
    picked_up_detector: Optional[bool] = Field(default=None, alias="picked_up_detector")
    found_cats: Optional[List[str]] = Field(default=None, alias="found_cats")
    unlocked_pet: Optional[bool] = Field(default=None, alias="unlocked_pet")
    montezuma: Optional[Montezuma] = None


class BlackLagoon(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    talked_to_edwin: Optional[bool] = Field(default=None, alias="talked_to_edwin")
    received_science_paper: Optional[bool] = Field(default=None, alias="received_science_paper")
    completed_step: Optional[int] = Field(default=None, alias="completed_step")
    delivered_science_paper: Optional[bool] = Field(default=None, alias="delivered_science_paper")


class WitherCage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    killed_eyes: Optional[List[str]] = Field(default=None, alias="killed_eyes")


class Seraphine(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    step_index: Optional[int] = Field(default=None, alias="step_index")


class Lonely(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    seconds_sitting: Optional[int] = Field(default=None, alias="seconds_sitting")


class Cowboy(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    stage: Optional[int] = None
    hay_eaten: Optional[int] = Field(default=None, alias="hay_eaten")
    rabbit_name: Optional[str] = Field(default=None, alias="rabbit_name")
    exported_carrots: Optional[int] = Field(default=None, alias="exported_carrots")


class BarryCenter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    first_talk_to_barry: Optional[bool] = Field(default=None, alias="first_talk_to_barry")
    convinced: Optional[List[str]] = Field(default=None)
    received_reward: Optional[bool] = Field(default=None, alias="received_reward")


class Murder(BaseModel):
    """
    Information

    """

    model_config = ConfigDict(populate_by_name=True)
    step_index: Optional[int] = Field(default=None, alias="step_index")
    room_clues: Optional[List[str]] = Field(default=None, alias="room_clues")
    step_index_pt2: Optional[int] = Field(default=None, alias="step_index_pt2")
    step_index_pt3: Optional[int] = Field(default=None, alias="step_index_pt3")


class VillagePlaza(BaseModel):
    """
    Information related to the Village Plaza

    :param murder: Detective Amog's murder quest
    """

    model_config = ConfigDict(populate_by_name=True)
    murder: Optional[Murder] = None
    barry_center: Optional[BarryCenter] = Field(default=None, alias="barryCenter")
    cowboy: Optional[Cowboy] = None
    barter_bank: Optional[Dict[str, Any]] = Field(default=None, alias="barter_bank")
    lonely: Optional[Lonely] = None
    seraphine: Optional[Seraphine] = None
    got_scammed: Optional[bool] = Field(default=None, alias="got_scammed")


class Rift(BaseModel):
    """
    Information about a player's Rift data.

    :param village_plaza: Information related to the Village Plaza
    """

    model_config = ConfigDict(populate_by_name=True)
    village_plaza: Optional[VillagePlaza] = Field(default=None, alias="village_plaza")
    wither_cage: Optional[WitherCage] = Field(default=None, alias="wither_cage")
    black_lagoon: Optional[BlackLagoon] = Field(default=None, alias="black_lagoon")
    dead_cats: Optional[DeadCats] = Field(default=None, alias="dead_cats")
    wizard_tower: Optional[WizardTower] = Field(default=None, alias="wizard_tower")
    enigma: Optional[Enigma] = None
    gallery: Optional[Gallery] = None
    slayer_quest: Optional[SlayerQuest] = Field(default=None, alias="slayer_quest")
    # TODO enum?
    lifetime_purchased_boundaries: Optional[List[str]] = Field(
        default=None, alias="lifetime_purchased_boundaries"
    )
    west_village: Optional[WestVillage] = Field(default=None, alias="west_village")
    wyld_woods: Optional[WyldWoods] = Field(default=None, alias="wyld_woods")
    castle: Optional[Castle] = None
    access: Optional[Access] = None
    dreadfarm: Optional[Dreadfarm] = None
    inventory: Optional[Inventory] = None
