from __future__ import annotations

from enum import Enum
from typing import Any, Optional


class CollectionType(str, Enum):
    AGARICUS_CAP = "AGARICUS_CAP"
    BLAZE_ROD = "BLAZE_ROD"
    BONE = "BONE"
    CACTUS = "CACTUS"
    CADUCOUS_STEM = "CADUCOUS_STEM"
    CARROT = "CARROT_ITEM"
    CHILI_PEPPER = "CHILI_PEPPER"
    CLAY_BALL = "CLAY_BALL"
    COAL = "COAL"
    COBBLESTONE = "COBBLESTONE"
    DIAMOND = "DIAMOND"
    DOUBLE_PLANT = "DOUBLE_PLANT"
    EMERALD = "EMERALD"
    ENDER_PEARL = "ENDER_PEARL"
    END_STONE = "ENDER_STONE"
    FEATHER = "FEATHER"
    FIG_LOG = "FIG_LOG"
    GEMSTONE_COLLECTION = "GEMSTONE_COLLECTION"
    GHAST_TEAR = "GHAST_TEAR"
    GLACITE = "GLACITE"
    GLOWSTONE_DUST = "GLOWSTONE_DUST"
    GOLD_INGOT = "GOLD_INGOT"
    GRAVEL = "GRAVEL"
    HALF_EATEN_CARROT = "HALF_EATEN_CARROT"
    HARD_STONE = "HARD_STONE"
    HEMOVIBE = "HEMOVIBE"
    ICE = "ICE"
    INK_SACK = "INK_SACK"
    COCOA_BEANS = "INK_SACK:3"
    LAPIS_LAZULI = "INK_SACK:4"
    IRON_INGOT = "IRON_INGOT"
    LEATHER = "LEATHER"
    OAK_LOG = "LOG"
    SPRUCE_LOG = "LOG:1"
    BIRCH_LOG = "LOG:2"
    JUNGLE_LOG = "LOG:3"
    ACACIA_LOG = "LOG_2"
    DARK_OAK_LOG = "LOG_2:1"
    LUSHLILAC = "LUSHLILAC"
    MAGMA_CREAM = "MAGMA_CREAM"
    MAGMA_FISH = "MAGMA_FISH"
    MANGROVE_LOG = "MANGROVE_LOG"
    MELON = "MELON"
    METAL_HEART = "METAL_HEART"
    MITHRIL_ORE = "MITHRIL_ORE"
    MOONFLOWER = "MOONFLOWER"
    MUSHROOM = "MUSHROOM_COLLECTION"
    MUTTON = "MUTTON"
    MYCEL = "MYCEL"
    NETHERRACK = "NETHERRACK"
    NETHER_WART = "NETHER_STALK"
    OBSIDIAN = "OBSIDIAN"
    PORKCHOP = "PORK"
    POTATO = "POTATO_ITEM"
    PRISMARINE_CRYSTALS = "PRISMARINE_CRYSTALS"
    PRISMARINE_SHARD = "PRISMARINE_SHARD"
    PUMPKIN = "PUMPKIN"
    QUARTZ = "QUARTZ"
    RABBIT = "RABBIT"
    CHICKEN = "RAW_CHICKEN"
    RAW_FISH = "RAW_FISH"
    SALMON = "RAW_FISH:1"
    CLOWNFISH = "RAW_FISH:2"
    PUFFERFISH = "RAW_FISH:3"
    REDSTONE = "REDSTONE"
    ROTTEN_FLESH = "ROTTEN_FLESH"
    SAND = "SAND"
    RED_SAND = "SAND:1"
    SEA_LUMIES = "SEA_LUMIES"
    SEEDS = "SEEDS"
    SLIME_BALL = "SLIME_BALL"
    SPIDER_EYE = "SPIDER_EYE"
    SPONGE = "SPONGE"
    STRING = "STRING"
    SUGAR_CANE = "SUGAR_CANE"
    SULPHUR = "SULPHUR"
    SULPHUR_ORE = "SULPHUR_ORE"
    TENDER_WOOD = "TENDER_WOOD"
    TIMITE = "TIMITE"
    TUNGSTEN = "TUNGSTEN"
    UMBER = "UMBER"
    VINESAP = "VINESAP"
    WATER_LILY = "WATER_LILY"
    WHEAT = "WHEAT"
    WILD_ROSE = "WILD_ROSE"
    WILTED_BERBERIS = "WILTED_BERBERIS"

    @property
    def id(self) -> str:
        return _IDS[self]

    @property
    def item_name(self) -> str:
        return _ITEM_NAMES[self]

    @classmethod
    def from_id(cls, id: Any) -> Optional[CollectionType]:
        try:
            return cls(id)
        except ValueError:
            return None


