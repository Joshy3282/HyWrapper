[hywrapper-ts](../README.md) / [Exports](../modules.md) / HousingActiveResponse

# Interface: HousingActiveResponse

List of all active Houses.

## Hierarchy

- [`HypixelResponse`](HypixelResponse.md)

  ↳ **`HousingActiveResponse`**

## Table of contents

### Properties

- [cause](HousingActiveResponse.md#cause)
- [houses](HousingActiveResponse.md#houses)
- [rateLimit](HousingActiveResponse.md#ratelimit)
- [success](HousingActiveResponse.md#success)

## Properties

### cause

• `Optional` **cause**: `string`

#### Inherited from

[HypixelResponse](HypixelResponse.md).[cause](HypixelResponse.md#cause)

#### Defined in

src/types.ts:92

___

### houses

• `Optional` **houses**: [`House`](House.md)[]

A list of [House](House.md).

#### Defined in

src/models/housing/HousingResponses.ts:10

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
