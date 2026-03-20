from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class Pattern(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    pattern: str = Field(default="", alias="Pattern")
    color: str = Field(default="", alias="Color")


class Banner(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    base: str = Field(default="", alias="Base")
    patterns: List[Pattern] = Field(default_factory=list, alias="Patterns")


class Rank(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = ""
    default: Optional[bool] = None
    tag: Optional[str] = None
    created: int = 0
    priority: int = 0


class Member(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: str = ""
    rank: str = ""
    joined: int = 0
    quest_participation: int = Field(default=0, alias="questParticipation")
    muted_till: int = Field(default=0, alias="mutedTill")
    exp_history: Dict[str, int] = Field(default_factory=dict, alias="expHistory")


class Guild(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(default="", alias="_id")
    name: str = ""
    name_lower: str = Field(default="", alias="name_lower")
    coins: int = 0
    coins_ever: int = Field(default=0, alias="coinsEver")
    created: int = 0
    members: List[Member] = Field(default_factory=list)
    ranks: List[Rank] = Field(default_factory=list)
    achievements: Dict[str, int] = Field(default_factory=dict)
    exp: int = 0
    tag_color: str = Field(default="", alias="tagColor")
    banner: Optional[Banner] = None
    publicly_listed: Optional[bool] = Field(default=None, alias="publiclyListed")
    preferred_games: List[str] = Field(default_factory=list, alias="preferredGames")
    description: str = ""
    chat_mute: int = Field(default=0, alias="chatMute")
    tag: str = ""
    guild_exp_by_game_type: Dict[str, int] = Field(default_factory=dict, alias="guildExpByGameType")


class GuildResponse(HypixelResponse):
    guild: Optional[Guild] = None
