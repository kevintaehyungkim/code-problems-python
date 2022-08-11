package com.breinify.models;

public class SaveCartEvent implements UserActionEvent {
    private static final String eventType = "saveCart";

    private final long timestamp;

    public SaveCartEvent(long timestamp) {
        this.timestamp = timestamp;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public String getEventType() { return eventType; }

}