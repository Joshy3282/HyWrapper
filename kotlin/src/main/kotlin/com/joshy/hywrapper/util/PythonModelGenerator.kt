package com.joshy.hywrapper.util

import java.io.File

fun main() {
    val kotlinSrcRoot = File("src/main/kotlin/com/joshy/hywrapper")
    val pythonSrcRoot = File("../python/src/hywrapper")

    val dataDir = File(kotlinSrcRoot, "data")
    val modelDir = File(kotlinSrcRoot, "model")

    val pythonDataDir = File(pythonSrcRoot, "data")
    val pythonModelDir = File(pythonSrcRoot, "models")

    pythonDataDir.mkdirs()
    pythonModelDir.mkdirs()

    val classMap = mutableMapOf<String, String>()

    collectClasses(dataDir, "hywrapper.data", classMap)
    collectClasses(modelDir, "hywrapper.models", classMap)

    processDirectory(dataDir, pythonDataDir, "hywrapper.data", classMap)
    processDirectory(modelDir, pythonModelDir, "hywrapper.models", classMap)

    generateInitFiles(pythonDataDir, "hywrapper.data", classMap)
    generateInitFiles(pythonModelDir, "hywrapper.models", classMap)
}

fun generateInitFiles(
    dir: File,
    pythonPackage: String,
    classMap: Map<String, String>,
) {
    val classesInThisPackage = classMap.filter { it.value.startsWith(pythonPackage) }
    val initFile = File(dir, "__init__.py")
    val content = StringBuilder()

    val modules = classesInThisPackage.values.distinct().sorted()
    modules.forEach { module ->
        val classes = classesInThisPackage.filter { it.value == module }.keys.sorted()
        if (classes.isNotEmpty()) {
            content.append("from $module import ${classes.joinToString(", ")}\n")
        }
    }

    if (classesInThisPackage.isNotEmpty()) {
        content.append("\n__all__ = [\n")
        classesInThisPackage.keys.sorted().forEach { className ->
            content.append("    \"$className\",\n")
        }
        content.append("]\n")
    }

    initFile.writeText(content.toString())

    dir.listFiles()?.filter { it.isDirectory }?.forEach { subDir ->
        generateInitFiles(subDir, "$pythonPackage.${subDir.name}", classMap)
    }
}

fun collectClasses(
    ktDir: File,
    pythonPackagePrefix: String,
    classMap: MutableMap<String, String>,
) {
    ktDir.walkTopDown().forEach { file ->
        if (file.isFile && file.extension == "kt") {
            val relativePath = file.parentFile.relativeTo(ktDir).path
            val pythonModule =
                if (relativePath.isEmpty()) {
                    pythonPackagePrefix + "." + file.nameWithoutExtension.toSnakeCase()
                } else {
                    pythonPackagePrefix + "." +
                        relativePath.replace(
                            File.separator,
                            ".",
                        ) + "." + file.nameWithoutExtension.toSnakeCase()
                }

            val content = file.readText()
            Regex("""(?:enum|data|abstract)\s+class\s+(\w+)""").findAll(content).forEach { match ->
                classMap[match.groupValues[1]] = pythonModule
            }
            Regex("""interface\s+(\w+)""").findAll(content).forEach { match ->
                classMap[match.groupValues[1]] = pythonModule
            }
        }
    }
}

fun processDirectory(
    ktDir: File,
    pyDir: File,
    pythonPackagePrefix: String,
    classMap: Map<String, String>,
) {
    ktDir.walkTopDown().forEach { file ->
        if (file.isFile && file.extension == "kt") {
            val relativePath = file.parentFile.relativeTo(ktDir).path
            val targetDir = if (relativePath.isEmpty()) pyDir else File(pyDir, relativePath)
            targetDir.mkdirs()

            val pythonFileName = file.nameWithoutExtension.toSnakeCase() + ".py"
            val targetFile = File(targetDir, pythonFileName)

            val currentModule =
                if (relativePath.isEmpty()) {
                    pythonPackagePrefix + "." + file.nameWithoutExtension.toSnakeCase()
                } else {
                    pythonPackagePrefix + "." +
                        relativePath.replace(
                            File.separator,
                            ".",
                        ) + "." + file.nameWithoutExtension.toSnakeCase()
                }

            println("Converting ${file.path} -> ${targetFile.path}")
            val pythonContent = convertKotlinToPython(file, currentModule, classMap)
            targetFile.writeText(pythonContent)

            val initFile = File(targetDir, "__init__.py")
            if (!initFile.exists()) {
                initFile.writeText("")
            }
        }
    }
}

