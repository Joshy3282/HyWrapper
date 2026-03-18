package com.joshy.hywrapper.data.skyblock

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertNotNull
import org.junit.jupiter.api.Test

class BazaarItemTest {
    @Test
    fun testFromId() {
        assertEquals(BazaarItem.COCOA_BEANS, BazaarItem.fromId("INK_SACK:3"))
        assertEquals(BazaarItem.TARANTULA_WEB, BazaarItem.fromId("TARANTULA_WEB"))
    }

    @Test
    fun testEnumConsistency() {
        assertNotNull(BazaarItem.entries)

        assertNotNull(BazaarItem.valueOf("OAK_LOG"))
        assertNotNull(BazaarItem.valueOf("COCOA_BEANS"))
    }
}
