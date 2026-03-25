[hywrapper-ts](../README.md) / [Exports](../modules.md) / HousingHousesResponse

# Interface: HousingHousesResponse

List of a player's houses.

## Hierarchy

- [`HypixelResponse`](HypixelResponse.md)

  ↳ **`HousingHousesResponse`**

## Table of contents

### Properties

- [cause](HousingHousesResponse.md#cause)
- [houses](HousingHousesResponse.md#houses)
- [rateLimit](HousingHousesResponse.md#ratelimit)
- [success](HousingHousesResponse.md#success)

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

A list of [House](House.md) belonging to the player.

#### Defined in

src/models/housing/HousingResponses.ts:70

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
