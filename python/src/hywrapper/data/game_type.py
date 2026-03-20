from __future__ import annotations

from enum import IntEnum
from typing import Any, Optional


class GameType(IntEnum):
    QUAKECRAFT = 2
    WALLS = 3
    PAINTBALL = 4
    SURVIVAL_GAMES = 5
    TNTGAMES = 6
    VAMPIREZ = 7
    WALLS3 = 13
    ARCADE = 14
    ARENA = 17
    UHC = 20
    MCGO = 21
    BATTLEGROUND = 23
    SUPER_SMASH = 24
    GINGERBREAD = 25
    HOUSING = 26
    SKYWARS = 51
    TRUE_COMBAT = 52
    SPEED_UHC = 54
    SKYCLASH = 55
    LEGACY = 56
    PROTOTYPE = 57
    BEDWARS = 58
    MURDER_MYSTERY = 59
    BUILD_BATTLE = 60
    DUELS = 61
    SKYBLOCK = 63
    PIT = 64
    REPLAY = 65
    SMP = 67
    WOOL_GAMES = 68

    @property
    def id(self) -> int:
        return _IDS[self]

    @property
    def database_name(self) -> str:
        return _DATABASE_NAMES[self]

    @property
    def clean_name(self) -> str:
        return _CLEAN_NAMES[self]

    @classmethod
    def from_id(cls, id: Any) -> Optional[GameType]:
        try:
            return cls(id)
        except ValueError:
            return None


_IDS = {
    GameType.QUAKECRAFT: 2,
    GameType.WALLS: 3,
    GameType.PAINTBALL: 4,
    GameType.SURVIVAL_GAMES: 5,
    GameType.TNTGAMES: 6,
    GameType.VAMPIREZ: 7,
    GameType.WALLS3: 13,
    GameType.ARCADE: 14,
    GameType.ARENA: 17,
    GameType.UHC: 20,
    GameType.MCGO: 21,
    GameType.BATTLEGROUND: 23,
    GameType.SUPER_SMASH: 24,
    GameType.GINGERBREAD: 25,
    GameType.HOUSING: 26,
    GameType.SKYWARS: 51,
    GameType.TRUE_COMBAT: 52,
    GameType.SPEED_UHC: 54,
    GameType.SKYCLASH: 55,
    GameType.LEGACY: 56,
    GameType.PROTOTYPE: 57,
    GameType.BEDWARS: 58,
    GameType.MURDER_MYSTERY: 59,
    GameType.BUILD_BATTLE: 60,
    GameType.DUELS: 61,
    GameType.SKYBLOCK: 63,
    GameType.PIT: 64,
    GameType.REPLAY: 65,
    GameType.SMP: 67,
    GameType.WOOL_GAMES: 68,
}

_DATABASE_NAMES = {
    GameType.QUAKECRAFT: "Quake",
    GameType.WALLS: "Walls",
    GameType.PAINTBALL: "Paintball",
    GameType.SURVIVAL_GAMES: "HungerGames",
    GameType.TNTGAMES: "TNTGames",
    GameType.VAMPIREZ: "VampireZ",
    GameType.WALLS3: "Walls3",
    GameType.ARCADE: "Arcade",
    GameType.ARENA: "Arena",
    GameType.UHC: "UHC",
    GameType.MCGO: "MCGO",
    GameType.BATTLEGROUND: "Battleground",
    GameType.SUPER_SMASH: "SuperSmash",
    GameType.GINGERBREAD: "GingerBread",
    GameType.HOUSING: "Housing",
    GameType.SKYWARS: "SkyWars",
    GameType.TRUE_COMBAT: "TrueCombat",
    GameType.SPEED_UHC: "SpeedUHC",
    GameType.SKYCLASH: "SkyClash",
    GameType.LEGACY: "Legacy",
    GameType.PROTOTYPE: "Prototype",
    GameType.BEDWARS: "Bedwars",
    GameType.MURDER_MYSTERY: "MurderMystery",
    GameType.BUILD_BATTLE: "BuildBattle",
    GameType.DUELS: "Duels",
    GameType.SKYBLOCK: "SkyBlock",
    GameType.PIT: "Pit",
    GameType.REPLAY: "Replay",
    GameType.SMP: "SMP",
    GameType.WOOL_GAMES: "WoolGames",
}

_CLEAN_NAMES = {
    GameType.QUAKECRAFT: "Quake",
    GameType.WALLS: "Walls",
    GameType.PAINTBALL: "Paintball",
    GameType.SURVIVAL_GAMES: "Blitz Survival Games",
    GameType.TNTGAMES: "TNT Games",
    GameType.VAMPIREZ: "VampireZ",
    GameType.WALLS3: "Mega Walls",
    GameType.ARCADE: "Arcade",
    GameType.ARENA: "Arena",
    GameType.UHC: "UHC Champions",
    GameType.MCGO: "Cops and Crims",
    GameType.BATTLEGROUND: "Warlords",
    GameType.SUPER_SMASH: "Smash Heroes",
    GameType.GINGERBREAD: "Turbo Kart Racers",
    GameType.HOUSING: "Housing",
    GameType.SKYWARS: "SkyWars",
    GameType.TRUE_COMBAT: "Crazy Walls",
    GameType.SPEED_UHC: "Speed UHC",
    GameType.SKYCLASH: "SkyClash",
    GameType.LEGACY: "Classic Games",
    GameType.PROTOTYPE: "Prototype",
    GameType.BEDWARS: "Bed Wars",
    GameType.MURDER_MYSTERY: "Murder Mystery",
    GameType.BUILD_BATTLE: "Build Battle",
    GameType.DUELS: "Duels",
    GameType.SKYBLOCK: "SkyBlock",
    GameType.PIT: "Pit",
    GameType.REPLAY: "Replay",
    GameType.SMP: "SMP",
    GameType.WOOL_GAMES: "Wool Wars",
}
