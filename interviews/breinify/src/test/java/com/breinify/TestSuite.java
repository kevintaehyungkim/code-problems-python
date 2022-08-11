package com.breinify;

import com.breinify.consumer.DataConsumerTest;
import com.breinify.service.AnalyticsServiceTest;
import com.breinify.storage.InMemoryDataStorageTest;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
    AnalyticsServiceTest.class,
    DataConsumerTest.class,
    InMemoryDataStorageTest.class
})

public class TestSuite {}
