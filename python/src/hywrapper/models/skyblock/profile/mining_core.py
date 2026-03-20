from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field


class MiningCore(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    receivedFreeTier: Optional[bool] = Field(default=None, alias="received_free_tier")
    tokens: Optional[int] = None
    powderMithril: Optional[int] = Field(default=None, alias="powder_mithril")
    powderMithrilTotal: Optional[int] = Field(default=None, alias="powder_mithril_total")
    powderSpentMithril: Optional[int] = Field(default=None, alias="powder_spent_mithril")
    retroactiveTier2Token: Optional[bool] = Field(default=None, alias="retroactive_tier2_token")
    dailyOresMinedDay: Optional[int] = Field(default=None, alias="daily_ores_mined_day")
    dailyOresMined: Optional[int] = Field(default=None, alias="daily_ores_mined")
    crystals: Optional[Dict[str, Crystal]] = None
    greaterMinesLastAccess: Optional[int] = Field(default=None, alias="greater_mines_last_access")
    biomes: Optional[Biomes] = None
    powderGemstone: Optional[int] = Field(default=None, alias="powder_gemstone")
    powderGemstoneTotal: Optional[int] = Field(default=None, alias="powder_gemstone_total")
    powderSpentGemstone: Optional[int] = Field(default=None, alias="powder_spent_gemstone")
    dailyOresMinedDayGemstone: Optional[int] = Field(
        default=None, alias="daily_ores_mined_day_gemstone"
    )
    dailyOresMinedGemstone: Optional[int] = Field(default=None, alias="daily_ores_mined_gemstone")
    dailyOresMinedDayMithrilOre: Optional[int] = Field(
        default=None, alias="daily_ores_mined_day_mithril_ore"
    )
    dailyOresMinedMithrilOre: Optional[int] = Field(
        default=None, alias="daily_ores_mined_mithril_ore"
    )
    dailyOresMinedDayGlacite: Optional[int] = Field(
        default=None, alias="daily_ores_mined_day_glacite"
    )
    dailyOresMinedGlacite: Optional[int] = Field(default=None, alias="daily_ores_mined_glacite")
    powderGlacite: Optional[int] = Field(default=None, alias="powder_glacite")
    powderGlaciteTotal: Optional[int] = Field(default=None, alias="powder_glacite_total")
    powderSpentGlacite: Optional[int] = Field(default=None, alias="powder_spent_glacite")
    currentDailyEffect: Optional[str] = Field(default=None, alias="current_daily_effect")
    currentDailyEffectLastChanged: Optional[int] = Field(
        default=None, alias="current_daily_effect_last_changed"
    )


class Crystal(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    state: Optional[str] = None
    totalPlaced: Optional[int] = Field(default=None, alias="total_placed")
    totalFound: Optional[int] = Field(default=None, alias="total_found")


class Biomes(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    precursor: Optional[Precursor] = None
    goblin: Optional[Goblin] = None
    jungle: Optional[Jungle] = None


class Precursor(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    claimingWithPrecursorApparatus: Optional[bool] = Field(
        default=None, alias="claiming_with_precursor_apparatus"
    )
    talkedToProfessor: Optional[bool] = Field(default=None, alias="talked_to_professor")


class Goblin(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    kingQuestActive: Optional[bool] = Field(default=None, alias="king_quest_active")
    kingQuestsCompleted: Optional[int] = Field(default=None, alias="king_quests_completed")


class Jungle(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    jungleTempleOpen: Optional[bool] = Field(default=None, alias="jungle_temple_open")
    jungleTempleChestUses: Optional[int] = Field(default=None, alias="jungle_temple_chest_uses")
