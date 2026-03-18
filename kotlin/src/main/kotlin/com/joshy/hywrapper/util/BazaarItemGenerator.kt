package com.joshy.hywrapper.util

import kotlinx.serialization.json.Json
import kotlinx.serialization.json.jsonObject
import java.io.File

object BazaarItemGenerator {
    private val overrides =
        mapOf(
            "INK_SACK:3" to "COCOA_BEANS",
            "INK_SACK:4" to "LAPIS_LAZULI",
            "CARROT_ITEM" to "CARROT",
            "POTATO_ITEM" to "POTATO",
            "RAW_CHICKEN" to "CHICKEN",
            "RAW_FISH:1" to "SALMON",
            "RAW_FISH:2" to "CLOWNFISH",
            "RAW_FISH:3" to "PUFFERFISH",
            "MUSHROOM_COLLECTION" to "MUSHROOM",
            "NETHER_STALK" to "NETHER_WART",
            "PORK" to "PORKCHOP",
            "ENDER_STONE" to "END_STONE",
            "ENDER_PEARL" to "ENDER_PEARL",
            "LOG" to "OAK_LOG",
            "LOG:1" to "SPRUCE_LOG",
            "LOG:2" to "BIRCH_LOG",
            "LOG:3" to "JUNGLE_LOG",
            "LOG_2" to "ACACIA_LOG",
            "LOG_2:1" to "DARK_OAK_LOG",
            "SAND:1" to "RED_SAND",
        )

    @JvmStatic
    fun main(args: Array<String>) {
        val resourcesDir = File("src/main/resources")
        val sourceDir = File("src/main/kotlin/com/joshy/hywrapper/data/skyblock")

        generate(
            File(resourcesDir, "bazaar.json"),
            File(sourceDir, "BazaarItem.kt"),
        )
    }

    fun generate(
        jsonFile: File,
        outputFile: File,
    ) {
        val jsonText = jsonFile.readText()
        val root = Json.parseToJsonElement(jsonText).jsonObject
        val products = root["products"]?.jsonObject ?: return

        val sb = StringBuilder()
        sb.append("package com.joshy.hywrapper.data.skyblock\n\n")
        sb.append("/**\n")
        sb.append(" * Automatically generated enum for Bazaar items.\n")
        sb.append(" */\n")
        sb.append("enum class BazaarItem(val id: String) {\n")

        val productIds = products.keys.sorted()
        val usedEnumNames = mutableSetOf<String>()

        productIds.forEachIndexed { index, id ->
            var enumName = overrides[id] ?: id.replace(":", "_").uppercase()

            if (usedEnumNames.contains(enumName)) {
                enumName = "${enumName}_ALT"
            }
            usedEnumNames.add(enumName)

            sb.append("    $enumName(\"$id\")")
            if (index < productIds.size - 1) {
                sb.append(",\n")
            } else {
                sb.append(", ;\n")
            }
        }

        sb.append("\n    companion object {\n")
        sb.append("        fun fromId(id: String): BazaarItem? = entries.find { it.id == id }\n")
        sb.append("    }\n")
        sb.append("}\n")

        outputFile.parentFile.mkdirs()
        outputFile.writeText(sb.toString())
        println("Generated ${productIds.size} bazaar item constants to ${outputFile.absolutePath}")
    }
}
