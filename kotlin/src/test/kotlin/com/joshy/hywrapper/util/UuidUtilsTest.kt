package com.joshy.hywrapper.util

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertFalse
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test

class UuidUtilsTest {
    private val dashed = "550e8400-e29b-41d4-a716-446655440000"
    private val undashed = "550e8400e29b41d4a716446655440000"

    @Test
    fun testUndash() {
        assertEquals(undashed, UuidUtils.undash(dashed))
        assertEquals(undashed, UuidUtils.undash(undashed))
    }

    @Test
    fun testDash() {
        assertEquals(dashed, UuidUtils.dash(undashed))
        assertEquals(dashed, UuidUtils.dash(dashed))
    }

    @Test
    fun testIsValid() {
        assertTrue(UuidUtils.isValid(dashed))
        assertTrue(UuidUtils.isValid(undashed))
        assertFalse(UuidUtils.isValid("invalid-uuid"))
        assertFalse(UuidUtils.isValid("550e8400-e29b-41d4-a716-44665544000g")) // invalid hex
    }
}
