[hywrapper-ts](../README.md) / [Exports](../modules.md) / LeaderboardsResponse

# Interface: LeaderboardsResponse

## Hierarchy

- [`HypixelResponse`](HypixelResponse.md)

  ↳ **`LeaderboardsResponse`**

## Table of contents

### Properties

- [cause](LeaderboardsResponse.md#cause)
- [leaderboards](LeaderboardsResponse.md#leaderboards)
- [rateLimit](LeaderboardsResponse.md#ratelimit)
- [success](LeaderboardsResponse.md#success)

## Properties

### cause

• `Optional` **cause**: `string`

#### Inherited from

[HypixelResponse](HypixelResponse.md).[cause](HypixelResponse.md#cause)

#### Defined in

src/types.ts:92

___

### leaderboards

• `Optional` **leaderboards**: `Record`\<`string`, [`Leaderboard`](Leaderboard.md)[]\>

#### Defined in

src/models/other/LeaderboardsResponse.ts:4

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
