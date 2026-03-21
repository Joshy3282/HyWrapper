# Installation

HyWrapper is available for both Python and JVM-based languages.

## Python Installation

HyWrapper is available on PyPI. You can install it using `pip`:

```bash
pip install hywrapper
```

Or with `uv`:

```bash
uv add hywrapper
```

## Kotlin/Java Installation

HyWrapper is available on Maven Central.

### Gradle (Kotlin)

Add the dependency to your `build.gradle.kts`:

```kotlin
dependencies {
    implementation("com.joshy:hywrapper:0.1.2")
}
```

### Gradle (Groovy)

Add the dependency to your `build.gradle`:

```groovy
dependencies {
    implementation 'com.joshy:hywrapper:0.1.2'
}
```

### Maven

Add the dependency to your `pom.xml`:

```xml
<dependency>
    <groupId>com.joshy</groupId>
    <artifactId>hywrapper</artifactId>
    <version>0.1.2</version>
</dependency>
```
