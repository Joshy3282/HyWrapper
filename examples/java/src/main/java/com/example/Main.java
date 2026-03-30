package com.example;

import com.joshy.hywrapper.HypixelClient;
import com.joshy.hywrapper.model.playerdata.Player;
import com.joshy.hywrapper.model.playerdata.PlayerResponse;
import com.joshy.hywrapper.model.skyblock.BazaarResponse;
import com.joshy.hywrapper.model.skyblock.Product;
import kotlinx.coroutines.BuildersKt;
import kotlin.coroutines.EmptyCoroutineContext;
import okhttp3.OkHttpClient;

import java.util.Map;

public class Main {
    public static void main(String[] args) {
        String apiKey = System.getenv("HYPIXEL_API_KEY") != null
                ? System.getenv("HYPIXEL_API_KEY")
                : "YOUR_API_KEY";

        HypixelClient client = new HypixelClient(
                apiKey,
                new OkHttpClient(),
                "https://api.hypixel.net/v2",
                1,
                false,
                3
        );

        try {
            PlayerResponse playerResponse = BuildersKt.runBlocking(EmptyCoroutineContext.INSTANCE,
                    (scope, continuation) -> client.getPlayer("ac29411d0826412f98c0dd14b334c1fa", continuation));

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