fun convertKotlinToPython(
    file: File,
    currentModule: String,
    classMap: Map<String, String>,
): String {
    val content = file.readText()
    val lines = content.lines()
    val imports = mutableSetOf<String>()
    imports.add("from __future__ import annotations")
    val result = StringBuilder()

    var braceDepth = 0
    var inClass = false
    var currentClassType: String? = null
    val classesInFile = mutableSetOf<String>()

    Regex("""(?:enum|data|abstract)\s+class\s+(\w+)""").findAll(content).forEach { classesInFile.add(it.groupValues[1]) }
    Regex("""interface\s+(\w+)""").findAll(content).forEach { classesInFile.add(it.groupValues[1]) }

    lines.forEach { line ->
        var trimmed = line.trim()
        if (trimmed.contains("//")) {
            trimmed = trimmed.substringBefore("//").trim()
        }
        if (trimmed.isEmpty()) return@forEach

        if (trimmed.startsWith("package ")) return@forEach
        if (trimmed.startsWith("import ")) return@forEach
        if (trimmed.startsWith("@Serializable")) return@forEach
        if (trimmed.startsWith("@Transient")) return@forEach

        val enumMatch = Regex("""enum\s+class\s+(\w+)\((.*?)\)\s*\{""").find(trimmed)
        if (enumMatch != null) {
            inClass = true
            braceDepth = 1
            currentClassType = "enum"
            val className = enumMatch.groupValues[1]
            val constructorParams = enumMatch.groupValues[2]

            imports.add("from enum import Enum")
            val firstParam = constructorParams.split(",").firstOrNull()?.trim()
            if (firstParam != null && (firstParam.contains(": Int") || firstParam.contains(": Long"))) {
                imports.add("from enum import IntEnum")
                result.append("class $className(IntEnum):\n")
            } else {
                result.append("class $className(str, Enum):\n")
            }
            return@forEach
        }

        if (trimmed.startsWith("data class") && trimmed.contains("(")) {
            val name = trimmed.substringAfter("data class ").substringBefore("(").trim()

            // Search for inheritance in the full content for this class
            // Find where this data class declaration ends (at the matching parenthesis or brace)
            val startIndex = content.indexOf(trimmed)
            var braceCount = 0
            var parenCount = 0
            var foundEnd = false
            var endIdx = startIndex

            for (i in startIndex until content.length) {
                if (content[i] == '(') parenCount++
                if (content[i] == ')') parenCount--
                if (content[i] == '{') {
                    braceCount++
                    foundEnd = true
                    endIdx = i
                    break
                }
                if (foundEnd) break
            }

            val classDeclPart = content.substring(startIndex, endIdx)
            val declMatch =
                Regex(
                    """data\s+class\s+$name\s*\(.*?\)\s*(?::\s*([^{]+))?""",
                    RegexOption.DOT_MATCHES_ALL,
                ).find(content.substring(startIndex))

            var baseClasses = mutableListOf("BaseModel")
            if (declMatch != null && declMatch.groupValues[1].isNotEmpty()) {
                val basesStr = declMatch.groupValues[1].substringBefore("{").trim()
                val foundBases = basesStr.split(",").map { it.trim().split("(").first().trim() }
                if (foundBases.isNotEmpty()) {
                    baseClasses = foundBases.filter { it.isNotEmpty() }.toMutableList()
                }
            }

            inClass = true
            braceDepth = 0
            currentClassType = "data"
            imports.add("from pydantic import BaseModel, Field, ConfigDict")
            imports.add("from typing import Optional, List, Dict, Any, Union")

            baseClasses.forEach { baseClass ->
                if (baseClass != "BaseModel" && !classesInFile.contains(baseClass)) {
                    val module = classMap[baseClass]
                    if (module != null && module != currentModule) {
                        imports.add("from $module import $baseClass")
                    }
                }
            }

            result.append("class $name(${baseClasses.joinToString(", ")}):\n")
            result.append("    model_config = ConfigDict(populate_by_name=True)\n")
            return@forEach
        }

        val interfaceMatch = Regex("""(?:interface|abstract\s+class)\s+(\w+)\s*\{""").find(trimmed)
        if (interfaceMatch != null) {
            inClass = true
            braceDepth = 1
            currentClassType = "interface"
            val className = interfaceMatch.groupValues[1]
            imports.add("from pydantic import BaseModel")
            imports.add("from typing import Optional, List, Dict, Any, Union")
            result.append("class $className(BaseModel):\n")
            return@forEach
        }

        if (inClass) {
            if (trimmed.endsWith("{")) braceDepth++
            if (trimmed.startsWith("}")) braceDepth--

            if (braceDepth < 0) {
                inClass = false
                result.append("\n")
                return@forEach
            }

            val isClassLevel = (currentClassType == "data" && braceDepth == 0) || (braceDepth == 1)

            if (isClassLevel) {
                if (currentClassType == "enum") {
                    if (trimmed.startsWith("@SerialName")) return@forEach
                    val entryMatch = Regex("""(\w+)\((.*?)\),?""").find(trimmed)
                    if (entryMatch != null) {
                        val name = entryMatch.groupValues[1]
                        val args = entryMatch.groupValues[2].split(",").map { it.trim() }
                        val value = args.firstOrNull() ?: "\"$name\""
                        result.append("    $name = $value\n")
                    }
                } else {
                    var fieldLine = trimmed
                    var alias: String? = null
                    val serialNameMatch = Regex("""@SerialName\("(.*?)"\)""").find(fieldLine)
                    if (serialNameMatch != null) {
                        alias = serialNameMatch.groupValues[1]
                        fieldLine = fieldLine.replace(serialNameMatch.value, "").trim()
                    }

                    if (fieldLine.startsWith("fun ") || fieldLine.contains("fun <")) return@forEach

                    val fieldMatch =
                        Regex("""(?:override\s+)?(?:val|var)\s+(\w+)\s*:\s*(.*?)(?:\s*=\s*(.*))?$""").find(fieldLine)
                    if (fieldMatch != null) {
                        val name = fieldMatch.groupValues[1]
                        var rawType = fieldMatch.groupValues[2].trim()
                        var rawDefault = fieldMatch.groupValues[3].trim()

                        if (rawType.contains("=")) {
                            rawDefault = rawType.substringAfter("=").trim()
                            rawType = rawType.substringBefore("=").trim()
                        }

                        rawType = rawType.removeSuffix(",")
                        rawDefault = rawDefault.removeSuffix(",")

                        val type = mapKotlinType(rawType, imports, classMap, currentModule, classesInFile)
                        val defaultValue = mapDefaultValue(rawDefault, type)

                        result.append("    $name: $type")
                        if (alias != null || defaultValue != "None") {
                            result.append(" = Field(")
                            if (defaultValue != "None") {
                                result.append("default=$defaultValue")
                                if (alias != null) result.append(", ")
                            }
                            if (alias != null) {
                                result.append("alias=\"$alias\"")
                            }
                            result.append(")")
                        } else if (type.startsWith("Optional[")) {
                            result.append(" = None")
                        }
                        result.append("\n")
                    }
                }
            }

            if (trimmed == "}" && braceDepth == 0) {
                inClass = false
                result.append("\n")
            }
        }
    }

    val finalResult = StringBuilder()
    imports.sorted().forEach { finalResult.append(it).append("\n") }
    if (imports.isNotEmpty()) finalResult.append("\n\n")
    finalResult.append(result)

    return finalResult.toString()
}

