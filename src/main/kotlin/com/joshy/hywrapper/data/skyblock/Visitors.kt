package com.joshy.hywrapper.data.skyblock

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
enum class Visitor(val cleanName: String) {
    @SerialName("jerry")
    JERRY("Jerry"),

    @SerialName("jack")
    JACK("Jack"),

    @SerialName("tia")
    TIA("Tia"),

    @SerialName("gwendolyn")
    GWENDOLYN("Gwendolyn"),

    @SerialName("leo")
    LEO("Leo"),

    @SerialName("anita")
    ANITA("Anita"),

    @SerialName("seraphine")
    SERAPHINE("Seraphine"),

    @SerialName("dusk")
    DUSK("Dusk"),

    @SerialName("vex")
    VEX("Vex"),

    @SerialName("iron_forger")
    IRON_FORGER("Iron Forger"),

    @SerialName("jacob")
    JACOB("Jacob"),

    @SerialName("emissary_ceanna")
    EMISSARY_CEANNA("Emissary Ceanna"),

    @SerialName("emissary_wilson")
    EMISSARY_WILSON("Emissary Wilson"),

    @SerialName("duke")
    DUKE("Duke"),

    @SerialName("grandma_wolf")
    GRANDMA_WOLF("Grandma Wolf"),

    @SerialName("rusty")
    RUSTY("Rusty"),

    @SerialName("rhys")
    RHYS("Rhys"),

    @SerialName("lynn")
    LYNN("Lynn"),

    @SerialName("zog")
    ZOG("Zog"),

    @SerialName("shifty")
    SHIFTY("Shifty"),

    @SerialName("terry")
    TERRY("Terry"),

    @SerialName("librarian")
    LIBRARIAN("Librarian"),

    @SerialName("stella")
    STELLA("Stella"),

    @SerialName("lumina")
    LUMINA("Lumina"),

    @SerialName("felix")
    FELIX("Felix"),

    @SerialName("adventurer")
    ADVENTURER("Adventurer"),

    @SerialName("geonathan_greatforge")
    GEONATHAN_GREATFORGE("Geonathan Greatforge"),

    @SerialName("friendly_hiker")
    FRIENDLY_HIKER("Friendly Hiker"),

    @SerialName("trevor")
    TREVOR("Trevor"),

    @SerialName("ryu")
    RYU("Ryu"),

    @SerialName("sirius")
    SIRIUS("Sirius"),

    @SerialName("bartender")
    BARTENDER("Bartender"),

    @SerialName("jotraeline_greatforge")
    JOTRAELINE_GREATFORGE("Jotraeline Greatforge"),

    @SerialName("lazy_miner")
    LAZY_MINER("Lazy Miner"),

    @SerialName("weaponsmith")
    WEAPONSMITH("Weaponsmith"),

    @SerialName("fisherman")
    FISHERMAN("Fisherman"),

    @SerialName("odawa")
    ODAWA("Odawa"),

    @SerialName("andrew")
    ANDREW("Andrew"),

    @SerialName("alchemist")
    ALCHEMIST("Alchemist"),

    @SerialName("liam")
    LIAM("Liam"),

    @SerialName("wizard")
    WIZARD("Wizard"),

    @SerialName("madame_eleanor")
    MADAME_ELEANOR("Madame Eleanor"),

    @SerialName("fear_mongerer")
    FEAR_MONGERER("Fear Mongerer"),

    @SerialName("plumber_joe")
    PLUMBER_JOE("Plumber Joe"),

    @SerialName("seymour")
    SEYMOUR("Seymour"),

    @SerialName("dalbrek")
    DALBREK("Dalbrek"),

    @SerialName("queen_mismyla")
    QUEEN_MISMYLA("Queen Mismyla"),

    @SerialName("old_man_garry")
    OLD_MAN_GARRY("Old Man Garry"),

    @SerialName("sargwyn")
    SARGWYN("Sargwyn"),

    @SerialName("banker_broadjaw")
    BANKER_BROADJAW("Banker Broadjaw"),

    @SerialName("mason")
    MASON("Mason"),

    @SerialName("emissary_carlton")
    EMISSARY_CARLTON("Emissary Carlton"),

    @SerialName("jamie")
    JAMIE("Jamie"),

    @SerialName("tom")
    TOM("Tom"),

    @SerialName("emissary_fraiser")
    EMISSARY_FRAISER("Emissary Fraiser"),

    @SerialName("tammy")
    TAMMY("Tammy"),

    @SerialName("gold_forger")
    GOLD_FORGER("Gold Forger"),

    @SerialName("gimley")
    GIMLEY("Gimley"),

    @SerialName("fragilis")
    FRAGILIS("Fragilis"),

    @SerialName("guy")
    GUY("Guy"),

    @SerialName("tarwen")
    TARWEN("Tarwen"),

    @SerialName("farmhand")
    FARMHAND("Farmhand"),

    @SerialName("arthur")
    ARTHUR("Arthur"),

    @SerialName("royal_resident_neighbour")
    ROYAL_RESIDENT_NEIGHBOUR("Royal Resident Neighbour"),

    @SerialName("hornum")
    HORNUM("Hornum"),

    @SerialName("beth")
    BETH("Beth"),

    @SerialName("xalx")
    XALX("Xalx"),

    @SerialName("hungry_hiker")
    HUNGRY_HIKER("Hungry Hiker"),

    @SerialName("lumberjack")
    LUMBERJACK("Lumberjack"),

    @SerialName("oringo")
    ORINGO("Oringo"),

