package com.joshy.hywrapper.util

import net.querz.nbt.io.NBTSerializer
import net.querz.nbt.io.NamedTag
import net.querz.nbt.tag.CompoundTag
import net.querz.nbt.tag.ListTag
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test
import java.io.ByteArrayOutputStream
import java.util.Base64
import java.util.zip.GZIPOutputStream

class NbtUtilsTest {
    @Test
    fun testDecodeAndParse() {
        val compound = CompoundTag()
        compound.putString("test", "hello")

        val list = ListTag(CompoundTag::class.java)
        val item = CompoundTag()
        item.putInt("id", 1)
        list.add(item)
        compound.put("items", list)

        val baos = ByteArrayOutputStream()
        GZIPOutputStream(baos).use { gzip ->
            NBTSerializer(false).toStream(NamedTag("", compound), gzip)
        }
        val compressed = baos.toByteArray()
        val base64 = Base64.getEncoder().encodeToString(compressed)

        val parsed = NbtUtils.parseCompoundTag(base64)

        assertEquals("hello", parsed.getString("test"))
        @Suppress("UNCHECKED_CAST")
        assertEquals(1, (parsed.getListTag("items") as ListTag<CompoundTag>)[0].getInt("id"))
    }

    @Test
    fun testUnescapeUnicode() {
        val baos = ByteArrayOutputStream()
        GZIPOutputStream(baos).use { gzip ->
            gzip.write("Hello".toByteArray())
        }
        val compressed = baos.toByteArray()
        val base64 = Base64.getEncoder().encodeToString(compressed)

        val escapedBase64 =
            if (base64.contains("=")) {
                base64.replace("=", "\\u003d")
            } else {
                "$base64\\u003d"
            }

        try {
            val result = NbtUtils.decodeInventoryData(escapedBase64)
            if (base64.contains("=")) {
                assertEquals("Hello", String(result))
            }
        } catch (e: Exception) {
            if (base64.contains("=")) throw e
        }
    }

    @Test
    fun testDecodeHypixelItemBytes() {
        val itemBytes =
            """
        H4sIAAAAAAAA/2VSTU/bQBAdJ6EkbhHlQnuqtlKrfiDT2Eljw40AAaSUSAROVYXW
        9sSsWO9G6zVq/kRvvXHPtcee81P4EVVPqGNaqag9rGbnvZk3b7TrArTAES4AODWo
        idTxHFja1aWyjgt1yzMHHp6p2CC/5LFEpw6tQ5HiQPKsoKZbF5ZTUUwln7WgMdQG
        m4SuwNpiHh4il/Zimy3myUavDesEHSmLUooMVYIVEXs+PCH8g1BCZWw8RUwrvLfh
        t+HpX2KgjS0V/qa68Ixi9JHom+svdPv0J41uvn+tUnLwigoHpZRsjJb1tSqLbTbO
        ubGMFNFQQ/i6/a77Bl7SbVerKzS2YDNdGnbfY1UnlNXQ+cckpZt3Zuj4NJbdJ6uu
        iTbwliKS8qza1H9PZv8TN5jrK0w3yXKVkvvTC1EwYTFnCVcsRmaQtDJMn8PjxXxr
        MZcnOyf7rD8anY7rsJRoSZPCb/0mNI55jrBKRQc6lkLR3toW4MLq/mdr+I61RsSl
        xaJZPTQ8Ohj1h0fH53dK1F2WBL7gadBJMJh4QSdMvG6Qhl4Uoe8l7R73J90giMKt
        BrSsyLGwPJ/Sv7n+OfwRANTgwR7PeYa0C/wCjr4LK1gCAAA=
        """.replace("\\s+".toRegex(), "") // TODO horrible fucking code oh my god
        val parsed = NbtUtils.parseCompoundTag(itemBytes)

        @Suppress("UNCHECKED_CAST")
        val items = parsed.getListTag("i") as ListTag<CompoundTag>
        val firstItem = items[0]
        val tag = firstItem.getCompoundTag("tag")
        val display = tag.getCompoundTag("display")
        val name = display.getString("Name")

        println("Item Name: $name")
        assert(name.isNotEmpty())
    }
}
