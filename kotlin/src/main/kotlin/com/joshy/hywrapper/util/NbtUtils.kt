package com.joshy.hywrapper.util

import net.querz.nbt.io.NBTDeserializer
import net.querz.nbt.tag.CompoundTag
import java.io.ByteArrayInputStream
import java.util.Base64
import java.util.zip.GZIPInputStream

object NbtUtils {
    fun decodeInventoryData(base64Encoded: String): ByteArray {
        val cleanedBase64 = unescapeUnicode(base64Encoded)
        val decodedBytes = Base64.getDecoder().decode(cleanedBase64)
        return decompressGzip(decodedBytes)
    }

    fun parseCompoundTag(base64Encoded: String): CompoundTag {
        val rawNbt = decodeInventoryData(base64Encoded)
        return NBTDeserializer(false).fromStream(ByteArrayInputStream(rawNbt)).tag as CompoundTag
    }

    private fun unescapeUnicode(input: String): String {
        if (!input.contains("\\u")) return input

        val regex = Regex("\\\\u([0-9a-fA-F]{4})")
        return regex.replace(input) { matchResult ->
            val charCode = matchResult.groupValues[1].toInt(16)
            charCode.toChar().toString()
        }
    }

    private fun decompressGzip(compressed: ByteArray): ByteArray {
        GZIPInputStream(ByteArrayInputStream(compressed)).use { gzipIn ->
            return gzipIn.readAllBytes()
        }
    }
}