    @SerialName("royal_resident_reward")
    ROYAL_RESIDENT_REWARD("Royal Resident Reward"),

    @SerialName("shaggy")
    SHAGGY("Shaggy"),

    @SerialName("royal_resident_peasant")
    ROYAL_RESIDENT_PEASANT("Royal Resident Peasant"),

    @SerialName("farmer_jon")
    FARMER_JON("Farmer Jon"),

    @SerialName("puzzler")
    PUZZLER("Puzzler"),

    @SerialName("emissary_sisko")
    EMISSARY_SISKO("Emissary Sisko"),

    @SerialName("bear_pete")
    BEAR_PETE("Bear Pete"),

    @SerialName("maeve")
    MAEVE("Maeve"),

    @SerialName("spaceman")
    SPACEMAN("Spaceman"),

    @SerialName("pest_wrangler")
    PEST_WRANGLER("Pest Wrangler"),

    @SerialName("vinyl_collector")
    VINYL_COLLECTOR("Vinyl Collector"),

    @SerialName("ravenous_rhino")
    RAVENOUS_RHINO("Ravenous Rhino"),

    @SerialName("disguised_rats")
    DISGUISED_RATS("Disguised Rats"),

    @SerialName("baker")
    BAKER("Baker"),

    @SerialName("carpenter")
    CARPENTER("Carpenter"),

    @SerialName("ophelia")
    OPHELIA("Ophelia"),

    @SerialName("lift_operator")
    LIFT_OPERATOR("Lift Operator"),

    @SerialName("moby")
    MOBY("Moby"),

    @SerialName("fire_guy")
    FIRE_GUY("Fire Guy"),

    @SerialName("farm_merchant")
    FARM_MERCHANT("Farm Merchant"),

    @SerialName("bruuh")
    BRUUH("Bruuh"),

    @SerialName("elle")
    ELLE("Elle"),

    @SerialName("gemma")
    GEMMA("Gemma"),

    @SerialName("bednom")
    BEDNOM("Bednom"),

    @SerialName("trinity")
    TRINITY("Trinity"),

    @SerialName("dulin_tunnels")
    DULIN_TUNNELS("Dulin Tunnels"),

    @SerialName("spider_tamer")
    SPIDER_TAMER("Spider Tamer"),

    @SerialName("romero")
    ROMERO("Romero"),

    @SerialName("master_tactician")
    MASTER_TACTICIAN("Master Tactician"),

    @SerialName("end_dealer")
    END_DEALER("End Dealer"),

    @SerialName("erihann")
    ERIHANN("Erihann"),

    @SerialName("cold_enjoyer")
    COLD_ENJOYER("Cold Enjoyer"),

    @SerialName("sherry")
    SHERRY("Sherry"),

    @SerialName("an")
    AN("An"),

    @SerialName("chantelle")
    CHANTELLE("Chantelle"),

    @SerialName("frozen_alex")
    FROZEN_ALEX("Frozen Alex"),

    @SerialName("queen_nyx")
    QUEEN_NYX("Queen Nyx"),

    @SerialName("archaeologist")
    ARCHAEOLOGIST("Archaeologist"),

    @SerialName("vincent")
    VINCENT("Vincent"),

    @SerialName("marigold")
    MARIGOLD("Marigold"),

    @SerialName("chief_scorn")
    CHIEF_SCORN("Chief Scorn"),

    @SerialName("tomioka")
    TOMIOKA("Tomioka"),

    @SerialName("vargul_garden")
    VARGUL_GARDEN("Vargul Garden"),

    @SerialName("ludleth")
    LUDLETH("Ludleth"),

    @SerialName("wolf_shaman")
    WOLF_SHAMAN("Wolf Shaman"),

    @SerialName("scardius")
    SCARDIUS("Scardius"),

    @SerialName("st_jerry")
    ST_JERRY("St Jerry"),

    @SerialName("snowmaker")
    SNOWMAKER("Snowmaker"),

    @SerialName("hendrik")
    HENDRIK("Hendrik"),

    @SerialName("pet_trainer")
    PET_TRAINER("Pet Trainer"),

    @SerialName("artist")
    ARTIST("Artist"),

    @SerialName("jacobus")
    JACOBUS("Jacobus"),

    @SerialName("dragon_ritualist")
    DRAGON_RITUALIST("Dragon Ritualist"),

    @SerialName("mage_alchemist")
    MAGE_ALCHEMIST("Mage Alchemist"),

    @SerialName("hoppity")
    HOPPITY("Hoppity"),

    @SerialName("dante_goon")
    DANTE_GOON("Dante Goon"),

    @SerialName("mayor_diaz")
    MAYOR_DIAZ("Mayor Diaz"),

    @SerialName("chunk")
    CHUNK("Chunk"),

    @SerialName("duncan")
    DUNCAN("Duncan"),

    @SerialName("mayor_paul")
    MAYOR_PAUL("Mayor Paul"),

    @SerialName("mayor_diana")
    MAYOR_DIANA("Mayor Diana"),

    @SerialName("mayor_marina")
    MAYOR_MARINA("Mayor Marina"),

    @SerialName("mayor_cole")
    MAYOR_COLE("Mayor Cole"),

    @SerialName("mayor_finnegan")
    MAYOR_FINNEGAN("Mayor Finnegan"),

    @SerialName("mayor_foxy")
    MAYOR_FOXY("Mayor Foxy"),

    @SerialName("mayor_aatrox")
    MAYOR_AATROX("Mayor Aatrox")
}