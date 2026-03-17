package com.joshy.hywrapper.util

import kotlinx.serialization.json.Json
import kotlinx.serialization.json.jsonObject
import java.io.File

object MuseumItemGenerator {
    @JvmStatic
    fun main(args: Array<String>) {
        val resourcesDir = File("src/main/resources")
        val sourceDir = File("src/main/kotlin/com/joshy/hywrapper/data/skyblock")

        generate(
            File(resourcesDir, "museum.json"),
            File(sourceDir, "MuseumItem.kt"),
        )
    }

    fun generate(
        jsonFile: File,
        outputFile: File,
    ) {
        val jsonText = jsonFile.readText()
        val root = Json.parseToJsonElement(jsonText).jsonObject
        val members = root["members"]?.jsonObject ?: return

        val allItemIds = mutableSetOf<String>()

        for ((_, memberValue) in members) {
            val items = memberValue.jsonObject["items"]?.jsonObject ?: continue
            allItemIds.addAll(items.keys)
        }

        val sb = StringBuilder()
        sb.append("package com.joshy.hywrapper.data.skyblock\n\n")
        sb.append("import kotlinx.serialization.SerialName\n")
        sb.append("import kotlinx.serialization.Serializable\n\n")
        sb.append("/**\n")
        sb.append(" * Automatically generated enum for Museum items.\n")
        sb.append(" */\n")
        sb.append("@Serializable\n")
        sb.append("enum class MuseumItem(val id: String) {\n")

        val sortedIds = allItemIds.sorted()
        sortedIds.forEachIndexed { index, id ->
            val enumName = id.replace(":", "_").uppercase()
            sb.append("    @SerialName(\"$id\")\n")
            sb.append("    $enumName(\"$id\")")
            if (index < sortedIds.size - 1) {
                sb.append(",\n")
            } else {
                sb.append(";\n")
            }
        }

        sb.append("\n    companion object {\n")
        sb.append("        fun fromId(id: String): MuseumItem? = entries.find { it.id == id }\n")
        sb.append("    }\n")
        sb.append("}\n")

        outputFile.parentFile.mkdirs()
        outputFile.writeText(sb.toString())
        println("Generated ${sortedIds.size} museum item constants with serialization to ${outputFile.absolutePath}")
    }
}
