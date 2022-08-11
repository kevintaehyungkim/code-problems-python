package com.breinify.consumer;

import com.breinify.models.BrowseEvent;
import com.breinify.models.CheckoutEvent;
import com.breinify.models.SaveCartEvent;
import com.breinify.models.UserActionEvent;
import com.breinify.storage.IDataStorage;

import java.util.Map;
import java.util.Optional;
import java.util.logging.Logger;

public class DataConsumer {
    private static final Logger LOG = Logger.getLogger("DataConsumer");

    private IDataStorage storage;

    public DataConsumer(final IDataStorage storage) {
        this.storage = storage;
    }

    /**
     * Consumes an user action event data map and saves to the data storage.
     * If map fields are invalid, throws an IllegalArgumentException.
     * If the event type is not supported
     *
     * @param data Event data map, containing fields 'type' and 'unixTimestamp'
     */
    public void consume(final Map<String, Object> data) {
        if (!data.containsKey("type") || !data.containsKey("unixTimestamp")) {
            IllegalArgumentException e = new IllegalArgumentException(
                "Event data map contains missing fields: " + data.toString());
            LOG.severe(e.getMessage());
            throw e;
        }

        String eventType = data.get("type").toString();
        Long timestamp = (Long) data.get("unixTimestamp");

        if (!storage.getUserActionEventStrings().contains(eventType)) {
            LOG.warning(String.format("Event data not processed - unsupported event type: %s.", eventType));
        } else {
            processEvent(eventType, timestamp);
        }
    }

    /*
     * Helper method to help process incoming user action events into their
     * respective models. Ideally we would want to have our messaging stream
     * of user action events partitioned into separate topics since the switch/case
     * conditions are not scalable.
     */
    private void processEvent(String eventType, long timestamp) {
        Optional<UserActionEvent> event;
        switch (eventType) {
            case "browse":
                event = Optional.of(new BrowseEvent(timestamp));
                break;
            case "saveCart":
                event = Optional.of(new SaveCartEvent(timestamp));
                break;
            case "checkout":
                event = Optional.of(new CheckoutEvent(timestamp));
                break;
            default:
                event = Optional.empty();
                break;
        }
        event.ifPresent(userActionEvent -> storage.storeUserActionEvent(userActionEvent));
        LOG.info(String.format("Event: %s at unix timestamp: %d has been successfully stored.",
                eventType, timestamp));
    }
}