_IDS = {
    CollectionType.AGARICUS_CAP: "AGARICUS_CAP",
    CollectionType.BLAZE_ROD: "BLAZE_ROD",
    CollectionType.BONE: "BONE",
    CollectionType.CACTUS: "CACTUS",
    CollectionType.CADUCOUS_STEM: "CADUCOUS_STEM",
    CollectionType.CARROT: "CARROT_ITEM",
    CollectionType.CHILI_PEPPER: "CHILI_PEPPER",
    CollectionType.CLAY_BALL: "CLAY_BALL",
    CollectionType.COAL: "COAL",
    CollectionType.COBBLESTONE: "COBBLESTONE",
    CollectionType.DIAMOND: "DIAMOND",
    CollectionType.DOUBLE_PLANT: "DOUBLE_PLANT",
    CollectionType.EMERALD: "EMERALD",
    CollectionType.ENDER_PEARL: "ENDER_PEARL",
    CollectionType.END_STONE: "ENDER_STONE",
    CollectionType.FEATHER: "FEATHER",
    CollectionType.FIG_LOG: "FIG_LOG",
    CollectionType.GEMSTONE_COLLECTION: "GEMSTONE_COLLECTION",
    CollectionType.GHAST_TEAR: "GHAST_TEAR",
    CollectionType.GLACITE: "GLACITE",
    CollectionType.GLOWSTONE_DUST: "GLOWSTONE_DUST",
    CollectionType.GOLD_INGOT: "GOLD_INGOT",
    CollectionType.GRAVEL: "GRAVEL",
    CollectionType.HALF_EATEN_CARROT: "HALF_EATEN_CARROT",
    CollectionType.HARD_STONE: "HARD_STONE",
    CollectionType.HEMOVIBE: "HEMOVIBE",
    CollectionType.ICE: "ICE",
    CollectionType.INK_SACK: "INK_SACK",
    CollectionType.COCOA_BEANS: "INK_SACK:3",
    CollectionType.LAPIS_LAZULI: "INK_SACK:4",
    CollectionType.IRON_INGOT: "IRON_INGOT",
    CollectionType.LEATHER: "LEATHER",
    CollectionType.OAK_LOG: "LOG",
    CollectionType.SPRUCE_LOG: "LOG:1",
    CollectionType.BIRCH_LOG: "LOG:2",
    CollectionType.JUNGLE_LOG: "LOG:3",
    CollectionType.ACACIA_LOG: "LOG_2",
    CollectionType.DARK_OAK_LOG: "LOG_2:1",
    CollectionType.LUSHLILAC: "LUSHLILAC",
    CollectionType.MAGMA_CREAM: "MAGMA_CREAM",
    CollectionType.MAGMA_FISH: "MAGMA_FISH",
    CollectionType.MANGROVE_LOG: "MANGROVE_LOG",
    CollectionType.MELON: "MELON",
    CollectionType.METAL_HEART: "METAL_HEART",
    CollectionType.MITHRIL_ORE: "MITHRIL_ORE",
    CollectionType.MOONFLOWER: "MOONFLOWER",
    CollectionType.MUSHROOM: "MUSHROOM_COLLECTION",
    CollectionType.MUTTON: "MUTTON",
    CollectionType.MYCEL: "MYCEL",
    CollectionType.NETHERRACK: "NETHERRACK",
    CollectionType.NETHER_WART: "NETHER_STALK",
    CollectionType.OBSIDIAN: "OBSIDIAN",
    CollectionType.PORKCHOP: "PORK",
    CollectionType.POTATO: "POTATO_ITEM",
    CollectionType.PRISMARINE_CRYSTALS: "PRISMARINE_CRYSTALS",
    CollectionType.PRISMARINE_SHARD: "PRISMARINE_SHARD",
    CollectionType.PUMPKIN: "PUMPKIN",
    CollectionType.QUARTZ: "QUARTZ",
    CollectionType.RABBIT: "RABBIT",
    CollectionType.CHICKEN: "RAW_CHICKEN",
    CollectionType.RAW_FISH: "RAW_FISH",
    CollectionType.SALMON: "RAW_FISH:1",
    CollectionType.CLOWNFISH: "RAW_FISH:2",
    CollectionType.PUFFERFISH: "RAW_FISH:3",
    CollectionType.REDSTONE: "REDSTONE",
    CollectionType.ROTTEN_FLESH: "ROTTEN_FLESH",
    CollectionType.SAND: "SAND",
    CollectionType.RED_SAND: "SAND:1",
    CollectionType.SEA_LUMIES: "SEA_LUMIES",
    CollectionType.SEEDS: "SEEDS",
    CollectionType.SLIME_BALL: "SLIME_BALL",
    CollectionType.SPIDER_EYE: "SPIDER_EYE",
    CollectionType.SPONGE: "SPONGE",
    CollectionType.STRING: "STRING",
    CollectionType.SUGAR_CANE: "SUGAR_CANE",
    CollectionType.SULPHUR: "SULPHUR",
    CollectionType.SULPHUR_ORE: "SULPHUR_ORE",
    CollectionType.TENDER_WOOD: "TENDER_WOOD",
    CollectionType.TIMITE: "TIMITE",
    CollectionType.TUNGSTEN: "TUNGSTEN",
    CollectionType.UMBER: "UMBER",
    CollectionType.VINESAP: "VINESAP",
    CollectionType.WATER_LILY: "WATER_LILY",
    CollectionType.WHEAT: "WHEAT",
    CollectionType.WILD_ROSE: "WILD_ROSE",
    CollectionType.WILTED_BERBERIS: "WILTED_BERBERIS",
}

