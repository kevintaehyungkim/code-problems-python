package com.breinify.consumer;

import com.breinify.mock.MockTestConstants;
import com.breinify.models.UserActionEvent;
import com.breinify.storage.IDataStorage;
import com.breinify.storage.InMemoryDataStorage;
import org.junit.Assert;
import org.junit.Test;

import java.util.List;
import java.util.Optional;

public class DataConsumerTest {

    // Mock
    private static IDataStorage dataStorageMock;
    private static DataConsumer dataConsumerMock;


    @Test
    public void testConsumeWithValidEventData() {
        int expectedSize = 1;

        initMock();

        dataConsumerMock.consume(MockTestConstants.VALID_EVENT_DATA);
        Optional<List<UserActionEvent>> maybeActualResult = dataStorageMock.findUserActionEvents(
            MockTestConstants.VALID_EVENT_DATA.get("type").toString(),
            Optional.empty(), Optional.empty());

        Assert.assertTrue(maybeActualResult.isPresent());
        Assert.assertEquals(expectedSize, maybeActualResult.get().size());
    }

    @Test
    public void testConsumeWithInvalidEventData() {
        initMock();

        dataConsumerMock.consume(MockTestConstants.IRRELEVANT_EVENT_DATA);

        Assert.assertFalse(dataStorageMock.findUserActionEvents(
            (String)MockTestConstants.IRRELEVANT_EVENT_DATA.get("type"),
            Optional.empty(), Optional.empty()).isPresent());
    }

    @Test(expected = IllegalArgumentException.class)
    public void testConsumeWithEmptyEventData() {
        initMock();

        dataConsumerMock.consume(MockTestConstants.EMPTY_EVENT_DATA);
    }


    // Initialize mock classes and fields
    private void initMock() {
        dataStorageMock = new InMemoryDataStorage();
        dataConsumerMock = new DataConsumer(dataStorageMock);
    }
}