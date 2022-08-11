package com.breinify.service;

import com.breinify.storage.IDataStorage;
import com.google.common.collect.ImmutableMap;

import java.util.Map;
import java.util.Optional;
import java.util.logging.Logger;

public class AnalyticsService {
    private static final Logger LOG = Logger.getLogger("AnalyticsService");

    private IDataStorage storage;

    public AnalyticsService(final IDataStorage storage) {
        this.storage = storage;
    }


    /**
     * Queries for the total number of events for a given event type.
     * If the event type is invalid, throws an IllegalArgumentException.
     *
     * @param type string representing the event type
     *
     * @return Result describing the total count for the specified event type
     */
    public Map<String, Object> getTotalCountForType(final String type) {
        if (!storage.getUserActionEventStrings().contains(type)) {
            IllegalArgumentException e = new IllegalArgumentException("Event type currently not supported: " + type);
            LOG.severe(e.getMessage());
            throw e;
        }

        return storage.findUserActionEvents(type, Optional.empty(), Optional.empty())
            .map(events -> ImmutableMap.<String, Object>builder()
                .put("event", type)
                .put("numberOfEvents", events.size())
                .build())
            .orElseThrow(() ->
                new RuntimeException("Internal Server Error - could not retrieve total count for event: " + type));
    }


    /**
     * Queries for the number of events per minute given a event type,
     * start timestamp (unix), and end timestamp (unix).
     * If the event type or timestamps values are invalid,
     * throws an IllegalArgumentException.
     *
     * @param type           string representing the Event type
     * @param startTimestamp Unix timestamp of start of time range
     * @param endTimestamp   Unix timestamp of end of time range
     *
     * @return Result describing the count per minute for the specified event type, within the given time range.
     */
    public Map<String, Object> getCountPerMinuteForType(final String type,
                                                        final long startTimestamp,
                                                        final long endTimestamp) {
        if (!storage.getUserActionEventStrings().contains(type)) {
            IllegalArgumentException e = new IllegalArgumentException("Event type currently not supported: " + type);
            LOG.severe(e.getMessage());
            throw e;
        } else if (startTimestamp > endTimestamp) {
            IllegalArgumentException e = new IllegalArgumentException(String.format(
                "Invalid timestamp values: startTimeStamp: %d and endTimestamp: %d", startTimestamp, endTimestamp));
            LOG.severe(e.getMessage());
            throw e;
        }

        return storage.findUserActionEvents(type, Optional.of(startTimestamp), Optional.of(endTimestamp))
            .<ImmutableMap<String, Object>>map(events -> {
                int numberOfEvents = events.size();
                double totalTimeInMinutes = getMinutesBetweenUnixTimestamps(startTimestamp, endTimestamp);
                double countPerMin = totalTimeInMinutes == 0 ? 0 : numberOfEvents/totalTimeInMinutes;

                return ImmutableMap.of(
                        "event", type,
                        "countPerMin", countPerMin,
                        "numberOfEvents", numberOfEvents,
                        "totalTimeInMin", totalTimeInMinutes);
            }).orElseThrow(() ->
                new RuntimeException("Internal Server Error - could not retrieve events for type: " + type));
    }


    /**
     * Calculates the number of minutes between two unix timestamps.
     *
     * @return a double value of the difference in minutes.
     */
    static double getMinutesBetweenUnixTimestamps(long t1, long t2) {
        return Math.abs(t2-t1)/60.0;
    }
}
