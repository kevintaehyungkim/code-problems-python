package com.breinify.models;

public class CheckoutEvent implements UserActionEvent {
    private static final String eventType = "checkout";

    private final long timestamp;

    public CheckoutEvent(long timestamp) {
        this.timestamp = timestamp;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public String getEventType() { return eventType; }

}