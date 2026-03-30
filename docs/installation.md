# Installation

HyWrapper is available for Python, TypeScript, and JVM-based languages (Kotlin/Java).

## Python Installation

HyWrapper is available on PyPI. You can install it using `pip`:

```bash
pip install hywrapper
```

Or with `uv`:

```bash
uv add hywrapper
```

## TypeScript Installation

HyWrapper is available on npm. You can install it using `npm`:

```bash
npm install hywrapper-ts
```

Or with `yarn`:

```bash
yarn add hywrapper-ts
```

## Kotlin/Java Installation

HyWrapper is available on JitPack and Maven Central.

### Gradle (Kotlin)

Add the JitPack repository and the dependency to your `build.gradle.kts`:

```kotlin
repositories {
    mavenCentral()
    maven { url = uri("https://jitpack.io") }
}

dependencies {
    implementation("com.github.Joshy3282:HyWrapper:1.0-SNAPSHOT")
}
```

### Gradle (Groovy)

Add the JitPack repository and the dependency to your `build.gradle`:

```groovy
repositories {
    mavenCentral()
    maven { url "https://jitpack.io" }
}

dependencies {
    implementation 'com.github.Joshy3282:HyWrapper:1.0-SNAPSHOT'
}
```

### Maven

Add the JitPack repository and the dependency to your `pom.xml`:

```xml
<repositories>
    <repository>
        <id>jitpack.io</id>
        <url>https://jitpack.io</url>
    </repository>
</repositories>

<dependency>
    <groupId>com.github.Joshy3282</groupId>
    <artifactId>HyWrapper</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
```
