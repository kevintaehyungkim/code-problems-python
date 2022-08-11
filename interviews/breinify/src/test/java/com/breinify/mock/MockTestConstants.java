package com.breinify.mock;

import com.breinify.models.BrowseEvent;
import com.breinify.models.CheckoutEvent;
import com.breinify.models.SaveCartEvent;
import com.google.common.collect.ImmutableMap;

import java.util.Map;

public class MockTestConstants {

    // Browse Event Mocks
    public static final String BROWSE = "browse";
    public static final BrowseEvent BROWSE_EVENT_1 = new BrowseEvent(100L);
    public static final BrowseEvent BROWSE_EVENT_2 = new BrowseEvent(200L);

    // Checkout Event Mocks
    public static final String CHECKOUT = "checkout";
    public static final CheckoutEvent CHECKOUT_EVENT_1 = new CheckoutEvent(100L);
    public static final CheckoutEvent CHECKOUT_EVENT_2 = new CheckoutEvent(200L);

    // Save Cart Event Mocks
    public static final String SAVE_CART = "saveCart";
    public static final SaveCartEvent SAVE_CART_EVENT_1 = new SaveCartEvent(100L);
    public static final SaveCartEvent SAVE_CART_EVENT_2 = new SaveCartEvent(200L);

    // Event Data Maps
    public static final Map<String, Object> VALID_EVENT_DATA = ImmutableMap.of(
        "type", MockTestConstants.BROWSE,
        "unixTimestamp", 100L);
    public static final Map<String, Object> IRRELEVANT_EVENT_DATA = ImmutableMap.of(
        "type", MockTestConstants.IRRELEVANT_EVENT,
        "unixTimestamp", 100L);
    public static final Map<String, Object> EMPTY_EVENT_DATA = ImmutableMap.of();

    // Misc.
    public static final String IRRELEVANT_EVENT = "irrelevantEvent";

}
