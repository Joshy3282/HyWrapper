[hywrapper-ts](../README.md) / [Exports](../modules.md) / GuildsAchievementsResponse

# Interface: GuildsAchievementsResponse

## Hierarchy

- [`HypixelResponse`](HypixelResponse.md)

  ↳ **`GuildsAchievementsResponse`**

## Table of contents

### Properties

- [cause](GuildsAchievementsResponse.md#cause)
- [lastUpdated](GuildsAchievementsResponse.md#lastupdated)
- [one\_time](GuildsAchievementsResponse.md#one_time)
- [rateLimit](GuildsAchievementsResponse.md#ratelimit)
- [success](GuildsAchievementsResponse.md#success)
- [tiered](GuildsAchievementsResponse.md#tiered)

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

#### Defined in

src/models/resources/GuildsAchievementsResponse.ts:4

___

### one\_time

• `Optional` **one\_time**: `Record`\<`string`, [`GuildOneTimeAchievement`](GuildOneTimeAchievement.md)\>

#### Defined in

src/models/resources/GuildsAchievementsResponse.ts:5

___

### rateLimit

• `Optional` **rateLimit**: [`RateLimit`](RateLimit.md)

#### Inherited from

[HypixelResponse](HypixelResponse.md).[rateLimit](HypixelResponse.md#ratelimit)

#### Defined in

src/types.ts:93

___

### success

• `Optional` **success**: `boolean`

#### Inherited from

[HypixelResponse](HypixelResponse.md).[success](HypixelResponse.md#success)

#### Defined in

src/types.ts:91

___

### tiered

• `Optional` **tiered**: `Record`\<`string`, [`GuildTieredAchievement`](GuildTieredAchievement.md)\>

#### Defined in

src/models/resources/GuildsAchievementsResponse.ts:6
