package com.breinify.storage;

import com.breinify.models.UserActionEvent;

import java.util.List;
import java.util.Optional;
import java.util.Set;

public interface IDataStorage {

    /**
     * Stores a {@link UserActionEvent} into the in-memory data storage.
     * @param event - any class derived from UserActionEvent interface.
     */
    void storeUserActionEvent(UserActionEvent event);

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
    Optional<List<UserActionEvent>> findUserActionEvents(String eventType, Optional<Long> maybeStartTime, Optional<Long> maybeEndTime);


    /**
     * Returns a set of strings for the currently stored action events.
     */
    Set<String> getUserActionEventStrings ();
}
