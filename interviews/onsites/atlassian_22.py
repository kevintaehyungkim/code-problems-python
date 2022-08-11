 #!/usr/bin/python
 # -*- coding: utf-8 -*-

'''
1. Code design round
- Design/code an API rate limiter. 
Expectation was to come up with a Java maven project 
for the same and run a simple Junit for the implementation.

Answer Question
2. Given a list of candidates, find the winner only. 
Also for handling a tie, the candidate (out of all the candidates who had the same vote count), 
who secured highest votes first should be the winner.

Example:String [] candidates = {"A", "C", "E", "B", "A", "B", "C", "B", "D", "B", "A"};
Method to be exposed: String findWinner(String [] candidates);
This should return B

-> keep track of last index 

Lru cache implementation and code
root to leaf path sum equals a target or not using dfs and bfs

- Manager interview: focus on collaboration within the team, resolve conflicts, etc to see if the candidate is a good fit for the team
- Values interview: focused on customer empathy and checks whether candidate is a good fit for the company (is aligned with the company values)

System design for a simple API request, saving data to database, pros and cons of different design decisions.

You will be asked to design a system which can tag different atlassian products. 
Let's say, you create a jira ticket and want to tag it with some name, 
also you want to tag a post on confluence. Basically a shared service for tagging. 
They ask same question to everyone. 
- Elastic search /inverted index/columnar databse

https://www.elastic.co/blog/elasticsearch-as-a-column-store

In this article, we survey recent research on column-oriented database
systems, or column-stores, where each attribute of a table is stored in
a separate file or region on storage. Such databases have seen a resurgence in recent years with a rise in interest in analytic queries that
perform scans and aggregates over large portions of a few columns of a
table.

The big advantage of inverted indexes over row-structured indexes is they're excellent for representing frequently-appearing values (Cardinality (SQL statements)), which is why they're great for search engines and other types of full-text indexes. 
They're also great for complex search logic on the lookup values, which can be turned into a bunch of bit-ands and bit-ors on the bitmap lists.
The big downside of inverted indexes is their fastest implementations, namely the ones that use bitmaps, are hard to update, and often have to be fully rebuilt every time the database is updated. These types of inverted indexes are used for load-and-read workloads like search engines.

In practice, most relational databases that implement these types of indexes are columnar databases ( Column-oriented DBMS ), which implement the whole table using "inverted index" structures to store the column values, 
and which also use these for secondary indexes as well, although you can use an inverted index to index a row-structured base table - Postgres has inverted indexes of this type.




For coding round, i assume you might have gotten api rate limiter, election votes, top k files.
Question — Design a system ID_Generator that generates unique ID for different apps asking for the same. Google was given as an example, with the Google Apps like Youtube, Gmail, Maps etc acting as client to the ID_Generator system. The 2 API’s had to be written with 1st being to give an output ID on random basis, and 2nd being in the case where the client had a preferred ID.
The database models to be used was the next question. The tables used also had to be defined and I also had to write some of SQL queries. The decision of using RDBMS and not DBMS also needed to be explained. More optimisation was also required as time complexity was needed to be improved. So, Hash Tables and its use in primary memory was my solution to it.
There were questions regarding the tradeoffs between the 2 ways in which I had approached the question. Explaining the use of Load Balancer and multiple servers was also a requirement. Explaining CS core over here with the help of Process Synchronization and also explaining the efficient use of RAM and Secondary Storage will also earn good points.
The round ended with me asking some questions to the interviewer. This is also important, as being curious about the life at the company you’re interviewing at might add to your advantage.
PS: I was happy with the way I handled this round, because I was’nt very confident about it at the beginning . And, did get a mail that the next round was scheduled at 1:00 pm.
'''


# sort keys first 
# then sort values (don't need to keep explicit count of cote count)
def rankTeams(self, votes):
    d = {}

    for vote in votes:
        for i, char in enumerate(vote):
            if char not in d:
                d[char] = [0] * len(vote)
            d[char][i] += 1

    voted_names = sorted(d.keys())
    return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))


#sliding window maximum # 
'''
Process the first k elements separately to initiate the deque.

Iterate over the array. At each step :
    Clean the deque :
    - Keep only the indexes of elements from the current sliding window.
    - Remove indexes of all elements smaller than the current one, 
      since they will not be the maximum ones.

Append the current element to the deque.
Append deque[0] to the output.
Return the output array.
'''
def maxSlidingWindow(self, nums, k):
    q = deque() # stores *indices*
    res = []
    for i, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur:
            q.pop()
        q.append(i)
        # remove first element if it's outside the window
        if q[0] == i - k:
            q.popleft()
        # if window has k elements add to results 
        # (first k-1 windows have < k elements because we start from 
        # empty window and add 1 element each iteration)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res


# INTERVIEW # 

