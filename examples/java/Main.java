package com.joshy.hywrapper.example;

import com.joshy.hywrapper.HypixelClient;
import com.joshy.hywrapper.model.playerdata.Player;
import com.joshy.hywrapper.model.playerdata.PlayerResponse;
import com.joshy.hywrapper.model.skyblock.BazaarResponse;
import com.joshy.hywrapper.model.skyblock.Product;
import kotlinx.coroutines.BuildersKt;
import kotlinx.coroutines.EmptyCoroutineContext;

import java.util.Map;

public class MainJava {
    public static void main(String[] args) {
        String apiKey = System.getenv("HYPIXEL_API_KEY") != null
                ? System.getenv("HYPIXEL_API_KEY")
                : "YOUR_API_KEY";

        HypixelClient client = new HypixelClient(apiKey);

        try {
            PlayerResponse playerResponse = BuildersKt.runBlocking(EmptyCoroutineContext.INSTANCE,
                    (scope, continuation) -> client.getPlayer("f7c77398-6623-4a31-8c7a-bc0c56b9d28e", continuation));

            Player player = playerResponse.getPlayer();
            if (player != null) {
                System.out.println("Player Name: " + player.getDisplayname());
                System.out.println("Network Level: " + player.getNetworkExp());
                System.out.println("Karma: " + player.getKarma());
            } else {
                System.out.println("Player not found.");
            }

            BazaarResponse bazaar = BuildersKt.runBlocking(EmptyCoroutineContext.INSTANCE,
                    (scope, continuation) -> client.getBazaar(continuation));

            Map<String, Product> products = bazaar.getProducts();
            int productCount = products != null ? products.size() : 0;
            System.out.println("Total Bazaar Products: " + productCount);

            if (products != null) {
                products.keySet().stream().limit(5).forEach(productId -> {
                    Product product = products.get(productId);
                    System.out.println("- " + productId + ": Buy Price " + product.getQuickStatus().getBuyPrice());
                });
            }

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
