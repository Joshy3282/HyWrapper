package com.joshy.hywrapper.data.skyblock

import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class SkillTypeTest {
    @Test
    fun testProperties() {
        assertEquals("Farming", SkillType.FARMING.cleanName)
        assertEquals("Mining", SkillType.MINING.cleanName)
    }

    @Test
    fun testSerialization() {
        val json = Json.encodeToString(SkillType.FARMING)
        assertEquals("\"FARMING\"", json)
    }

    @Test
    fun testDeserialization() {
        val skill = Json.decodeFromString<SkillType>("\"MINING\"")
        assertEquals(SkillType.MINING, skill)
    }
}
