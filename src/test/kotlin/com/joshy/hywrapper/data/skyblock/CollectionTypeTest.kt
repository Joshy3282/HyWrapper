package com.joshy.hywrapper.data.skyblock

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class CollectionTypeTest {
    @Test
    fun testFromId() {
        assertEquals(CollectionType.COCOA_BEANS, CollectionType.fromId("INK_SACK:3"))
        assertEquals(CollectionType.CARROT, CollectionType.fromId("CARROT_ITEM"))
    }

    @Test
    fun testProperties() {
        assertEquals("INK_SACK:3", CollectionType.COCOA_BEANS.id)
        assertEquals("Cocoa Beans", CollectionType.COCOA_BEANS.itemName)
    }
}
