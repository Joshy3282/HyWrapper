[hywrapper-ts](../README.md) / [Exports](../modules.md) / SkillsResponse

# Interface: SkillsResponse

Lists information about skills.

## Hierarchy

- [`HypixelResponse`](HypixelResponse.md)

  ↳ **`SkillsResponse`**

## Table of contents

### Properties

- [cause](SkillsResponse.md#cause)
- [lastUpdated](SkillsResponse.md#lastupdated)
- [rateLimit](SkillsResponse.md#ratelimit)
- [skills](SkillsResponse.md#skills)
- [success](SkillsResponse.md#success)
- [version](SkillsResponse.md#version)

## Properties

### cause

• `Optional` **cause**: `string`

#### Inherited from

[HypixelResponse](HypixelResponse.md).[cause](HypixelResponse.md#cause)

#### Defined in

src/types.ts:92

___

### lastUpdated

• `Optional` **lastUpdated**: `number`

The timestamp skills was last updated.

#### Defined in

src/models/skyblock/SkillsResponse.ts:11

___

### rateLimit

• `Optional` **rateLimit**: [`RateLimit`](RateLimit.md)

#### Inherited from

[HypixelResponse](HypixelResponse.md).[rateLimit](HypixelResponse.md#ratelimit)

#### Defined in

src/types.ts:93

___

### skills

• `Optional` **skills**: `Record`\<[`SkillType`](../enums/SkillType.md), [`Skill`](Skill.md)\>

A list of [SkillType](../enums/SkillType.md) containing information.

#### Defined in

src/models/skyblock/SkillsResponse.ts:19

___

### success

• `Optional` **success**: `boolean`

#### Inherited from

[HypixelResponse](HypixelResponse.md).[success](HypixelResponse.md#success)

#### Defined in

src/types.ts:91

___

### version

• `Optional` **version**: `string`

SkyBlocks current version.

#### Defined in

src/models/skyblock/SkillsResponse.ts:15
