[hywrapper-ts](../README.md) / [Exports](../modules.md) / BazaarResponseHelper

# Class: BazaarResponseHelper

Helper class to provide methods similar to the Kotlin version.

## Table of contents

### Constructors

- [constructor](BazaarResponseHelper.md#constructor)

### Methods

- [getProduct](BazaarResponseHelper.md#getproduct)

## Constructors

### constructor

• **new BazaarResponseHelper**(): [`BazaarResponseHelper`](BazaarResponseHelper.md)

#### Returns

[`BazaarResponseHelper`](BazaarResponseHelper.md)

## Methods

### getProduct

▸ **getProduct**(`response`, `item`): `undefined` \| [`Product`](../interfaces/Product.md)

Retrieves a product from the bazaar response by item ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `response` | [`BazaarResponse`](../interfaces/BazaarResponse.md) | The bazaar response. |
| `item` | [`BazaarItem`](../enums/BazaarItem.md) | The bazaar item. |

#### Returns

`undefined` \| [`Product`](../interfaces/Product.md)

The product data, or undefined if not found.

#### Defined in

src/models/skyblock/BazaarResponse.ts:45
