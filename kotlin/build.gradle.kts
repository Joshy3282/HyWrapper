val serializationVersion: String by project
val okhttpVersion: String by project
val coroutinesVersion: String by project
val junitVersion: String by project
val nbtVersion: String by project

plugins {
    kotlin("jvm")
    kotlin("plugin.serialization")
    id("java")
    `maven-publish`
    id("application")
}

configure<JavaApplication> {
    mainClass.set("com.joshy.hywrapper.util.PythonModelGeneratorKt")
}

group = "com.joshy"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
    maven { url = uri("https://jitpack.io") }
}

dependencies {
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:$serializationVersion")
    implementation("com.squareup.okhttp3:okhttp:$okhttpVersion")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:$coroutinesVersion")
    implementation("com.github.Querz:NBT:$nbtVersion")

    testImplementation(kotlin("test"))
    testImplementation(platform("org.junit:junit-bom:$junitVersion"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")

    testImplementation("com.squareup.okhttp3:mockwebserver:$okhttpVersion")
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(21)
}
