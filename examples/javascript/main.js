import { HypixelClient } from 'hywrapper';

async function main() {
    const apiKey = process.env.HYPIXEL_API_KEY || 'YOUR_API_KEY';
    const client = new HypixelClient({ api_key: apiKey });

    try {
        const playerResponse = await client.getPlayer('ac29411d0826412f98c0dd14b334c1fa');
        const player = playerResponse.player;

        if (player) {
            console.log(`Player Name: ${player.displayname}`);
            console.log(`Network Level: ${player.networkExp}`);
            console.log(`Karma: ${player.karma}`);
        } else {
            console.log('Player not found.');
        }

        const bazaar = await client.getBazaar();
        const productCount = bazaar.products ? Object.keys(bazaar.products).length : 0;
        console.log(`Total Bazaar Products: ${productCount}`);

        if (bazaar.products) {
            Object.keys(bazaar.products).slice(0, 5).forEach(productId => {
                const product = bazaar.products[productId];
                console.log(`- ${productId}: Buy Price ${product.quick_status.buyPrice}`);
            });
        }

    } catch (error) {
        console.error('Error:', error);
    }
}

main();
