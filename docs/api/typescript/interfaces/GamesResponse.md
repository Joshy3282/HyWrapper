[hywrapper-ts](../README.md) / [Exports](../modules.md) / GamesResponse

# Interface: GamesResponse

## Hierarchy

- [`HypixelResponse`](HypixelResponse.md)

  ↳ **`GamesResponse`**

## Table of contents

### Properties

- [cause](GamesResponse.md#cause)
- [games](GamesResponse.md#games)
- [lastUpdated](GamesResponse.md#lastupdated)
- [rateLimit](GamesResponse.md#ratelimit)
- [success](GamesResponse.md#success)

## Properties

### cause

• `Optional` **cause**: `string`

#### Inherited from

[HypixelResponse](HypixelResponse.md).[cause](HypixelResponse.md#cause)

#### Defined in

src/types.ts:92

___

### games

• `Optional` **games**: `Record`\<`string`, [`Game`](Game.md)\>

#### Defined in

src/models/resources/GamesResponse.ts:5

___

### lastUpdated

• `Optional` **lastUpdated**: `number`

#### Defined in

src/models/resources/GamesResponse.ts:4

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
