[hywrapper-ts](../README.md) / [Exports](../modules.md) / NewsResponse

# Interface: NewsResponse

Lists all current news entries. These are viewable through Jerry on the island.

## Hierarchy

- [`HypixelResponse`](HypixelResponse.md)

  ↳ **`NewsResponse`**

## Table of contents

### Properties

- [cause](NewsResponse.md#cause)
- [items](NewsResponse.md#items)
- [rateLimit](NewsResponse.md#ratelimit)
- [success](NewsResponse.md#success)

## Properties

### cause

• `Optional` **cause**: `string`

#### Inherited from

[HypixelResponse](HypixelResponse.md).[cause](HypixelResponse.md#cause)

#### Defined in

src/types.ts:92

___

### items

• `Optional` **items**: [`NewsItem`](NewsItem.md)[]

The list of current news' information.

#### Defined in

src/models/skyblock/NewsResponse.ts:8

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
