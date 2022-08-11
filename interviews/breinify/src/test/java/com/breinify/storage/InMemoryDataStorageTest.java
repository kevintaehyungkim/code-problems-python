package com.breinify.storage;

import org.junit.Test;

public class InMemoryDataStorageTest {

    // Mock
    private static InMemoryDataStorage inMemoryDataStorageMock;

    @Test
    public void testStoreValidUserActionEvent() {
        initMock();
    }

    @Test
    public void testStoreUnsupportedUserActionEvent() {
        initMock();
    }

    @Test
    public void testFindValidEventsWithTimestamps() {
        initMock();
    }

    @Test
    public void testFindValidEventsEmpty() {
        initMock();
    }

    @Test
    public void testFindEventsWithInvalidTimestamps() {
        initMock();
    }


    // Initialize mock classes and fields
    private void initMock() {
        inMemoryDataStorageMock = new InMemoryDataStorage();
    }
}
