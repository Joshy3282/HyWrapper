from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Harp(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    claimed_talisman: Optional[bool] = Field(default=None, alias="claimed_talisman")
    selected_song: Optional[str] = Field(default=None, alias="selected_song")
    selected_song_epoch: Optional[int] = Field(default=None, alias="selected_song_epoch")

    # Joy to the World
    song_joy_world_completions: Optional[int] = Field(
        default=None, alias="song_joy_world_completions"
    )
    song_joy_world_perfect_completions: Optional[int] = Field(
        default=None, alias="song_joy_world_perfect_completions"
    )
    song_joy_world_best_completion: Optional[float] = Field(
        default=None, alias="song_joy_world_best_completion"
    )

    # Jeopardy
    song_jeopardy_completions: Optional[int] = Field(
        default=None, alias="song_jeopardy_completions"
    )
    song_jeopardy_perfect_completions: Optional[int] = Field(
        default=None, alias="song_jeopardy_perfect_completions"
    )
    song_jeopardy_best_completion: Optional[float] = Field(
        default=None, alias="song_jeopardy_best_completion"
    )

    # Pure Imagination
    song_pure_imagination_completions: Optional[int] = Field(
        default=None, alias="song_pure_imagination_completions"
    )
    song_pure_imagination_perfect_completions: Optional[int] = Field(
        default=None, alias="song_pure_imagination_perfect_completions"
    )
    song_pure_imagination_best_completion: Optional[float] = Field(
        default=None, alias="song_pure_imagination_best_completion"
    )

    # Through the Campfire (Fire and Flames)
    song_fire_and_flames_completions: Optional[int] = Field(
        default=None, alias="song_fire_and_flames_completions"
    )
    song_fire_and_flames_perfect_completions: Optional[int] = Field(
        default=None, alias="song_fire_and_flames_perfect_completions"
    )
    song_fire_and_flames_best_completion: Optional[float] = Field(
        default=None, alias="song_fire_and_flames_best_completion"
    )

    # Happy Birthday
    song_happy_birthday_completions: Optional[int] = Field(
        default=None, alias="song_happy_birthday_completions"
    )
    song_happy_birthday_perfect_completions: Optional[int] = Field(
        default=None, alias="song_happy_birthday_perfect_completions"
    )
    song_happy_birthday_best_completion: Optional[float] = Field(
        default=None, alias="song_happy_birthday_best_completion"
    )

    # Minuet
    song_minuet_completions: Optional[int] = Field(default=None, alias="song_minuet_completions")
    song_minuet_perfect_completions: Optional[int] = Field(
        default=None, alias="song_minuet_perfect_completions"
    )
    song_minuet_best_completion: Optional[float] = Field(
        default=None, alias="song_minuet_best_completion"
    )

    # Amazing Grace
    song_amazing_grace_completions: Optional[int] = Field(
        default=None, alias="song_amazing_grace_completions"
    )
    song_amazing_grace_perfect_completions: Optional[int] = Field(
        default=None, alias="song_amazing_grace_perfect_completions"
    )
    song_amazing_grace_best_completion: Optional[float] = Field(
        default=None, alias="song_amazing_grace_best_completion"
    )

    # Greensleeves
    song_greensleeves_completions: Optional[int] = Field(
        default=None, alias="song_greensleeves_completions"
    )
    song_greensleeves_perfect_completions: Optional[int] = Field(
        default=None, alias="song_greensleeves_perfect_completions"
    )
    song_greensleeves_best_completion: Optional[float] = Field(
        default=None, alias="song_greensleeves_best_completion"
    )

    # La Vie en Rose
    song_vie_en_rose_completions: Optional[int] = Field(
        default=None, alias="song_vie_en_rose_completions"
    )
    song_vie_en_rose_perfect_completions: Optional[int] = Field(
        default=None, alias="song_vie_en_rose_perfect_completions"
    )
    song_vie_en_rose_best_completion: Optional[float] = Field(
        default=None, alias="song_vie_en_rose_best_completion"
    )

    # Brahms' Lullaby
    song_brahms_completions: Optional[int] = Field(default=None, alias="song_brahms_completions")
    song_brahms_perfect_completions: Optional[int] = Field(
        default=None, alias="song_brahms_perfect_completions"
    )
    song_brahms_best_completion: Optional[float] = Field(
        default=None, alias="song_brahms_best_completion"
    )

    # Frere Jacques
    song_frere_jacques_completions: Optional[int] = Field(
        default=None, alias="song_frere_jacques_completions"
    )
    song_frere_jacques_perfect_completions: Optional[int] = Field(
        default=None, alias="song_frere_jacques_perfect_completions"
    )
    song_frere_jacques_best_completion: Optional[float] = Field(
        default=None, alias="song_frere_jacques_best_completion"
    )

    # Pachelbel
    song_pachelbel_completions: Optional[int] = Field(
        default=None, alias="song_pachelbel_completions"
    )
    song_pachelbel_perfect_completions: Optional[int] = Field(
        default=None, alias="song_pachelbel_perfect_completions"
    )
    song_pachelbel_best_completion: Optional[float] = Field(
        default=None, alias="song_pachelbel_best_completion"
    )

    # Ode to Joy
    song_hymn_joy_completions: Optional[int] = Field(
        default=None, alias="song_hymn_joy_completions"
    )
    song_hymn_joy_perfect_completions: Optional[int] = Field(
        default=None, alias="song_hymn_joy_perfect_completions"
    )
    song_hymn_joy_best_completion: Optional[float] = Field(
        default=None, alias="song_hymn_joy_best_completion"
    )


class Songs(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    harp: Optional[Harp] = None


class TreeGifts(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    fig: int = Field(default=0, alias="FIG")
    milestone_tier_claimed: Dict[str, int] = Field(
        default_factory=dict, alias="milestone_tier_claimed"
    )
    mangrove: int = Field(default=0, alias="MANGROVE")


class HinaTasks(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    completed_tasks: List[str] = Field(default_factory=list, alias="completed_tasks")
    # TODO enum
    task_progress: Dict[str, int] = Field(default_factory=dict, alias="task_progress")
    # TODO enum
    claimed_rewards: List[str] = Field(default_factory=list, alias="claimed_rewards")
    tier_claimed: int = Field(default=0, alias="tier_claimed")


class Hina(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tasks: Optional[HinaTasks] = None


class Starlyn(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    personal_bests: Dict[str, int] = Field(default_factory=dict, alias="personal_bests")


class Foraging(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    starlyn: Optional[Starlyn] = None
    # TODO enum
    fish_family: List[str] = Field(default_factory=list, alias="fish_family")
    hina: Optional[Hina] = None
    tree_gifts: Optional[TreeGifts] = Field(default=None, alias="tree_gifts")
    songs: Optional[Songs] = None
