from __future__ import annotations

from enum import Enum
from typing import Any, Optional


class Visitor(str, Enum):
    JERRY = "jerry"
    JACK = "jack"
    TIA = "tia"
    GWENDOLYN = "gwendolyn"
    LEO = "leo"
    ANITA = "anita"
    SERAPHINE = "seraphine"
    DUSK = "dusk"
    VEX = "vex"
    IRON_FORGER = "iron_forger"
    JACOB = "jacob"
    EMISSARY_CEANNA = "emissary_ceanna"
    EMISSARY_WILSON = "emissary_wilson"
    DUKE = "duke"
    GRANDMA_WOLF = "grandma_wolf"
    RUSTY = "rusty"
    RHYS = "rhys"
    LYNN = "lynn"
    ZOG = "zog"
    SHIFTY = "shifty"
    TERRY = "terry"
    LIBRARIAN = "librarian"
    STELLA = "stella"
    LUMINA = "lumina"
    FELIX = "felix"
    ADVENTURER = "adventurer"
    GEONATHAN_GREATFORGE = "geonathan_greatforge"
    FRIENDLY_HIKER = "friendly_hiker"
    TREVOR = "trevor"
    RYU = "ryu"
    SIRIUS = "sirius"
    BARTENDER = "bartender"
    JOTRAELINE_GREATFORGE = "jotraeline_greatforge"
    LAZY_MINER = "lazy_miner"
    WEAPONSMITH = "weaponsmith"
    FISHERMAN = "fisherman"
    ODAWA = "odawa"
    ANDREW = "andrew"
    ALCHEMIST = "alchemist"
    LIAM = "liam"
    WIZARD = "wizard"
    MADAME_ELEANOR = "madame_eleanor"
    FEAR_MONGERER = "fear_mongerer"
    PLUMBER_JOE = "plumber_joe"
    SEYMOUR = "seymour"
    DALBREK = "dalbrek"
    QUEEN_MISMYLA = "queen_mismyla"
    OLD_MAN_GARRY = "old_man_garry"
    SARGWYN = "sargwyn"
    BANKER_BROADJAW = "banker_broadjaw"
    MASON = "mason"
    EMISSARY_CARLTON = "emissary_carlton"
    JAMIE = "jamie"
    TOM = "tom"
    EMISSARY_FRAISER = "emissary_fraiser"
    TAMMY = "tammy"
    GOLD_FORGER = "gold_forger"
    GIMLEY = "gimley"
    FRAGILIS = "fragilis"
    GUY = "guy"
    TARWEN = "tarwen"
    FARMHAND = "farmhand"
    ARTHUR = "arthur"
    ROYAL_RESIDENT_NEIGHBOUR = "royal_resident_neighbour"
    HORNUM = "hornum"
    BETH = "beth"
    XALX = "xalx"
    HUNGRY_HIKER = "hungry_hiker"
    LUMBERJACK = "lumberjack"
    ORINGO = "oringo"
    ROYAL_RESIDENT_REWARD = "royal_resident_reward"
    SHAGGY = "shaggy"
    ROYAL_RESIDENT_PEASANT = "royal_resident_peasant"
    FARMER_JON = "farmer_jon"
    PUZZLER = "puzzler"
    EMISSARY_SISKO = "emissary_sisko"
    BEAR_PETE = "bear_pete"
    MAEVE = "maeve"
    SPACEMAN = "spaceman"
    PEST_WRANGLER = "pest_wrangler"
    VINYL_COLLECTOR = "vinyl_collector"
    RAVENOUS_RHINO = "ravenous_rhino"
    DISGUISED_RATS = "disguised_rats"
    BAKER = "baker"
    CARPENTER = "carpenter"
    OPHELIA = "ophelia"
    LIFT_OPERATOR = "lift_operator"
    MOBY = "moby"
    FIRE_GUY = "fire_guy"
    FARM_MERCHANT = "farm_merchant"
    BRUUH = "bruuh"
    ELLE = "elle"
    GEMMA = "gemma"
    BEDNOM = "bednom"
    TRINITY = "trinity"
    DULIN_TUNNELS = "dulin_tunnels"
    SPIDER_TAMER = "spider_tamer"
    ROMERO = "romero"
    MASTER_TACTICIAN = "master_tactician"
    END_DEALER = "end_dealer"
    ERIHANN = "erihann"
    COLD_ENJOYER = "cold_enjoyer"
    SHERRY = "sherry"
    AN = "an"
    CHANTELLE = "chantelle"
    FROZEN_ALEX = "frozen_alex"
    QUEEN_NYX = "queen_nyx"
    ARCHAEOLOGIST = "archaeologist"
    VINCENT = "vincent"
    MARIGOLD = "marigold"
    CHIEF_SCORN = "chief_scorn"
    TOMIOKA = "tomioka"
    VARGUL_GARDEN = "vargul_garden"
    LUDLETH = "ludleth"
    WOLF_SHAMAN = "wolf_shaman"
    SCARDIUS = "scardius"
    ST_JERRY = "st_jerry"
    SNOWMAKER = "snowmaker"
    HENDRIK = "hendrik"
    PET_TRAINER = "pet_trainer"
    ARTIST = "artist"
    JACOBUS = "jacobus"
    DRAGON_RITUALIST = "dragon_ritualist"
    MAGE_ALCHEMIST = "mage_alchemist"
    HOPPITY = "hoppity"
    DANTE_GOON = "dante_goon"
    MAYOR_DIAZ = "mayor_diaz"
    CHUNK = "chunk"
    DUNCAN = "duncan"
    MAYOR_PAUL = "mayor_paul"
    MAYOR_DIANA = "mayor_diana"
    MAYOR_MARINA = "mayor_marina"
    MAYOR_COLE = "mayor_cole"
    MAYOR_FINNEGAN = "mayor_finnegan"
    MAYOR_FOXY = "mayor_foxy"
    MAYOR_AATROX = "mayor_aatrox"

    @property
    def clean_name(self) -> str:
        return _CLEAN_NAMES[self]

    @classmethod
    def from_id(cls, id: Any) -> Optional[Visitor]:
        try:
            return cls(id)
        except ValueError:
            return None


