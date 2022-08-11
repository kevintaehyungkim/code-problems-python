In this challenge, you will implement an application that handles a stream of event datas, stores relevant information
as analytics, and makes the knowledge available for querying. In our exercise here, we simulate the incoming stream of
events generated from users browsing an online shop. Their actions on the site generate events related to their
browsing activities. Normally this stream of data would be fed into our system from an external source.
For the purposes of this challenge, we will use some small stream of data that we generate ourselves, and
rather than use an actual data streaming tool like Kafka, we'll consume this data from a mocked source within the application.

Your task is to handle the stream of data so that we have the ability to answer the following queries:
    * How many total occurrences of a given event are there?
    * How many total occurrences of a given event are there per minute, in a given time range?

Each event data in the data stream is a map containing the following keys:
    * type - This is the type of the event. The only types we consider valid in this exercise are 'browse', 'saveCart', and 'checkout'
    * unixTimestamp - This is the unix time (in seconds) of the event

These queries will be answered via HTTP calls. A simple skeleton for serving these HTTP calls has been included already
in the main class of the challenge. You will only need to fill in the portion marked in the code that writes the query
result to the response output.

The two necessary HTTP endpoints have already added to the code skeleton. They are both GET calls, and the type/timeranges are passed in via headers.
- Endpoint 1: Total count -
Header values: type
Example curl: curl -H 'type: checkout' localhost:8000/count

- Endpoint 2: Count per minute -
Header values: type, startTimestamp (unix time in seconds), endTimestamp (unix time in seconds)
Example curl: curl -H 'type: checkout' -H 'startTimestamp: 100' -H 'endTimestamp: 200' localhost:8000/countPerMinute

Please make sure to do the following:
    * Fill in all the locations marked with "TODO: Implement". Hint: To search all project files for some text, use the shortcut CMD + Shift + F
    * Include tests where you feel is needed
    * Define and implement the IDataStorage interface and InMemoryDataStorage class
    * Implement the data consumer class
    * Implement the AnalyticsService methods, which should return the data responses that then get written to the http response. It's been left open ended how the structure of response to the queries looks like. Please make a note of what structure you put the response in

Additional notes:
    * In the test directory please include sufficient testing. You can use JUnit, see the classes TestSample and TestSuite in the test/ directory.
    * To run the challenge, run the "Main" class, this will begin the stream of mocked event data, and start listening for HTTP calls.
    * Please make sure that you document anywhere you feel would be useful (JavaDocs, in line comments, etc).
    * We've supplied a few empty classes and interfaces to give you a place to start, but feel free to create additional classes if you feel they'd be useful.
    * Please use Java 8 for this challenge.
    * Consider creating a data class for the event data.
    * Feel free to use any libraries you find that might be useful, just include the dependencies in the "pom.xml" file.
    * Don't worry too much about space efficiency of the storage.

ADDITIONAL INFORMATION

------ IntelliJ IDE ------
For this challenge, we recommend using IntelliJ. This is the IDE we use during our day-to-day, and the challenge is optimized to work with IntelliJ.
However, you are free to complete the challenge however you wish. Just give us some instructions how to check your work if you used something else to complete it.
If you do not have IntelliJ, you can download the free community edition at: https://www.jetbrains.com/idea/download/.

To open the project in IntelliJ, you can go to "Open" and select the directory containing the full set of project files.

If you use IntelliJ, you will need to tell it what SDK to use. Go to Project Settings -> Project, and you can set up where it should look for your SDK. Remember to use Java 8+.

------ Maven ------
The project is set up so you can use Maven to get any dependencies.
Just add your dependency to the pom.xml file in the project root directory.
IntelliJ will ask you if you want to import dependencies if you have auto import enabled. If you don't have this enabled you'll need to manually trigger an import for the dependencies.

------ Submitting the Challenge ------
To submit the challenge you can compress the whole directory containing the project and email it to haven.wang@breinify.com.
