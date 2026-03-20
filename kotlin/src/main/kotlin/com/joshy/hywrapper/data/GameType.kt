package com.joshy.hywrapper.data

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(with = GameTypeSerializer::class)
enum class GameType(val id: Int, val databaseName: String, val cleanName: String) {
    QUAKECRAFT(2, "Quake", "Quake"),
    WALLS(3, "Walls", "Walls"),
    PAINTBALL(4, "Paintball", "Paintball"),
    SURVIVAL_GAMES(5, "HungerGames", "Blitz Survival Games"),
    TNTGAMES(6, "TNTGames", "TNT Games"),
    VAMPIREZ(7, "VampireZ", "VampireZ"),
    WALLS3(13, "Walls3", "Mega Walls"),
    ARCADE(14, "Arcade", "Arcade"),
    ARENA(17, "Arena", "Arena"),
    UHC(20, "UHC", "UHC Champions"),
    MCGO(21, "MCGO", "Cops and Crims"),
    BATTLEGROUND(23, "Battleground", "Warlords"),
    SUPER_SMASH(24, "SuperSmash", "Smash Heroes"),
    GINGERBREAD(25, "GingerBread", "Turbo Kart Racers"),
    HOUSING(26, "Housing", "Housing"),
    SKYWARS(51, "SkyWars", "SkyWars"),
    TRUE_COMBAT(52, "TrueCombat", "Crazy Walls"),
    SPEED_UHC(54, "SpeedUHC", "Speed UHC"),
    SKYCLASH(55, "SkyClash", "SkyClash"),
    LEGACY(56, "Legacy", "Classic Games"),
    PROTOTYPE(57, "Prototype", "Prototype"),
    BEDWARS(58, "Bedwars", "Bed Wars"),
    MURDER_MYSTERY(59, "MurderMystery", "Murder Mystery"),
    BUILD_BATTLE(60, "BuildBattle", "Build Battle"),
    DUELS(61, "Duels", "Duels"),
    SKYBLOCK(63, "SkyBlock", "SkyBlock"),
    PIT(64, "Pit", "Pit"),
    REPLAY(65, "Replay", "Replay"),
    SMP(67, "SMP", "SMP"),
    WOOL_GAMES(68, "WoolGames", "Wool Wars"),
    ;

    companion object {
        fun fromId(id: Int): GameType? = entries.find { it.id == id }
    }
}

object GameTypeSerializer : KSerializer<GameType> {
    override val descriptor: SerialDescriptor =
        PrimitiveSerialDescriptor("GameType", PrimitiveKind.INT)

    override fun serialize(encoder: Encoder, value: GameType) {
        encoder.encodeInt(value.id)
    }

    override fun deserialize(decoder: Decoder): GameType {
        val id = decoder.decodeInt()
        return GameType.fromId(id) ?: throw IllegalArgumentException("Unknown GameType ID: $id")
    }
}