_ITEM_NAMES = {
    CollectionType.AGARICUS_CAP: "Agaricus Cap",
    CollectionType.BLAZE_ROD: "Blaze Rod",
    CollectionType.BONE: "Bone",
    CollectionType.CACTUS: "Cactus",
    CollectionType.CADUCOUS_STEM: "Caducous Stem",
    CollectionType.CARROT: "Carrot",
    CollectionType.CHILI_PEPPER: "Chili Pepper",
    CollectionType.CLAY_BALL: "Clay Ball",
    CollectionType.COAL: "Coal",
    CollectionType.COBBLESTONE: "Cobblestone",
    CollectionType.DIAMOND: "Diamond",
    CollectionType.DOUBLE_PLANT: "Sunflower",
    CollectionType.EMERALD: "Emerald",
    CollectionType.ENDER_PEARL: "Ender Pearl",
    CollectionType.END_STONE: "End Stone",
    CollectionType.FEATHER: "Feather",
    CollectionType.FIG_LOG: "Fig Log",
    CollectionType.GEMSTONE_COLLECTION: "Gemstone",
    CollectionType.GHAST_TEAR: "Ghast Tear",
    CollectionType.GLACITE: "Glacite",
    CollectionType.GLOWSTONE_DUST: "Glowstone Dust",
    CollectionType.GOLD_INGOT: "Gold Ingot",
    CollectionType.GRAVEL: "Gravel",
    CollectionType.HALF_EATEN_CARROT: "Half-Eaten Carrot",
    CollectionType.HARD_STONE: "Hard Stone",
    CollectionType.HEMOVIBE: "Hemovibe",
    CollectionType.ICE: "Ice",
    CollectionType.INK_SACK: "Ink Sac",
    CollectionType.COCOA_BEANS: "Cocoa Beans",
    CollectionType.LAPIS_LAZULI: "Lapis Lazuli",
    CollectionType.IRON_INGOT: "Iron Ingot",
    CollectionType.LEATHER: "Leather",
    CollectionType.OAK_LOG: "Oak Log",
    CollectionType.SPRUCE_LOG: "Spruce Log",
    CollectionType.BIRCH_LOG: "Birch Log",
    CollectionType.JUNGLE_LOG: "Jungle Log",
    CollectionType.ACACIA_LOG: "Acacia Log",
    CollectionType.DARK_OAK_LOG: "Dark Oak Log",
    CollectionType.LUSHLILAC: "Lushlilac",
    CollectionType.MAGMA_CREAM: "Magma Cream",
    CollectionType.MAGMA_FISH: "Magmafish",
    CollectionType.MANGROVE_LOG: "Mangrove Log",
    CollectionType.MELON: "Melon Slice",
    CollectionType.METAL_HEART: "Living Metal Heart",
    CollectionType.MITHRIL_ORE: "Mithril",
    CollectionType.MOONFLOWER: "Moonflower",
    CollectionType.MUSHROOM: "Mushroom",
    CollectionType.MUTTON: "Raw Mutton",
    CollectionType.MYCEL: "Mycelium",
    CollectionType.NETHERRACK: "Netherrack",
    CollectionType.NETHER_WART: "Nether Wart",
    CollectionType.OBSIDIAN: "Obsidian",
    CollectionType.PORKCHOP: "Raw Porkchop",
    CollectionType.POTATO: "Potato",
    CollectionType.PRISMARINE_CRYSTALS: "Prismarine Crystals",
    CollectionType.PRISMARINE_SHARD: "Prismarine Shard",
    CollectionType.PUMPKIN: "Pumpkin",
    CollectionType.QUARTZ: "Nether Quartz",
    CollectionType.RABBIT: "Raw Rabbit",
    CollectionType.CHICKEN: "Raw Chicken",
    CollectionType.RAW_FISH: "Raw Cod",
    CollectionType.SALMON: "Raw Salmon",
    CollectionType.CLOWNFISH: "Tropical Fish",
    CollectionType.PUFFERFISH: "Pufferfish",
    CollectionType.REDSTONE: "Redstone Dust",
    CollectionType.ROTTEN_FLESH: "Rotten Flesh",
    CollectionType.SAND: "Sand",
    CollectionType.RED_SAND: "Red Sand",
    CollectionType.SEA_LUMIES: "Sea Lumies",
    CollectionType.SEEDS: "Seeds",
    CollectionType.SLIME_BALL: "Slimeball",
    CollectionType.SPIDER_EYE: "Spider Eye",
    CollectionType.SPONGE: "Sponge",
    CollectionType.STRING: "String",
    CollectionType.SUGAR_CANE: "Sugar Cane",
    CollectionType.SULPHUR: "Gunpowder",
    CollectionType.SULPHUR_ORE: "Sulphur",
    CollectionType.TENDER_WOOD: "Tender Wood",
    CollectionType.TIMITE: "Timite",
    CollectionType.TUNGSTEN: "Tungsten",
    CollectionType.UMBER: "Umber",
    CollectionType.VINESAP: "Vinesap",
    CollectionType.WATER_LILY: "Lily Pad",
    CollectionType.WHEAT: "Wheat",
    CollectionType.WILD_ROSE: "Wild Rose",
    CollectionType.WILTED_BERBERIS: "Wilted Berberis",
}
