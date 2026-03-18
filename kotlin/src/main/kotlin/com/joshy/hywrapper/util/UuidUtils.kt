package com.joshy.hywrapper.util

object UuidUtils {
    fun undash(uuid: String): String {
        return uuid.replace("-", "").lowercase()
    }

    fun dash(uuid: String): String {
        val undashed = undash(uuid)
        if (undashed.length != 32) return uuid

        return buildString {
            append(undashed.substring(0, 8))
            append("-")
            append(undashed.substring(8, 12))
            append("-")
            append(undashed.substring(12, 16))
            append("-")
            append(undashed.substring(16, 20))
            append("-")
            append(undashed.substring(20, 32))
        }
    }

    fun isValid(uuid: String): Boolean {
        val undashed = undash(uuid)
        return undashed.length == 32 && undashed.all { it in '0'..'9' || it in 'a'..'f' }
    }
}
