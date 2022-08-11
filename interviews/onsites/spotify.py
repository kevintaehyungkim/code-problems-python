'''
I interviewed for a back-end engineer position at Spotify.
Location : New York

https://leetcode.com/discuss/interview-question/1101668/Spotify-or-Onsite-or-Software-Engineer-2-or-3-YOE/872833



Interview consists of 4 (four) 60 minutes round: System design, behavior/fit , algorithim coding question, case study

System design: Design a system that can retrieve and display thumbnails. Given 4 data centers ( 2 in EU, 2 in US ). 5x 1TB hard drive in each data center. You can do whatever you want with the data. Cannot use CDN ( I assumed since he wanted to know how you would distribute the files over 4 data centers and how to retrieve them efficiently. Basically what CDN does )

The interviewer was somewhat critical on everything I talked about. He wanted to know more details about all the components that I listed out. He kept telling me to only use what I am familiar with. Strong emphasis on meeting the requirements listed for this. He didn't ask to dive into storage / network/ bandwidth estimation

 "You mentioned you wanted to use webserver for this. What specific webserver ?"
 "Can HDFS support the requirement ? " 
 "what kind of DB ? why do you choose this DB?
Didn't do so well on this round as I didn't have much experience in designing from my past experience. Needed more study on this next time

Behavior/ Culture fit: This round was with hiring manager. Typical behaviral and culture fit questions. Nothing special. Just be yourself and don't be a jerk. Do use STAR format in your responses . Manager cared about culture and fit. Did well on this round

Coding only 1 question - medium leetcode. Can't go into much details on this but it's among top 10 frequent questions on spotify-tagged questions. Got the final result they were looking for, but didn't see the optimization it needed. Did average on this.

Case Study Most interesting round overall. Interviewer walked through the basic design of their system. Explained about a notification that their system failed. You work together with interviewer to figure out what went wrong and a potential fix. Interviewer took notes of all the steps and questions you asked along the way. They cared more about your approach and your way of thinking. Only thing I can talk about is to NOT focus on the obviously wrong and unnecessary questions. Questions that I asked which I thought was wasting alot of my time.

"Which version of product they were using when notification happened? 
"When was the latest commit on master branch? When was this deployed last? " ( always assume there is no mistake on versioning )
"Is there something wrong with configuration / settings ? "
"Have you tried bouncing the system ? (quick fix is never the answer. They were more focused on finding the real issue and preventing it from happening again)"
""
Overall, it was a pleasant experience interviewing with them. I'd give it more focus on studying the system design round. Their coding round was somewhat simple and straightforward. Nothing really hard or tricky.







TECHNICAL PHONE SCREEN

intro

recent project discussion

CS fundamentals
- time/space complexities 
- hashing collision 
- serialization
- what is map reduce 


data 
- sql problem

select track_id, count(distinct user_id) as user_count
from track_playbacks
group by track id 
order by user_count desc;

-write sample spark job


sliding window median
https://leetcode.com/problems/sliding-window-median/solution/ 



'''