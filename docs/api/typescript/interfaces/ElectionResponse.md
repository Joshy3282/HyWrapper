[hywrapper-ts](../README.md) / [Exports](../modules.md) / ElectionResponse

# Interface: ElectionResponse

Information about the current election and next election.

## Hierarchy

- [`HypixelResponse`](HypixelResponse.md)

  ↳ **`ElectionResponse`**

## Table of contents

### Properties

- [cause](ElectionResponse.md#cause)
- [current](ElectionResponse.md#current)
- [lastUpdated](ElectionResponse.md#lastupdated)
- [mayor](ElectionResponse.md#mayor)
- [rateLimit](ElectionResponse.md#ratelimit)
- [success](ElectionResponse.md#success)

## Properties

### cause

• `Optional` **cause**: `string`

#### Inherited from

[HypixelResponse](HypixelResponse.md).[cause](HypixelResponse.md#cause)

#### Defined in

src/types.ts:92

___

### current

• `Optional` **current**: [`Election`](Election.md)

Information about the next election.

#### Defined in

src/models/skyblock/ElectionResponse.ts:12

___

### lastUpdated

• `Optional` **lastUpdated**: `number`

Timestamp of when the information was last updated.

#### Defined in

src/models/skyblock/ElectionResponse.ts:8

___

### mayor

• `Optional` **mayor**: [`Mayor`](Mayor.md)

Information about the current mayor and election results.

#### Defined in

src/models/skyblock/ElectionResponse.ts:10

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
