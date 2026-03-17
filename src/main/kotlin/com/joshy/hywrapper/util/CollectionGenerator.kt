package com.joshy.hywrapper.util

import kotlinx.serialization.json.Json
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive
import java.io.File

object CollectionGenerator {
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
            File(resourcesDir, "collections.json"),
            File(sourceDir, "CollectionType.kt"),
        )
    }

    fun generate(
        jsonFile: File,
        outputFile: File,
    ) {
        val jsonText = jsonFile.readText()
        val root = Json.parseToJsonElement(jsonText).jsonObject
        val collections = root["collections"]?.jsonObject ?: return

        val allItems = mutableMapOf<String, String>()

        for ((_, categoryValue) in collections) {
            val items = categoryValue.jsonObject["items"]?.jsonObject ?: continue
            for ((itemKey, itemValue) in items) {
                val itemName = itemValue.jsonObject["name"]?.jsonPrimitive?.content ?: ""
                allItems[itemKey] = itemName
            }
        }

        val sb = StringBuilder()
        sb.append("package com.joshy.hywrapper.data.skyblock\n\n")
        sb.append("/**\n")
        sb.append(" * Automatically generated enum for Collections.\n")
        sb.append(" */\n")
        sb.append("enum class CollectionType(val id: String, val itemName: String) {\n")

        val sortedItems = allItems.toList().sortedBy { it.first }
        val usedEnumNames = mutableSetOf<String>()

        sortedItems.forEachIndexed { index, (id, name) ->
            var enumName = overrides[id] ?: id.replace(":", "_").uppercase()

            if (usedEnumNames.contains(enumName)) {
                enumName = "${enumName}_ALT"
            }
            usedEnumNames.add(enumName)

            val escapedName = name.replace("\"", "\\\"")
            sb.append("    $enumName(\"$id\", \"$escapedName\")")
            if (index < sortedItems.size - 1) {
                sb.append(",\n")
            } else {
                sb.append(";\n")
            }
        }

        sb.append("\n    companion object {\n")
        sb.append("        fun fromId(id: String): CollectionType? = entries.find { it.id == id }\n")
        sb.append("    }\n")
        sb.append("}\n")

        outputFile.parentFile.mkdirs()
        outputFile.writeText(sb.toString())
        println("Generated ${sortedItems.size} enum constants to ${outputFile.absolutePath}")
    }
}