fun mapKotlinType(
    ktType: String,
    imports: MutableSet<String>,
    classMap: Map<String, String>,
    currentModule: String,
    classesInFile: Set<String>,
): String {
    val baseType = ktType.removeSuffix("?").trim()
    val isNullable = ktType.endsWith("?")

    val pyType =
        when {
            baseType == "String" -> "str"
            baseType == "Int" -> "int"
            baseType == "Long" -> "int"
            baseType == "Boolean" -> "bool"
            baseType == "Double" -> "float"
            baseType == "Float" -> "float"
            baseType.startsWith("List<") -> {
                val innerType = baseType.substringAfter("<").substringBeforeLast(">")
                "List[${mapKotlinType(innerType, imports, classMap, currentModule, classesInFile)}]"
            }

            baseType.startsWith("Map<") -> {
                val inner = baseType.substringAfter("<").substringBeforeLast(">")
                var angleBrackets = 0
                var splitIdx = -1
                for (i in inner.indices) {
                    if (inner[i] == '<') {
                        angleBrackets++
                    } else if (inner[i] == '>') {
                        angleBrackets--
                    } else if (inner[i] == ',' && angleBrackets == 0) {
                        splitIdx = i
                        break
                    }
                }
                if (splitIdx != -1) {
                    val keyType =
                        mapKotlinType(inner.substring(0, splitIdx).trim(), imports, classMap, currentModule, classesInFile)
                    val valueType =
                        mapKotlinType(inner.substring(splitIdx + 1).trim(), imports, classMap, currentModule, classesInFile)
                    "Dict[$keyType, $valueType]"
                } else {
                    "Dict[Any, Any]"
                }
            }

            else -> {
                if (!classesInFile.contains(baseType)) {
                    val module = classMap[baseType]
                    if (module != null && module != currentModule) {
                        imports.add("from $module import $baseType")
                    }
                }
                baseType
            }
        }

    return if (isNullable) "Optional[$pyType]" else pyType
}

fun mapDefaultValue(
    ktValue: String,
    pyType: String,
): String {
    if (ktValue.isEmpty()) return "None"
    return when {
        ktValue == "emptyList()" -> "[]"
        ktValue == "emptyMap()" -> "{}"
        ktValue == "null" -> "None"
        ktValue == "0L" -> "0"
        ktValue == "true" -> "True"
        ktValue == "false" -> "False"
        else -> ktValue
    }
}

fun String.toSnakeCase(): String {
    return this.replace(Regex("([a-z])([A-Z])"), "$1_$2").lowercase()
}
