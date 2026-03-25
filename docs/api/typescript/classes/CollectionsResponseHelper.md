[hywrapper-ts](../README.md) / [Exports](../modules.md) / CollectionsResponseHelper

# Class: CollectionsResponseHelper

Helper class to provide methods similar to the Kotlin version.

## Table of contents

### Constructors

- [constructor](CollectionsResponseHelper.md#constructor)

### Methods

- [getCollection](CollectionsResponseHelper.md#getcollection)

## Constructors

### constructor

• **new CollectionsResponseHelper**(): [`CollectionsResponseHelper`](CollectionsResponseHelper.md)

#### Returns

[`CollectionsResponseHelper`](CollectionsResponseHelper.md)

## Methods

### getCollection

▸ **getCollection**(`response`, `skill`): `undefined` \| [`Collection`](../interfaces/Collection.md)

Retrieves a collection from the collections response by skill type.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `response` | [`CollectionsResponse`](../interfaces/CollectionsResponse.md) | The collections response. |
| `skill` | [`SkillType`](../enums/SkillType.md) | The skill type. |

#### Returns

`undefined` \| [`Collection`](../interfaces/Collection.md)

The collection data, or undefined if not found.

#### Defined in

src/models/skyblock/CollectionsResponse.ts:38
