package com.breinify.service;

import com.breinify.mock.MockTestConstants;
import com.breinify.storage.IDataStorage;
import com.breinify.storage.InMemoryDataStorage;
import org.junit.Assert;
import org.junit.Test;

import java.util.Map;

public class AnalyticsServiceTest {

    // Mock
    private static IDataStorage dataStorageMock;
    private static AnalyticsService analyticsServiceMock;

    @Test
    public void testCorrectTotalCountForValidEvent() {
        int expectedCount = 2;
        String expectedType = MockTestConstants.CHECKOUT;

        initMock();

        Map<String, Object> actual = analyticsServiceMock.getTotalCountForType(MockTestConstants.CHECKOUT);
        int actualCount = (int) actual.get("numberOfEvents");
        String actualType = (String) actual.get("event");

        Assert.assertEquals(expectedCount, actualCount);
        Assert.assertEquals(expectedType, actualType);
    }

    @Test
    public void testCorrectTotalCountForEmptyEvent() {
        int expectedCount = 0;
        String expectedType = MockTestConstants.SAVE_CART;

        initMock();

        Map<String, Object> actual = analyticsServiceMock.getTotalCountForType(MockTestConstants.SAVE_CART);
        int actualCount = (int) actual.get("numberOfEvents");
        String actualType = (String) actual.get("event");

        Assert.assertEquals(expectedCount, actualCount);
        Assert.assertEquals(expectedType, actualType);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testCorrectTotalCountForInvalidEvent() {
        initMock();

        analyticsServiceMock.getTotalCountForType(MockTestConstants.IRRELEVANT_EVENT);
    }

    @Test
    public void testGetCountPerMinuteForValidType() {
        long startTime = 0L;
        long endTime = 240L;
        double expectedCountPerMin = 0.5;
        int expectedNumberOfEvents = 2;

        initMock();

        Map<String, Object> actual = analyticsServiceMock.getCountPerMinuteForType(
            MockTestConstants.CHECKOUT, startTime, endTime);
        double actualCountPerMin = (double) actual.get("countPerMin");
        int actualNumberOfEvents = (int) actual.get("numberOfEvents");

        Assert.assertEquals(expectedCountPerMin, actualCountPerMin, 0.0f);
        Assert.assertEquals(expectedNumberOfEvents, actualNumberOfEvents);
    }

    @Test
    public void testGetCountPerMinuteForInvalidType() {}

    @Test(expected = IllegalArgumentException.class)
    public void testGetCountPerMinuteForInvalidTimeStamp() {
        long startTime = 200L;
        long endTime = 100L;

        initMock();

        analyticsServiceMock.getCountPerMinuteForType(MockTestConstants.CHECKOUT, startTime, endTime);
    }


    // Initialize mock classes and fields
    private void initMock() {
        dataStorageMock = new InMemoryDataStorage();
        dataStorageMock.storeUserActionEvent(MockTestConstants.BROWSE_EVENT_1);
        dataStorageMock.storeUserActionEvent(MockTestConstants.CHECKOUT_EVENT_1);
        dataStorageMock.storeUserActionEvent(MockTestConstants.CHECKOUT_EVENT_2);

        analyticsServiceMock = new AnalyticsService(dataStorageMock);
    }
}
