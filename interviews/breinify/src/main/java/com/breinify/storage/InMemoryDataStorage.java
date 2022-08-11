package com.breinify.storage;

import com.breinify.models.UserActionEvent;

import java.util.*;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class InMemoryDataStorage implements IDataStorage {
    private static final Logger LOG = Logger.getLogger("InMemoryDataStorage");

    /*
     * Given that we are to use an in-memory storage, I decided to use a
     * hashmap containing arraylists with user action events as the keys.
     * This allows for O(1) to store an event, O(1) and O(n) to find
     * events without and with timestamps respectively.
     *
     * For better scalability, I would ideally separate the events into
     * separate topics and process them via independent pipelines as opposed
     * to a single data consumer that processes all incoming user events.
     * In such a scenario, I would further optimize for performance around
     * find with timestamps provided by partitioning the arraylists into
     * ranges of different unix timestamps and only filter for relevant events.
     */
    private Map<String, ArrayList<UserActionEvent>> userActionEvents =
        new HashMap<String, ArrayList<UserActionEvent>>()
        {{
            put("browse", new ArrayList<>());
            put("checkout", new ArrayList<>());
            put("saveCart", new ArrayList<>());
        }};


    /**
     * Stores a {@link UserActionEvent} into the in-memory data storage.
     * @param event - any class derived from UserActionEvent interface.
     */
    public void storeUserActionEvent(UserActionEvent event) {
        String eventType = event.getEventType();

        if (userActionEvents.containsKey(eventType)) {
            userActionEvents.get(eventType).add(event);
        }
    }


    /**
     * Finds all {@link UserActionEvent}s with the provided search criteria.
     * If start and end times are not provided, only filters for the event type.
     * If event type is not supported, returns an empty optional.
     * If no events exist that match the search parameters, returns an optional
     * containing an empty list.
     *
     * @param eventType - string that represents a UserActionEvent implementation.
     * @param maybeStartTime - optional start time to filter search.
     * @param maybeEndTime - optional end time to filter search.
     *
     * @return a list of {@link UserActionEvent}s.
     */
    public Optional<List<UserActionEvent>> findUserActionEvents(String eventType, Optional<Long> maybeStartTime, Optional<Long> maybeEndTime) {
        if (maybeStartTime.isPresent() && maybeEndTime.isPresent()) {
            return Optional.of(userActionEvents.get(eventType).stream()
                .filter(event -> event.getTimestamp() >= maybeStartTime.get() && event.getTimestamp() <= maybeEndTime.get())
                .collect(Collectors.toList()));
        }

        return userActionEvents.containsKey(eventType)
            ? Optional.of(userActionEvents.get(eventType))
            : Optional.empty();
    }


    /**
     * Returns a set of strings for the currently stored action events.
     */
    public Set<String> getUserActionEventStrings() {
        return userActionEvents.keySet();
    }
}
