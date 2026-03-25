[hywrapper-ts](../README.md) / [Exports](../modules.md) / CountsResponse

# Interface: CountsResponse

## Hierarchy

- [`HypixelResponse`](HypixelResponse.md)

  ↳ **`CountsResponse`**

## Table of contents

### Properties

- [cause](CountsResponse.md#cause)
- [games](CountsResponse.md#games)
- [playerCount](CountsResponse.md#playercount)
- [rateLimit](CountsResponse.md#ratelimit)
- [success](CountsResponse.md#success)

## Properties

### cause

• `Optional` **cause**: `string`

#### Inherited from

[HypixelResponse](HypixelResponse.md).[cause](HypixelResponse.md#cause)

#### Defined in

src/types.ts:92

___

### games

• `Optional` **games**: `Record`\<`string`, [`GameCount`](GameCount.md)\>

#### Defined in

src/models/other/CountsResponse.ts:4

___

### playerCount

• `Optional` **playerCount**: `number`

#### Defined in

src/models/other/CountsResponse.ts:5

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