#######
# TPS # 
#######
'''
https://leetcode.com/discuss/general-discussion/1082786/System-Design%3A-Designing-a-distributed-Job-Scheduler-or-Many-interesting-concepts-to-learn

event scheduler
internal atlassian
http request 

ex. 8am - myservice.com/api/delete to happen 8 am monday 
ex. 8am monday - postservice.com/api/create 
9am tuesday - POST notificationservice.com/api/notify


schedule service
- get (primary id event key)
- create: create a new event model with new event id, store it in database 
- update: find the event id, if present, update with new event details
- delete: if event id is in database -> delete the event or mark as deleted 


mysql database
- stores all the events (past, present, future) 
- need ACID properties, use sharding 


process service
- use apache zookeeper as kind of a pseudo-scheduler -> heartbeart events to the database
    -> every minute or so, retrieve all events in the next minute
    -> take these events, and then start new jobs and then queue them into kafka messaging stream 
    -> depending on how we want to handle failures, we configure to retry or not
- ex. make sure we log event successes/failures -> 
- task.map -> log failures/successes 
- also have a monitoring service or event handler


event
- eventid: primary key (long)
- userid: (long)
- request_type: EventType (GET, CREATE, POST, DELETE, etc....)
- request_body: "postservice.com/api/create { ... }" 
- event_time: unix_timestamp 
- created_at: unix_timestamp 
- event_status: EventStatus (SCHEDULED, COMPLETED, DELETED, FAILED...)
'''



##########
# ONSITE # 
##########
'''
# 1 
We are going to implement a function that determines the winner of an election. Our function is going to look something like this:


String findWinner(List<String> votes)
We pass in a list of names and we are returned the name that appeared in the list of names the most times.

ties?  the winner of the election is the candidate that gets to the final tally first

n - length of votes 
c - candidates
time: O(n) 
space: O(c)

- current_lead: (name, votes)

= whoever has the most votes currently 

dictionary -> vote_count
- storing for each name key, value -> the number of votes 


# 2
Each voter can now vote for candidates in order. 
Voters can give 3 votes, with each vote providing points to the candidate in the following order:

Candidate 1: 3 points

Candidate 2: 2 points
    
Candidate 3: 1 point

The candidate with the most points wins.

ties? 
First candidate to the largest number of points wins


[[candidate1, candidate2, candidate3],....]

'''


def find_winner(votes): 
    if not votes:
        return "" 
    
    vote_count = {} 
    curr_lead = [[votes[0], 1]]
    
    for vote in votes: 
        vote_count[vote] = vote_count.get(vote, 0) + 1
        curr_vote_count = vote_count[vote] 
        
        if curr_vote_count > curr_lead[0][1]:
            curr_lead = [[vote, curr_vote_count]]
        
        elif curr_vote_count == curr_lead[0][1]:
            curr_lead.append([vote, curr_vote_count])
        
    return curr_lead[0][0]
    
votes1 = ['A', 'B', 'A' ,'C', 'B'] #A 
votes2 = ['A', 'A', 'B', 'B', 'C', 'C'] #A
votes3 = ['A', 'A', 'B', 'B', 'C', 'C', 'C'] #C
votes4 = [] #""

# print(find_winner(votes1))
# print(find_winner(votes2))
# print(find_winner(votes3))
# print(find_winner(votes4))

# a - 40, b - 41 
# a 43 b 43 
# A, B, C 

def find_winner2(votes): 
    if not votes:
        return "" 
    
    vote_count = {} 
    curr_lead = [votes[0][0], 3]
    
    def update_winner(candidate, vote_count, current_leader):

        if vote_count >= current_leader[1]:
            return [candidate, vote_count]
        
        return current_leader 
    
    # vote = [c1, c2, c3]
    for vote in votes: 
        c1, c2, c3 = vote[0], vote[1], vote[2]
        vote_count[c1] = vote_count.get(c1, 0) + 3
        vote_count[c2] = vote_count.get(c2, 0) + 2
        vote_count[c3] = vote_count.get(c3, 0) + 1

        curr_lead = update_winner(c3, vote_count[c3], curr_lead)
        curr_lead = update_winner(c2, vote_count[c2], curr_lead)
        curr_lead = update_winner(c1, vote_count[c1], curr_lead)
        
    return curr_lead[0]

    
votes5 = [['A', 'B', 'C'], ['B', 'A', 'C'], ['A', 'C', 'B']] #A 
votes6 = [['A', 'B', 'C'], ['B', 'A', 'C']] #B

print(find_winner2(votes5))
print(find_winner2(votes6))




###################
# ONSITE CODING 2 #
###################
'''
rate limiter on customer 

send request to rate limit function with their id -> true/false for request

// Perform rate limiting logic for provided customer ID. Return true if the
// request is allowed, and false if it is not.

boolean rateLimit(int customerId)

“Each customer can make X requests per Y seconds”

current time - allowed refresh window <-> current time 
- store requests that fall into this window
- delete requests for time point t that fall out of this window starting at index 0

dictionary: customer_recent_requests
key - customer id
val - [1, 2, 5, 10 , 15]  current time - 20, Y - 10
'''

