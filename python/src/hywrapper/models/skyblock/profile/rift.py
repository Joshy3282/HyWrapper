from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Rift(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    villagePlaza: Optional[VillagePlaza] = None
    witherCage: Optional[WitherCage] = None
    blackLagoon: Optional[BlackLagoon] = None
    deadCats: Optional[DeadCats] = None
    wizardTower: Optional[WizardTower] = None
    enigma: Optional[Enigma] = None
    slayerQuest: Optional[SlayerQuest] = None
    lifetimePurchasedBoundaries: List[str] = Field(default=[])
    westVillage: Optional[WestVillage] = None
    wyldWoods: Optional[WyldWoods] = None
    castle: Optional[Castle] = None
    access: Optional[Access] = None
    dreadfarm: Optional[Dreadfarm] = None
    inventory: Optional[Inventory] = None


class VillagePlaza(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    murder: Optional[Murder] = None
    barryCenter: Optional[BarryCenter] = None
    cowboy: Optional[Cowboy] = None
    lonely: Optional[Lonely] = None
    seraphine: Optional[Seraphine] = None
    gotScammed: Optional[bool] = None


class Murder(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    stepIndex: int = Field(default=0)
    roomClues: List[str] = Field(default=[])
    stepIndexPt2: int = Field(default=0)
    stepIndexPt3: int = Field(default=0)


class BarryCenter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    firstTalkToBarry: Optional[bool] = None
    convinced: List[str] = Field(default=[])
    receivedReward: Optional[bool] = None


class Cowboy(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    stage: int = Field(default=0)
    hayEaten: int
    rabbitName: str = Field(default="")
    exportedCarrots: int = Field(default=0)


class Lonely(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    secondsSitting: int = Field(default=0)


class Seraphine(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    stepIndex: int = Field(default=0)


class WitherCage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    killedEyes: List[str] = Field(default=[])


class BlackLagoon(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    talkedToEdwin: Optional[bool] = None
    receivedSciencePaper: Optional[bool] = None
    completedStep: int = Field(default=0)
    deliveredSciencePaper: Optional[bool] = None


class DeadCats(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    talkedToJacquelle: Optional[bool] = None
    pickedUpDetector: Optional[bool] = None
    foundCats: List[str] = Field(default=[])
    unlockedPet: Optional[bool] = None
    montezuma: Optional[Montezuma] = None


class Montezuma(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: Optional[str] = None
    uniqueId: str = Field(default="")
    type: str = Field(default="")
    exp: float = Field(default=0.0)
    active: Optional[bool] = None
    tier: str = Field(default="")
    heldItem: Optional[str] = None
    candyUsed: int = Field(default=0)
    petSoulbound: Optional[bool] = None
    skin: Optional[str] = None
    extra: Optional[str] = None


class WizardTower(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    wizardQuestStep: int = Field(default=0)
    crumbsLaidOut: int = Field(default=0)


class Enigma(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    boughtCloak: Optional[bool] = None
    foundSouls: List[str] = Field(default=[])
    claimedBonusIndex: int = Field(default=0)


class Gallery(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    eliseStep: int = Field(default=0)
    securedTrophies: List[SecuredTrophy] = Field(default=[])
    sentTrophyDialogues: List[str] = Field(default=[])


class SecuredTrophy(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = Field(default="")
    timestamp: int = Field(default=0)
    visits: int = Field(default=0)


class SlayerQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = Field(default="")
    tier: int = Field(default=0)
    startTimestamp: int = Field(default=0)
    completionState: int = Field(default=0)
    usedArmor: Optional[bool] = None
    solo: Optional[bool] = None
    combatXp: int = Field(default=0)
    recentMobKills: List[RecentMobKill] = Field(default=[])
    lastKilledMobIsland: str = Field(default="")
    spawnTimestamp: int = Field(default=0)


class RecentMobKill(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    xp: float = Field(default=0.0)
    timestamp: int = Field(default=0)


class WestVillage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    crazyKloon: Optional[CrazyKloon] = None
    mirrorverse: Optional[Mirrorverse] = None
    katHouse: Optional[KatHouse] = None
    glyph: Optional[Glyph] = None


class CrazyKloon(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    selectedColors: Dict[str, str] = Field(default={})
    talked: Optional[bool] = None
    hackedTerminals: List[str] = Field(default=[])
    questComplete: Optional[bool] = None


class Mirrorverse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    visitedRooms: List[str] = Field(default=[])
    upsideDownHard: Optional[bool] = None
    claimedChestItems: List[str] = Field(default=[])
    claimedReward: Optional[bool] = None


class KatHouse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    binCollectedSilverfish: int = Field(default=0)
    binCollectedSpider: int = Field(default=0)
    binCollectedMosquito: int = Field(default=0)


class Glyph(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    claimedWand: Optional[bool] = None
    currentGlyphDelivered: Optional[bool] = None
    currentGlyphCompleted: Optional[bool] = None
    currentGlyph: int = Field(default=0)
    completed: Optional[bool] = None
    claimedBraclet: Optional[bool] = None


class WyldWoods(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    siriusStartedQA: Optional[bool] = None
    siriusQAChainDone: Optional[bool] = None
    siriusCompletedQA: Optional[bool] = None
    siriusClaimedDoubloon: Optional[bool] = None
    talkedThreeBrothers: List[str] = Field(default=[])
    bughunterStep: int = Field(default=0)


class Castle(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    unlockedPathwaySkip: Optional[bool] = None
    fairyStep: int = Field(default=0)
    grubberStacks: int = Field(default=0)


class Access(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    lastFree: int = Field(default=0)
    consumedPrism: Optional[bool] = None
    chargeTrackTimestamp: int = Field(default=0)


class Dreadfarm(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    shaniaStage: int = Field(default=0)
    caducousFeederUses: List[int] = Field(default=[])


class Inventory(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    invContents: Optional[InventoryData] = None
    invArmor: Optional[InventoryData] = None
    enderChestContents: Optional[InventoryData] = None
    enderChestPageIcons: List[InventoryData] = Field(default=[])
    equipmentContents: Optional[InventoryData] = None


class InventoryData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: int = Field(default=0)
    data: str = Field(default="")
