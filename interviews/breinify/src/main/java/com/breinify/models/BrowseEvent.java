package com.breinify.models;

public class BrowseEvent implements UserActionEvent {
    private static final String eventType = "browse";

    private final long timestamp;

    public BrowseEvent(long timestamp) {
        this.timestamp = timestamp;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public String getEventType() { return eventType; }
}
