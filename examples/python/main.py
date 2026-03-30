import asyncio
import os
from hywrapper import HypixelClient

async def main():
    api_key = os.getenv('HYPIXEL_API_KEY', 'YOUR_API_KEY')
    client = HypixelClient(api_key)

    try:
        player_response = await client.get_player('ac29411d0826412f98c0dd14b334c1fa')
        player = player_response.player
        
        if player:
            print(f'Player Name: {player.displayname}')
            print(f'Network Level: {player.network_exp}')
            print(f'Karma: {player.karma}')
        else:
            print('Player not found.')

        bazaar = await client.get_bazaar()
        products = bazaar.products or {}
        print(f'Total Bazaar Products: {len(products)}')

        for product_id in list(products.keys())[:5]:
            product = products[product_id]
            print(f'- {product_id}: Buy Price {product.quick_status.buy_price}')

    except Exception as e:
        print(f'Error: {e}')
    finally:
        await client.close()

if __name__ == '__main__':
    asyncio.run(main())
