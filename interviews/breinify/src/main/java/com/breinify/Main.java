package com.breinify;

import com.breinify.consumer.DataConsumer;
import com.breinify.service.AnalyticsService;
import com.breinify.storage.IDataStorage;
import com.breinify.storage.InMemoryDataStorage;
import com.google.gson.Gson;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

/*
 * No modification to this class is required
 */
public class Main {

    private static DataConsumer consumer;
    private static IDataStorage storage;
    private static AnalyticsService service;

    public static void main(final String[] args) throws IOException {
        // Initialize the data consumer
        storage = new InMemoryDataStorage();
        consumer = new DataConsumer(storage);
        service = new AnalyticsService(storage);

        // Begin generating data and feeding consumer
        generateData();

        // Start up HTTP
        HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
        server.createContext("/count", new TotalCountHandler());
        server.createContext("/countPerMinute", new CountPerMinuteHandler());
        server.setExecutor(null);
        server.start();
    }

    protected static void generateData() {
        /*
         * Note: feel free to play around with how mocked data is generated if you want to see some different results
         */
        final List<String> dataTypes = Arrays.asList("checkout", "browse", "saveCart", "irrelevantEvent");
        final Random rand = new Random();
        Executors.newSingleThreadScheduledExecutor().scheduleAtFixedRate(() -> {
            final Map<String, Object> generatedData = new HashMap<>();
            generatedData.put("unixTimestamp", System.currentTimeMillis() / 1000L);
            generatedData.put("type", dataTypes.get(rand.nextInt(dataTypes.size())));
            consumer.consume(generatedData);
        }, 0, 1, TimeUnit.SECONDS);
    }

    static class TotalCountHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            final String type = t.getRequestHeaders().getFirst("type");

            final Map<String, Object> response = service.getTotalCountForType(type);

            final String responseString = new Gson().toJson(response);
            t.sendResponseHeaders(200, responseString.length());
            final OutputStream os = t.getResponseBody();
            os.write(responseString.getBytes());
            os.close();
        }
    }

    static class CountPerMinuteHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            final String type = t.getRequestHeaders().getFirst("type");
            final String startTimeString = t.getRequestHeaders().getFirst("startTimestamp");
            final String endTimeString = t.getRequestHeaders().getFirst("endTimestamp");
            final long startTimestamp = startTimeString == null ? -1 : Long.valueOf(startTimeString);
            final long endTimestamp = endTimeString == null ? -1 : Long.valueOf(endTimeString);

            final Map<String, Object> response = service.getCountPerMinuteForType(type, startTimestamp, endTimestamp);

            final String responseString = new Gson().toJson(response);
            t.sendResponseHeaders(200, responseString.length());
            final OutputStream os = t.getResponseBody();
            os.write(responseString.getBytes());
            os.close();
        }
    }
}
