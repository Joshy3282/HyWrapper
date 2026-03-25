[hywrapper-ts](../README.md) / [Exports](../modules.md) / Mayor

# Interface: Mayor

Information about the current Mayor.

## Table of contents

### Properties

- [election](Mayor.md#election)
- [key](Mayor.md#key)
- [minister](Mayor.md#minister)
- [name](Mayor.md#name)
- [perks](Mayor.md#perks)

## Properties

### election

• `Optional` **election**: [`Election`](Election.md)

Information about the past election.

#### Defined in

src/models/skyblock/ElectionResponse.ts:28

___

### key

• `Optional` **key**: `string`

Type of mayor (eg; economist {Diaz}, farming {Finnegan}).

#### Defined in

src/models/skyblock/ElectionResponse.ts:20

___

### minister

• `Optional` **minister**: [`Minister`](Minister.md)

Information about the current Minister.

#### Defined in

src/models/skyblock/ElectionResponse.ts:26

___

### name

• `Optional` **name**: `string`

Name of the mayor.

#### Defined in

src/models/skyblock/ElectionResponse.ts:22

___

### perks

• `Optional` **perks**: [`Perk`](Perk.md)[]

A list of the current mayor's perks.

#### Defined in

src/models/skyblock/ElectionResponse.ts:24
