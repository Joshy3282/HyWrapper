from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class Pattern(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    pattern: Optional[str] = Field(default=None, alias="Pattern")
    color: Optional[str] = Field(default=None, alias="Color")


class Banner(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    base: Optional[str] = Field(default=None, alias="Base")
    patterns: Optional[List[Pattern]] = Field(default=None, alias="Patterns")


class Rank(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = None
    default: Optional[bool] = None
    tag: Optional[str] = None
    created: Optional[int] = None
    priority: Optional[int] = None


class Member(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: Optional[str] = None
    rank: Optional[str] = None
    joined: Optional[int] = None
    quest_participation: Optional[int] = Field(default=None, alias="questParticipation")
    muted_till: Optional[int] = Field(default=None, alias="mutedTill")
    exp_history: Optional[Dict[str, int]] = Field(default=None, alias="expHistory")


class Guild(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = Field(default=None, alias="_id")
    name: Optional[str] = None
    name_lower: Optional[str] = Field(default=None, alias="name_lower")
    coins: Optional[int] = None
    coins_ever: Optional[int] = Field(default=None, alias="coinsEver")
    created: Optional[int] = None
    members: Optional[List[Member]] = Field(default=None)
    ranks: Optional[List[Rank]] = Field(default=None)
    achievements: Optional[Dict[str, int]] = Field(default=None)
    exp: Optional[int] = None
    tag_color: Optional[str] = Field(default=None, alias="tagColor")
    banner: Optional[Banner] = None
    publicly_listed: Optional[bool] = Field(default=None, alias="publiclyListed")
    preferred_games: Optional[List[str]] = Field(default=None, alias="preferredGames")
    description: Optional[str] = None
    chat_mute: Optional[int] = Field(default=None, alias="chatMute")
    tag: Optional[str] = None
    guild_exp_by_game_type: Optional[Dict[str, int]] = Field(
        default=None, alias="guildExpByGameType"
    )


class GuildResponse(HypixelResponse):
    guild: Optional[Guild] = None