class request_processor:
    
    def __init__(self, x, y):
        self.requests_allowed = x
        self.refresh_window = y 
        self.customer_request_cache = {} 
        
   
    def make_request(self, cid, curr_time):
        if cid in self.customer_request_cache: 
            if self.rate_limit(cid, curr_time):
                self.customer_request_cache[cid].append(curr_time)
            return
        
        self.customer_request_cache[cid] = [curr_time]
            
        return self.customer_request_cache

        
    def update_cache(self, cid, curr_time):
        # if theres no more prev requests within window, just delete cid from dict 
        if cid not in self.customer_request_cache:
            return
        
        reqs = self.customer_request_cache[cid]
        i = 0
        lower_limit = curr_time - self.refresh_window
        
        while i < len(reqs):
            req_time = reqs[i]
            if req_time >= lower_limit:
                break
            i += 1
        
        new_requests = reqs[i:]
        if not new_requests:
            del self.customer_request_cache[cid]
        
        self.customer_request_cache[cid] = new_requests

            
    def rate_limit(self, cid, curr_time): 
        self.update_cache(cid, curr_time)
        
        customer_reqs = self.customer_request_cache[cid]
        
        if len(customer_reqs) < self.requests_allowed: 
            print ("Able to make request for customer id:" + str(cid) + " at time: " + str(curr_time))
            return True 

        print ("Not able to make request for customer id:", str(cid) + " at time: " + str(curr_time))
        return False 

    
req_processor = request_processor(3, 5)

req_processor.make_request(0, 2) 
req_processor.make_request(0, 3) 
req_processor.make_request(0, 4) 
print(req_processor.customer_request_cache)
req_processor.make_request(0, 5) # not able to make request 
print(req_processor.customer_request_cache)
req_processor.make_request(0, 7) # not able to make request 
print(req_processor.customer_request_cache)
req_processor.make_request(0, 8) 
print(req_processor.customer_request_cache)
req_processor.make_request(0, 10) 
print(req_processor.customer_request_cache)

'''
Able to make request for customer id:0 at time: 3
Able to make request for customer id:0 at time: 4
{0: [2, 3, 4]}
Not able to make request for customer id: 0 at time: 5
{0: [2, 3, 4]}
Able to make request for customer id:0 at time: 8
{0: [3, 4, 8]}
Able to make request for customer id:0 at time: 10
{0: [8, 10]}



######################
### SYSTEMS DESIGN ###
######################

Design a system which can tag different atlassian products.
Let's say, you create a jira ticket and want to tag it with some name,
also you want to tag a post on confluence or bitbucket. 
[Basically a shared service for tagging]

Requirements: 
1. add/remove/get (tags for content) for tags on content
2. for a tag, see all content associated w tag 
3. dashboard (or list) of popular tags

?s: 
- endpoint for a tag that doesnt exist -> create if not found when adding
- can i assume high query/reading from db, moderate writes/ingest

main points: 
- content agnostic
- service id and content id -> dual key to identify specific content 

    confluence bitbucket jira 

    zookeeper + kafka stream

          tag service

   db/storage - elastic search 

# UNIQUE TAG ID GENERATION

how to generate tag id -> distributed id generation
zookeeper communication/distributed synchronization with servers responsible for tag service
- use any of the servers to generate a tag -> make id generation code an atomic process

# TAG SERVICE - REST API 

- createNewTagId(tagname) -> distributed unique id generator for tag id -> addTag 

- addTagToContent(tag id, service id, user id, content id)
     -> createNewTagID

- findTagIdForTagName(string tagname) [get]
     - which would take tagname -> find corresponding tag id 
     - 404 if not present 
 
- removeTagFromContent(tag id, service id, content id)

- getTagsForContent(service id, content id) 
     - list of tag ids associated w dual key
 
- findContentForTag(tag id) [finder]
     - return a collection of content, perhaps paginated
     - if no match, then return empty collection

- getMostPopularTags(int numberoftags) -> up until # tags? (perhaps set limit)
     - first query the distributed cache, if for watever reason theres no hit (servers went down) 
     - then run the search query (failsafe)

     - returns the most popular tagids based on highest content count
     - comparison tool for recency, how often it's being accessed


# DATABASE
- high query/reading from db
- instead of typical relational db -> elastic search
- inverted index -> hashmap -> column based inverted index

-> 2 tables: 
      1. [tagid, tagname, createdAt, deletedAt]
      2. tagid -> inverted index/column db module 
           -> [tag id, service id, content id, updatedAt, createdAt, deletedAt, taggedBy (userid)
      
      possibly:
      -> shard table 2 so that we have say 1 table w more than 30 content/service ids associated
      -> separating out into tables by recency (older tag ids no longer used -> aka. cold storage) 
 


performance degradation -> db overloaded - 


1. popular tag super slow 
- implemenet event messaging queue of the tag service 
- every 5 minutes -> cron 5 min -> create a new kafka job that will call getMostPopularTags(30) 
- maintain distributed cache using zookeeper and our servers -> zookeeper + configs ensure that content is synchronized

userA ->  first check the distributed server layer cache -> if not present then make query call within getMostPopularTags


2. scaling horizontally 
  - just add more servers -> more processing power to handle more requests

3. db sharding 

'''



    
    
    
    
    




