package com.breinify.models;

/*
 * Although it's not within the domain of this particular problem,
 * I decided to use an interface to capture all user action events
 * because realistically each user action event would contain certain
 * fields that are only relevant to itself. Thus I wanted to modularize
 * for components that are independent from one another.
 */
public interface UserActionEvent {

    long getTimestamp();

    String getEventType();
}
