# HyWrapper - Kotlin/Java Hypixel API Wrapper

An asynchronous and multi-platform Hypixel API wrapper for Kotlin and Java.

## Installation

Add the JitPack repository and the dependency to your `build.gradle.kts`:

```kotlin
repositories {
    maven { url = uri("https://jitpack.io") }
}

dependencies {
    implementation("com.github.joshy3282:hywrapper:1.0.0")
}
```

## Usage

### Kotlin

```kotlin
import com.joshy.hywrapper.HypixelClient
import kotlinx.coroutines.runBlocking

fun main() = runBlocking {
    val client = HypixelClient(apiKey = "your-api-key")
    val response = client.getPlayer("ac29411d0826412f98c0dd14b334c1fa")
    
    if (response.success) {
        println("Player Found: ${response.player?.displayname}")
    }
}
```

## Features

- Coroutines support for asynchronous requests
- Multi-platform support
- Type-safe models with Kotlin Serialization

## Building

To build the project manually using Gradle:

```bash
./gradlew build
```

To install it to your local Maven repository:

```bash
./gradlew publishToMavenLocal
```