_CLEAN_NAMES = {
    Visitor.JERRY: "Jerry",
    Visitor.JACK: "Jack",
    Visitor.TIA: "Tia",
    Visitor.GWENDOLYN: "Gwendolyn",
    Visitor.LEO: "Leo",
    Visitor.ANITA: "Anita",
    Visitor.SERAPHINE: "Seraphine",
    Visitor.DUSK: "Dusk",
    Visitor.VEX: "Vex",
    Visitor.IRON_FORGER: "Iron Forger",
    Visitor.JACOB: "Jacob",
    Visitor.EMISSARY_CEANNA: "Emissary Ceanna",
    Visitor.EMISSARY_WILSON: "Emissary Wilson",
    Visitor.DUKE: "Duke",
    Visitor.GRANDMA_WOLF: "Grandma Wolf",
    Visitor.RUSTY: "Rusty",
    Visitor.RHYS: "Rhys",
    Visitor.LYNN: "Lynn",
    Visitor.ZOG: "Zog",
    Visitor.SHIFTY: "Shifty",
    Visitor.TERRY: "Terry",
    Visitor.LIBRARIAN: "Librarian",
    Visitor.STELLA: "Stella",
    Visitor.LUMINA: "Lumina",
    Visitor.FELIX: "Felix",
    Visitor.ADVENTURER: "Adventurer",
    Visitor.GEONATHAN_GREATFORGE: "Geonathan Greatforge",
    Visitor.FRIENDLY_HIKER: "Friendly Hiker",
    Visitor.TREVOR: "Trevor",
    Visitor.RYU: "Ryu",
    Visitor.SIRIUS: "Sirius",
    Visitor.BARTENDER: "Bartender",
    Visitor.JOTRAELINE_GREATFORGE: "Jotraeline Greatforge",
    Visitor.LAZY_MINER: "Lazy Miner",
    Visitor.WEAPONSMITH: "Weaponsmith",
    Visitor.FISHERMAN: "Fisherman",
    Visitor.ODAWA: "Odawa",
    Visitor.ANDREW: "Andrew",
    Visitor.ALCHEMIST: "Alchemist",
    Visitor.LIAM: "Liam",
    Visitor.WIZARD: "Wizard",
    Visitor.MADAME_ELEANOR: "Madame Eleanor",
    Visitor.FEAR_MONGERER: "Fear Mongerer",
    Visitor.PLUMBER_JOE: "Plumber Joe",
    Visitor.SEYMOUR: "Seymour",
    Visitor.DALBREK: "Dalbrek",
    Visitor.QUEEN_MISMYLA: "Queen Mismyla",
    Visitor.OLD_MAN_GARRY: "Old Man Garry",
    Visitor.SARGWYN: "Sargwyn",
    Visitor.BANKER_BROADJAW: "Banker Broadjaw",
    Visitor.MASON: "Mason",
    Visitor.EMISSARY_CARLTON: "Emissary Carlton",
    Visitor.JAMIE: "Jamie",
    Visitor.TOM: "Tom",
    Visitor.EMISSARY_FRAISER: "Emissary Fraiser",
    Visitor.TAMMY: "Tammy",
    Visitor.GOLD_FORGER: "Gold Forger",
    Visitor.GIMLEY: "Gimley",
    Visitor.FRAGILIS: "Fragilis",
    Visitor.GUY: "Guy",
    Visitor.TARWEN: "Tarwen",
    Visitor.FARMHAND: "Farmhand",
    Visitor.ARTHUR: "Arthur",
    Visitor.ROYAL_RESIDENT_NEIGHBOUR: "Royal Resident Neighbour",
    Visitor.HORNUM: "Hornum",
    Visitor.BETH: "Beth",
    Visitor.XALX: "Xalx",
    Visitor.HUNGRY_HIKER: "Hungry Hiker",
    Visitor.LUMBERJACK: "Lumberjack",
    Visitor.ORINGO: "Oringo",
    Visitor.ROYAL_RESIDENT_REWARD: "Royal Resident Reward",
    Visitor.SHAGGY: "Shaggy",
    Visitor.ROYAL_RESIDENT_PEASANT: "Royal Resident Peasant",
    Visitor.FARMER_JON: "Farmer Jon",
    Visitor.PUZZLER: "Puzzler",
    Visitor.EMISSARY_SISKO: "Emissary Sisko",
    Visitor.BEAR_PETE: "Bear Pete",
    Visitor.MAEVE: "Maeve",
    Visitor.SPACEMAN: "Spaceman",
    Visitor.PEST_WRANGLER: "Pest Wrangler",
    Visitor.VINYL_COLLECTOR: "Vinyl Collector",
    Visitor.RAVENOUS_RHINO: "Ravenous Rhino",
    Visitor.DISGUISED_RATS: "Disguised Rats",
    Visitor.BAKER: "Baker",
    Visitor.CARPENTER: "Carpenter",
    Visitor.OPHELIA: "Ophelia",
    Visitor.LIFT_OPERATOR: "Lift Operator",
    Visitor.MOBY: "Moby",
    Visitor.FIRE_GUY: "Fire Guy",
    Visitor.FARM_MERCHANT: "Farm Merchant",
    Visitor.BRUUH: "Bruuh",
    Visitor.ELLE: "Elle",
    Visitor.GEMMA: "Gemma",
    Visitor.BEDNOM: "Bednom",
    Visitor.TRINITY: "Trinity",
    Visitor.DULIN_TUNNELS: "Dulin Tunnels",
    Visitor.SPIDER_TAMER: "Spider Tamer",
    Visitor.ROMERO: "Romero",
    Visitor.MASTER_TACTICIAN: "Master Tactician",
    Visitor.END_DEALER: "End Dealer",
    Visitor.ERIHANN: "Erihann",
    Visitor.COLD_ENJOYER: "Cold Enjoyer",
    Visitor.SHERRY: "Sherry",
    Visitor.AN: "An",
    Visitor.CHANTELLE: "Chantelle",
    Visitor.FROZEN_ALEX: "Frozen Alex",
    Visitor.QUEEN_NYX: "Queen Nyx",
    Visitor.ARCHAEOLOGIST: "Archaeologist",
    Visitor.VINCENT: "Vincent",
    Visitor.MARIGOLD: "Marigold",
    Visitor.CHIEF_SCORN: "Chief Scorn",
    Visitor.TOMIOKA: "Tomioka",
    Visitor.VARGUL_GARDEN: "Vargul Garden",
    Visitor.LUDLETH: "Ludleth",
    Visitor.WOLF_SHAMAN: "Wolf Shaman",
    Visitor.SCARDIUS: "Scardius",
    Visitor.ST_JERRY: "St Jerry",
    Visitor.SNOWMAKER: "Snowmaker",
    Visitor.HENDRIK: "Hendrik",
    Visitor.PET_TRAINER: "Pet Trainer",
    Visitor.ARTIST: "Artist",
    Visitor.JACOBUS: "Jacobus",
    Visitor.DRAGON_RITUALIST: "Dragon Ritualist",
    Visitor.MAGE_ALCHEMIST: "Mage Alchemist",
    Visitor.HOPPITY: "Hoppity",
    Visitor.DANTE_GOON: "Dante Goon",
    Visitor.MAYOR_DIAZ: "Mayor Diaz",
    Visitor.CHUNK: "Chunk",
    Visitor.DUNCAN: "Duncan",
    Visitor.MAYOR_PAUL: "Mayor Paul",
    Visitor.MAYOR_DIANA: "Mayor Diana",
    Visitor.MAYOR_MARINA: "Mayor Marina",
    Visitor.MAYOR_COLE: "Mayor Cole",
    Visitor.MAYOR_FINNEGAN: "Mayor Finnegan",
    Visitor.MAYOR_FOXY: "Mayor Foxy",
    Visitor.MAYOR_AATROX: "Mayor Aatrox",
}
