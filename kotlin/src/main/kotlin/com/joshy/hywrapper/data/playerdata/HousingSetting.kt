package com.joshy.hywrapper.data.playerdata

import kotlin.reflect.KClass

enum class HousingSetting(val cleanName: String, val type: KClass<*>) {
    TIPS("Tips", Boolean::class),
    VISIBILITY("Visibility", Int::class),
    BORDER("Border", Boolean::class),
    PRO_TOOLS_PARTICLES("Pro Tools Particles", Boolean::class),
    HOUSING_PLUS_PREFIX("Housing Plus Prefix", Boolean::class),
    JUKEBOX_MUSIC("Jukebox Music", Boolean::class),
}
