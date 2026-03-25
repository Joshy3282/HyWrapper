[hywrapper-ts](../README.md) / [Exports](../modules.md) / FiresalesResponse

# Interface: FiresalesResponse

Lists all active SkyBlock fire sales.

## Hierarchy

- [`HypixelResponse`](HypixelResponse.md)

  ↳ **`FiresalesResponse`**

## Table of contents

### Properties

- [cause](FiresalesResponse.md#cause)
- [rateLimit](FiresalesResponse.md#ratelimit)
- [sales](FiresalesResponse.md#sales)
- [success](FiresalesResponse.md#success)

## Properties

### cause

• `Optional` **cause**: `string`

#### Inherited from

[HypixelResponse](HypixelResponse.md).[cause](HypixelResponse.md#cause)

#### Defined in

src/types.ts:92

___

### rateLimit

• `Optional` **rateLimit**: [`RateLimit`](RateLimit.md)

#### Inherited from

[HypixelResponse](HypixelResponse.md).[rateLimit](HypixelResponse.md#ratelimit)

#### Defined in

src/types.ts:93

___

### sales

• `Optional` **sales**: [`Sale`](Sale.md)[]

A list of all active firesales

#### Defined in

src/models/skyblock/FiresalesResponse.ts:8

___

### success

• `Optional` **success**: `boolean`

#### Inherited from

[HypixelResponse](HypixelResponse.md).[success](HypixelResponse.md#success)

#### Defined in

src/types.ts:91
