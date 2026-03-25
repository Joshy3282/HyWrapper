[hywrapper-ts](../README.md) / [Exports](../modules.md) / Skill

# Interface: Skill

Information about a skill

## Table of contents

### Properties

- [description](Skill.md#description)
- [levels](Skill.md#levels)
- [maxLevel](Skill.md#maxlevel)
- [name](Skill.md#name)

## Properties

### description

• `Optional` **description**: `string`

The skill's description

#### Defined in

src/models/skyblock/SkillsResponse.ts:33

___

### levels

• `Optional` **levels**: [`Level`](Level.md)[]

A list of information and rewards about each level for a skill

#### Defined in

src/models/skyblock/SkillsResponse.ts:41

___

### maxLevel

• `Optional` **maxLevel**: `number`

Maximum level possible for the skill, including level cap increases.

#### Defined in

src/models/skyblock/SkillsResponse.ts:37

___

### name

• `Optional` **name**: `string`

The name of the skill (eg; Farming, Mining)

#### Defined in

src/models/skyblock/SkillsResponse.ts:29
