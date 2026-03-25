[hywrapper-ts](../README.md) / [Exports](../modules.md) / HypixelClient

# Class: HypixelClient

A client for interacting with the Hypixel API.

This client handles authentication, rate limiting, and automatic retries.
It uses Promises for asynchronous requests.

**`Param`**

The Hypixel API key.

**`Param`**

The base URL for the Hypixel API.

**`Param`**

The duration for which successful responses should be cached.

**`Param`**

Whether to automatically retry requests that fail due to rate limiting.

**`Param`**

The maximum number of retries for rate-limited requests.

## Table of contents

### Constructors

- [constructor](HypixelClient.md#constructor)

### Properties

- [\_lastRateLimit](HypixelClient.md#_lastratelimit)
- [apiKey](HypixelClient.md#apikey)
- [autoRetry](HypixelClient.md#autoretry)
- [axiosInstance](HypixelClient.md#axiosinstance)
- [baseUrl](HypixelClient.md#baseurl)
- [defaultCacheDurationMinutes](HypixelClient.md#defaultcachedurationminutes)
- [maxRetries](HypixelClient.md#maxretries)

### Accessors

- [lastRateLimit](HypixelClient.md#lastratelimit)

### Methods

- [fetch](HypixelClient.md#fetch)
- [getAchievements](HypixelClient.md#getachievements)
- [getAuction](HypixelClient.md#getauction)
- [getAuctions](HypixelClient.md#getauctions)
- [getAuctionsEnded](HypixelClient.md#getauctionsended)
- [getBazaar](HypixelClient.md#getbazaar)
- [getBingo](HypixelClient.md#getbingo)
- [getBoosters](HypixelClient.md#getboosters)
- [getChallenges](HypixelClient.md#getchallenges)
- [getCollections](HypixelClient.md#getcollections)
- [getCounts](HypixelClient.md#getcounts)
- [getElection](HypixelClient.md#getelection)
- [getFiresales](HypixelClient.md#getfiresales)
- [getGames](HypixelClient.md#getgames)
- [getGarden](HypixelClient.md#getgarden)
- [getGuildAchievements](HypixelClient.md#getguildachievements)
- [getGuildById](HypixelClient.md#getguildbyid)
- [getGuildByName](HypixelClient.md#getguildbyname)
- [getGuildByPlayer](HypixelClient.md#getguildbyplayer)
- [getHousingActive](HypixelClient.md#gethousingactive)
- [getHousingHouse](HypixelClient.md#gethousinghouse)
- [getHousingHouses](HypixelClient.md#gethousinghouses)
- [getItems](HypixelClient.md#getitems)
- [getLeaderboards](HypixelClient.md#getleaderboards)
- [getMuseum](HypixelClient.md#getmuseum)
- [getNews](HypixelClient.md#getnews)
- [getPlayer](HypixelClient.md#getplayer)
- [getPlayerBingo](HypixelClient.md#getplayerbingo)
- [getProfile](HypixelClient.md#getprofile)
- [getProfiles](HypixelClient.md#getprofiles)
- [getPunishmentStats](HypixelClient.md#getpunishmentstats)
- [getQuests](HypixelClient.md#getquests)
- [getRecentGames](HypixelClient.md#getrecentgames)
- [getSkills](HypixelClient.md#getskills)
- [getStatus](HypixelClient.md#getstatus)
- [getVanityCompanions](HypixelClient.md#getvanitycompanions)
- [getVanityPets](HypixelClient.md#getvanitypets)
- [parseRateLimit](HypixelClient.md#parseratelimit)

## Constructors

### constructor

• **new HypixelClient**(`options`): [`HypixelClient`](HypixelClient.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`ClientOptions`](../interfaces/ClientOptions.md) |

#### Returns

[`HypixelClient`](HypixelClient.md)

#### Defined in

src/client.ts:78

## Properties

### \_lastRateLimit

• `Private` **\_lastRateLimit**: ``null`` \| [`RateLimit`](../interfaces/RateLimit.md) = `null`

#### Defined in

src/client.ts:76

___

### apiKey

• `Private` `Readonly` **apiKey**: `string`

#### Defined in

src/client.ts:69

___

### autoRetry

• `Private` `Readonly` **autoRetry**: `boolean`

#### Defined in

src/client.ts:72

___

### axiosInstance

• `Private` `Readonly` **axiosInstance**: `AxiosInstance`

#### Defined in

src/client.ts:74

___

### baseUrl

• `Private` `Readonly` **baseUrl**: `string`

#### Defined in

src/client.ts:70

___

### defaultCacheDurationMinutes

• `Private` `Readonly` **defaultCacheDurationMinutes**: `number`

#### Defined in

src/client.ts:71

___

### maxRetries

• `Private` `Readonly` **maxRetries**: `number`

#### Defined in

src/client.ts:73

## Accessors

### lastRateLimit

• `get` **lastRateLimit**(): ``null`` \| [`RateLimit`](../interfaces/RateLimit.md)

The rate limit information from the last successful API request.

#### Returns

``null`` \| [`RateLimit`](../interfaces/RateLimit.md)

#### Defined in

src/client.ts:104

## Methods

### fetch

▸ **fetch**\<`T`\>(`endpoint`, `params?`, `authenticated?`): `Promise`\<`T`\>

#### Type parameters

| Name | Type |
| :------ | :------ |
| `T` | extends [`HypixelResponse`](../interfaces/HypixelResponse.md) |

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `endpoint` | `string` | `undefined` |
| `params` | `Record`\<`string`, `string`\> | `{}` |
| `authenticated` | `boolean` | `true` |

#### Returns

`Promise`\<`T`\>

#### Defined in

src/client.ts:439

___

### getAchievements

▸ **getAchievements**(): `Promise`\<[`AchievementsResponse`](../interfaces/AchievementsResponse.md)\>

Retrieves the list of achievements.
https://api.hypixel.net/v2/resources/achievements

#### Returns

`Promise`\<[`AchievementsResponse`](../interfaces/AchievementsResponse.md)\>

#### Defined in

src/client.ts:187

___

### getAuction

▸ **getAuction**(`uuid?`, `player?`, `profile?`): `Promise`\<[`AuctionsResponse`](../interfaces/AuctionsResponse.md)\>

Searches for SkyBlock auctions by UUID, player, or profile.
https://api.hypixel.net/v2/skyblock/auction

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `uuid?` | `string` | The auction UUID. |
| `player?` | `string` | The player UUID. |
| `profile?` | `string` | The profile UUID. |

#### Returns

`Promise`\<[`AuctionsResponse`](../interfaces/AuctionsResponse.md)\>

#### Defined in

src/client.ts:287

___

### getAuctions

▸ **getAuctions**(`page?`): `Promise`\<[`AuctionsResponse`](../interfaces/AuctionsResponse.md)\>

Retrieves active SkyBlock auctions.
https://api.hypixel.net/v2/skyblock/auctions

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `page` | `number` | `0` | The page number to get. |

#### Returns

`Promise`\<[`AuctionsResponse`](../interfaces/AuctionsResponse.md)\>

#### Defined in

src/client.ts:301

___

### getAuctionsEnded

▸ **getAuctionsEnded**(): `Promise`\<[`AuctionsEndedResponse`](../interfaces/AuctionsEndedResponse.md)\>

Retrieves recently ended SkyBlock auctions.
https://api.hypixel.net/v2/skyblock/auctions_ended

#### Returns

`Promise`\<[`AuctionsEndedResponse`](../interfaces/AuctionsEndedResponse.md)\>

#### Defined in

src/client.ts:309

___

### getBazaar

▸ **getBazaar**(): `Promise`\<[`BazaarResponse`](../interfaces/BazaarResponse.md)\>

Retrieves current bazaar data.
https://api.hypixel.net/v2/skyblock/bazaar

#### Returns

`Promise`\<[`BazaarResponse`](../interfaces/BazaarResponse.md)\>

#### Defined in

src/client.ts:317

___

### getBingo

▸ **getBingo**(): `Promise`\<[`BingoResponse`](../interfaces/BingoResponse.md)\>

Retrieves the current SkyBlock bingo information.
https://api.hypixel.net/v2/resources/skyblock/bingo

#### Returns

`Promise`\<[`BingoResponse`](../interfaces/BingoResponse.md)\>

#### Defined in

src/client.ts:267

___

### getBoosters

▸ **getBoosters**(): `Promise`\<[`BoostersResponse`](../interfaces/BoostersResponse.md)\>

Retrieves the current boosters.
https://api.hypixel.net/v2/boosters

#### Returns

`Promise`\<[`BoostersResponse`](../interfaces/BoostersResponse.md)\>

#### Defined in

src/client.ts:411

___

### getChallenges

▸ **getChallenges**(): `Promise`\<[`ChallengesResponse`](../interfaces/ChallengesResponse.md)\>

Retrieves the list of challenges.
https://api.hypixel.net/v2/resources/challenges

#### Returns

`Promise`\<[`ChallengesResponse`](../interfaces/ChallengesResponse.md)\>

#### Defined in

src/client.ts:195

___

### getCollections

▸ **getCollections**(): `Promise`\<[`CollectionsResponse`](../interfaces/CollectionsResponse.md)\>

Retrieves the list of SkyBlock collections.
https://api.hypixel.net/v2/resources/skyblock/collections

#### Returns

`Promise`\<[`CollectionsResponse`](../interfaces/CollectionsResponse.md)\>

#### Defined in

src/client.ts:235

___

### getCounts

▸ **getCounts**(): `Promise`\<[`CountsResponse`](../interfaces/CountsResponse.md)\>

Retrieves the player counts across various games.
https://api.hypixel.net/v2/counts

#### Returns

`Promise`\<[`CountsResponse`](../interfaces/CountsResponse.md)\>

#### Defined in

src/client.ts:419

___

### getElection

▸ **getElection**(): `Promise`\<[`ElectionResponse`](../interfaces/ElectionResponse.md)\>

Retrieves the current SkyBlock election information.
https://api.hypixel.net/v2/resources/skyblock/election

#### Returns

`Promise`\<[`ElectionResponse`](../interfaces/ElectionResponse.md)\>

#### Defined in

src/client.ts:259

___

### getFiresales

▸ **getFiresales**(): `Promise`\<[`FiresalesResponse`](../interfaces/FiresalesResponse.md)\>

Retrieves current SkyBlock fire sales.
https://api.hypixel.net/v2/skyblock/firesales

#### Returns

`Promise`\<[`FiresalesResponse`](../interfaces/FiresalesResponse.md)\>

#### Defined in

src/client.ts:375

___

### getGames

▸ **getGames**(): `Promise`\<[`GamesResponse`](../interfaces/GamesResponse.md)\>

Retrieves the list of games.
https://api.hypixel.net/v2/resources/games

#### Returns

`Promise`\<[`GamesResponse`](../interfaces/GamesResponse.md)\>

#### Defined in

src/client.ts:179

___

### getGarden

▸ **getGarden**(`profileUuid`): `Promise`\<[`GardenResponse`](../interfaces/GardenResponse.md)\>

Retrieves SkyBlock garden information for a profile.
https://api.hypixel.net/v2/skyblock/garden

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `profileUuid` | `string` | The UUID of the SkyBlock profile. |

#### Returns

`Promise`\<[`GardenResponse`](../interfaces/GardenResponse.md)\>

#### Defined in

src/client.ts:357

___

### getGuildAchievements

▸ **getGuildAchievements**(): `Promise`\<[`GuildsAchievementsResponse`](../interfaces/GuildsAchievementsResponse.md)\>

Retrieves the list of guild achievements.
https://api.hypixel.net/v2/resources/guilds/achievements

#### Returns

`Promise`\<[`GuildsAchievementsResponse`](../interfaces/GuildsAchievementsResponse.md)\>

#### Defined in

src/client.ts:211

___

### getGuildById

▸ **getGuildById**(`id`): `Promise`\<[`GuildResponse`](../interfaces/GuildResponse.md)\>

Retrieves a guild by an id.
https://api.hypixel.net/v2/guild

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the guild. |

#### Returns

`Promise`\<[`GuildResponse`](../interfaces/GuildResponse.md)\>

A [GuildResponse](../interfaces/GuildResponse.md) containing the guild's data.

#### Defined in

src/client.ts:149

___

### getGuildByName

▸ **getGuildByName**(`name`): `Promise`\<[`GuildResponse`](../interfaces/GuildResponse.md)\>

Retrieves a guild by a name.
https://api.hypixel.net/v2/guild

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | The name of the guild. |

#### Returns

`Promise`\<[`GuildResponse`](../interfaces/GuildResponse.md)\>

A [GuildResponse](../interfaces/GuildResponse.md) containing the guild's data.

#### Defined in

src/client.ts:171

___

### getGuildByPlayer

▸ **getGuildByPlayer**(`uuid`): `Promise`\<[`GuildResponse`](../interfaces/GuildResponse.md)\>

Retrieves a guild by a player.
https://api.hypixel.net/v2/guild

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `uuid` | `string` | The UUID of the player. |

#### Returns

`Promise`\<[`GuildResponse`](../interfaces/GuildResponse.md)\>

A [GuildResponse](../interfaces/GuildResponse.md) containing the guild's data.

#### Defined in

src/client.ts:160

___

### getHousingActive

▸ **getHousingActive**(): `Promise`\<[`HousingActiveResponse`](../interfaces/HousingActiveResponse.md)\>

Retrieves the currently active housing.
https://api.hypixel.net/v2/housing/active

#### Returns

`Promise`\<[`HousingActiveResponse`](../interfaces/HousingActiveResponse.md)\>

#### Defined in

src/client.ts:383

___

### getHousingHouse

▸ **getHousingHouse**(`houseUuid`): `Promise`\<[`HousingHouseResponse`](../interfaces/HousingHouseResponse.md)\>

Retrieves information about a specific housing instance.
https://api.hypixel.net/v2/housing/house

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `houseUuid` | `string` | The UUID of the housing instance. |

#### Returns

`Promise`\<[`HousingHouseResponse`](../interfaces/HousingHouseResponse.md)\>

#### Defined in

src/client.ts:393

___

### getHousingHouses

▸ **getHousingHouses**(`uuid`): `Promise`\<[`HousingHousesResponse`](../interfaces/HousingHousesResponse.md)\>

Retrieves the housing instances owned by a player.
https://api.hypixel.net/v2/housing/houses

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `uuid` | `string` | The UUID of the player. |

#### Returns

`Promise`\<[`HousingHousesResponse`](../interfaces/HousingHousesResponse.md)\>

#### Defined in

src/client.ts:403

___

### getItems

▸ **getItems**(): `Promise`\<[`ItemsResponse`](../interfaces/ItemsResponse.md)\>

Retrieves the list of SkyBlock items.
https://api.hypixel.net/v2/resources/skyblock/items

#### Returns

`Promise`\<[`ItemsResponse`](../interfaces/ItemsResponse.md)\>

#### Defined in

src/client.ts:251

___

### getLeaderboards

▸ **getLeaderboards**(): `Promise`\<[`LeaderboardsResponse`](../interfaces/LeaderboardsResponse.md)\>

Retrieves the current leaderboards.
https://api.hypixel.net/v2/leaderboards

#### Returns

`Promise`\<[`LeaderboardsResponse`](../interfaces/LeaderboardsResponse.md)\>

#### Defined in

src/client.ts:427

___

### getMuseum

▸ **getMuseum**(`profileUuid`): `Promise`\<[`MuseumResponse`](../interfaces/MuseumResponse.md)\>

Retrieves SkyBlock museum information for a profile.
https://api.hypixel.net/v2/skyblock/museum

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `profileUuid` | `string` | The UUID of the SkyBlock profile. |

#### Returns

`Promise`\<[`MuseumResponse`](../interfaces/MuseumResponse.md)\>

#### Defined in

src/client.ts:347

___

### getNews

▸ **getNews**(): `Promise`\<[`NewsResponse`](../interfaces/NewsResponse.md)\>

Retrieves SkyBlock news.
https://api.hypixel.net/v2/skyblock/news

#### Returns

`Promise`\<[`NewsResponse`](../interfaces/NewsResponse.md)\>

#### Defined in

src/client.ts:275

___

### getPlayer

▸ **getPlayer**(`uuid`): `Promise`\<[`PlayerResponse`](../interfaces/PlayerResponse.md)\>

Retrieves data of a specific player, including game stats.
https://api.hypixel.net/v2/player

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `uuid` | `string` | The UUID of the player. |

#### Returns

`Promise`\<[`PlayerResponse`](../interfaces/PlayerResponse.md)\>

A [PlayerResponse](../interfaces/PlayerResponse.md) containing the player's data.

**`Throws`**

HypixelException if the API returns an error.

#### Defined in

src/client.ts:116

___

### getPlayerBingo

▸ **getPlayerBingo**(`uuid`): `Promise`\<[`BingoResponse`](../interfaces/BingoResponse.md)\>

Retrieves SkyBlock bingo data for a player.
https://api.hypixel.net/v2/skyblock/bingo

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `uuid` | `string` | The UUID of the player. |

#### Returns

`Promise`\<[`BingoResponse`](../interfaces/BingoResponse.md)\>

#### Defined in

src/client.ts:367

___

### getProfile

▸ **getProfile**(`uuid`): `Promise`\<[`ProfileResponse`](../interfaces/ProfileResponse.md)\>

Retrieves a specific SkyBlock profile by its UUID.
https://api.hypixel.net/v2/skyblock/profile

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `uuid` | `string` | The UUID of the profile. |

#### Returns

`Promise`\<[`ProfileResponse`](../interfaces/ProfileResponse.md)\>

#### Defined in

src/client.ts:327

___

### getProfiles

▸ **getProfiles**(`uuid`): `Promise`\<[`ProfilesResponse`](../interfaces/ProfilesResponse.md)\>

Retrieves all SkyBlock profiles for a player.
https://api.hypixel.net/v2/skyblock/profiles

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `uuid` | `string` | The UUID of the player. |

#### Returns

`Promise`\<[`ProfilesResponse`](../interfaces/ProfilesResponse.md)\>

#### Defined in

src/client.ts:337

___

### getPunishmentStats

▸ **getPunishmentStats**(): `Promise`\<[`PunishmentStatsResponse`](../interfaces/PunishmentStatsResponse.md)\>

Retrieves punishment statistics.
https://api.hypixel.net/v2/punishmentstats

#### Returns

`Promise`\<[`PunishmentStatsResponse`](../interfaces/PunishmentStatsResponse.md)\>

#### Defined in

src/client.ts:435

___

### getQuests

▸ **getQuests**(): `Promise`\<[`QuestsResponse`](../interfaces/QuestsResponse.md)\>

Retrieves the list of quests.
https://api.hypixel.net/v2/resources/quests

#### Returns

`Promise`\<[`QuestsResponse`](../interfaces/QuestsResponse.md)\>

#### Defined in

src/client.ts:203

___

### getRecentGames

▸ **getRecentGames**(`uuid`): `Promise`\<[`RecentGamesResponse`](../interfaces/RecentGamesResponse.md)\>

Retrieves the recently played games of a specific player.
https://api.hypixel.net/v2/recentgames

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `uuid` | `string` | The UUID of the player. |

#### Returns

`Promise`\<[`RecentGamesResponse`](../interfaces/RecentGamesResponse.md)\>

A [RecentGamesResponse](../interfaces/RecentGamesResponse.md) containing the recent games data.

#### Defined in

src/client.ts:127

___

### getSkills

▸ **getSkills**(): `Promise`\<[`SkillsResponse`](../interfaces/SkillsResponse.md)\>

Retrieves SkyBlock skills information.
https://api.hypixel.net/v2/resources/skyblock/skills

#### Returns

`Promise`\<[`SkillsResponse`](../interfaces/SkillsResponse.md)\>

#### Defined in

src/client.ts:243

___

### getStatus

▸ **getStatus**(`uuid`): `Promise`\<[`OnlineResponse`](../interfaces/OnlineResponse.md)\>

Retrieves the current online status of a specific player.
https://api.hypixel.net/v2/status

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `uuid` | `string` | The UUID of the player. |

#### Returns

`Promise`\<[`OnlineResponse`](../interfaces/OnlineResponse.md)\>

An [OnlineResponse](../interfaces/OnlineResponse.md) containing the player's online status.

#### Defined in

src/client.ts:138

___

### getVanityCompanions

▸ **getVanityCompanions**(): `Promise`\<[`VanityResponse`](../interfaces/VanityResponse.md)\>

Retrieves the list of vanity companions.
https://api.hypixel.net/v2/resources/vanity/companions

#### Returns

`Promise`\<[`VanityResponse`](../interfaces/VanityResponse.md)\>

#### Defined in

src/client.ts:227

___

### getVanityPets

▸ **getVanityPets**(): `Promise`\<[`VanityResponse`](../interfaces/VanityResponse.md)\>

Retrieves the list of vanity pets.
https://api.hypixel.net/v2/resources/vanity/pets

#### Returns

`Promise`\<[`VanityResponse`](../interfaces/VanityResponse.md)\>

#### Defined in

src/client.ts:219

___

### parseRateLimit

▸ **parseRateLimit**(`headers`): ``null`` \| [`RateLimit`](../interfaces/RateLimit.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `headers` | `any` |

#### Returns

``null`` \| [`RateLimit`](../interfaces/RateLimit.md)

#### Defined in

src/client.ts:534
