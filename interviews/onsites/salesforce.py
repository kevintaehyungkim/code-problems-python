
'''

BFS, LinkedList questions, tree traversal, lru cache, overlapping rectangles problem

system design question centered around network latency - Lots of grilling around latency and making system fast

1. Symmetrical tree
2. Dequeue Snake maze
2. Mirror of a tree
3. Trie with Hash Map


system design. design a system where you could add, modify and delete contacts


3rd round
1. projects
2. trees traversals
3. code for recursive and iterative inorder traversal



Implement a class to track the number of site accesses in the last 5 minutes


array sorting 

Name several design patterns that you used in your most recent project.


BFS, DFS, Sorting, Map-Reduce, Database, System Design, Tree problems


tree traversals 

Balancing curly brackets, parens, and square brackets




'''



# tree traversals/binary tree
# sql
# graphs 



# sliding window maximum 
 def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## RC ##
        ## APPROACH : DEQUE ##
        """
            ## LOGIC ##
            1. For the First k numbers we can directly find maximum and store, 
            but the when the window slides by one position, the first element is removed. 
                What if the first number is the maximum of 0 to K ? 
                How do we know the second maximum when first element is removed ? 
                ( consider this example: [5, 2, 3, -1] and k = 3 ans = [5, 3] )
                So, For that we need to maintain some storage, here we use deque.
            2. Our Deque will always have the maximum at the start and we append 
            	small elements next to it. 
                ( if deque(for now, say we have numbers in it) is [4,1,0] 
                and incoming curr num is 2, pop all nums smaller from backside 
                i.e deque will be [4, 2] )
            3. And when the window slides, we remove all the numbers from front of 
            	deque if they donot fall under this window size.

            Example : [1,3,1,2,0,5] 3
            deque([0])              [1]
            deque([1])              [1, 3]
            deque([1, 2])           [1, 3, 3]
            deque([1, 3])           [1, 3, 3, 3]
            deque([3, 4])           [1, 3, 3, 3, 2]
            deque([5])              [1, 3, 3, 3, 2, 5]

            ## TIME COMPLEXITY : O(N) ##
            ## SPACE COMPLEXITY : O(k) ##
        """
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while(deque and nums[deque[-1]] < num):
                deque.pop()     # 2
            if(deque and i - deque[0] >= k):
                deque.popleft() # 3
            deque.append(i)
            res.append(nums[deque[0]])
            # print(deque, res)
        return res[k-1:]

# min rescue bots
def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans


# super egg drop
class Solution:
    def superEggDrop(self, K, N):
        dp = [[0] * (K + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, K + 1):
                dp[i][j] = 1 + dp[i - 1][j - 1] + dp[i - 1][j]
            if dp[i][j] >= N:
                return i


# min taps to open water garden 
def minTaps(self, n, ranges):
        watered = [0]*len(ranges)
        
        for i in range(len(ranges)):
            cover = ranges[i]
            left = max(0,i-cover)
            watered[left] = max(i+cover, watered[left])
            
        res = lo = hi = 0            
        while hi < n:
            lo, hi = hi, max(watered[lo:hi+1])
            if hi == lo: return -1
            res += 1
            
        return res




'''
ONSITE: 


### 1 ###
LFU Cache 
-> data dict
-> frequency dict ()


### 2 ### 
'''
# Kevin/Amit
# Implement "int read(int count, byte *buf)"  using "int read4k(byte *buf);" 

# file: a b c d e -> 4k byte chunks of this file 
# byte buf[2];
# int ret = read(2, buf); //buf[0]:a, buf[1]:b, ret:2

# return expecting int 2 

# How to sort a very large table of integers?

'''
ex. 

t0 - [5, 2, 7, 6, 3, 8]

both would be indexed (10,000 rows) 
t1 - [5, 2, 7] 
t2 - [6, 3, 8]

-> sort (t0)

sort (t1) sort (t2) ...

merge the results we obtain two jobs for ex. 
-> result sorted 

[2,3] [5, 6] -> 

[2] [3] [5] [6] [7] [8] 

intermediate nodes that still maintain the sorted order but are separated into smaller tables
i1 [2, 3, 5] 
i2 [6, 7, 8]
-> chunks of tables that are sorted and then indexed in sorted order

-> reduce: [2,3,5,6] as the intermediate product 
-> 





int read(int count, byte *buf)"
-> count number of bytes (4k -> 4096)
-> base case scenario -> count < 4096:
    return read4k(buf) 

-> we want to separate out the byte array into chunks of 4k 
-> multiple byte arrays of size 4k -> 
-> while loop - for every 4k, add new byte array to our chunks 

-> for each of these chunks -> read4k(each chunk) 
-> piece those together in our final return string 

- character can be multi-byte

using... 

"int read4k(byte *buf);" 
-> passing in count #bytes we want to read 
-> block has fixed size 
-> reads in 4k bytes 

read from a file.. 
-> byte string/arr 



'''


'''
if count < 4096: return read4k(byte_arr)
else: 
    buff_split = [] 
    we want to separate out the byte array into chunks of 4k via while loop 
        add 4k chunks into buff_split 
        
    for each of these 4k chunks -> pass that into read4k(chunk)
        res += read4k(chunk)
        
    return res 
'''

# buf -> "b'0famfkenfkqnwlmwdlmwflqwfgegwpl" each char is 1 byte long 
def read(count, buf):
    if not buf:
        return ""
    
    if count < 4096:
        return read4k(buf) 
    
    curr = 0 #track how many bytes we've currently processed
    res = ""
    
    while curr < count:
        res += read4k(buf[0:4096])
        curr += 4096

    return res 

    
read(60000, b'abcdefghi....') 
    
    
# read from some underlying file 
def read4k(buf): 
    return 

'''   
josh armstrong - trying to understand the pseudocode 
amit ghosh - going over time to explain project overview and what you guys are working on 
srinivasan krishnamoorthy - manger tips ic high pressure, and jigsaw puzzle for people side 



### 3 ### 
design a system to get word count for file
- queue for client and backend
- check file size, if big split into chunks and multiprocess 



### 4 ### 
1. bst tree in-order iterator
2. using (1) create a DLL in place in increasing order 
3. using DLL create a balanced BST 



### 5 ### 
## Kevin/Jake 
## Start typing here

# Implement a Web Crawler
Implement a function, `crawl(url)`, that crawls all web pages (i.e., URLs) reachable from `url`.
The return result should map each web page to the list of links on that web page.

Assume you have a helper function, `getLinks(String url)`, that returns the list of links on a web page.

For example, `getLinks("http://foo.com")` might return: `['http://foo.com/bar', 'http://baz.com']`.

## Complete example
Consider a very small network with three web pages: http://foo.com,
http://foo.com/bar, and http://baz.com.

### http://foo.com
```html
<html>
  <body>
    Foo.com links:
    <a href="http://foo.com/bar">http://foo.com/bar</a>
    <a href="http://baz.com">http://baz.com</a>
  </body>
</html>
```

### http://foo.com/bar
```html
<html>
  <body>
    <a href="http://foo.com">Go back to the main page.</a>
  </body>
</html>
```

### http://baz.com
```html
<html>
  <body>
    Welcome to baz.com
  </body>
</html>
```

### Result

`crawl("http://foo.com")` should return a result like this after being serialized to JSON:
```json
{
  "http://foo.com": [
    "http://foo.com/bar",
    "http://baz.com"
  ],
  "http://foo.com/bar": [
    "http://foo.com"
  ],
  "http://baz.com": []
}
```
'''


'''
crawl -> foo.com 
    -> map each web page to the list of links on that web page.->

a.com -> b.com, c.com 

b.com -> d.com 
{
    a: [b,c]
    b: [d]
    c: []
    d: []
}

prevent cycles!
a -> b,c 
c-> a, d 
a -> c ... 

page_urls = {} -> for each url the list of links on web page
    k: url
    v: [] storing links

queue = [root_url] 

getLinks("http://foo.com")
    -> ['http://foo.com/bar', 'http://baz.com']
'''



def web_crawler(root_url):
    if not root_url:
        return {} 
        
    page_urls = {}
    url_queue = [root_url] 
    visited_urls = set() 
    
    while url_queue: 
        curr_url = url_queue.pop(0)
        if curr_url in visited_urls:
            continue
        
        reachable_links = get_links(curr_url) # [b.com, c.com]
        page_urls[curr_url] = reachable_links 
        
        url_queue += reachable_links
        
        visited_urls.add(curr_url)
        
    return page_urls 



def get_links(url):
    
    # return urls for a.com
    if url == "a.com":
        return ["b.com", "c.com"]
    
    # return urls for b.com
    elif url == "b.com":
        return ["d.com"]

    # return urls for c.com 
    elif url == "c.com":
        return ["a.com", "d.com"]
    
    return [] 
    
    
    
print(web_crawler("a.com"))
    
    


1. search through every available page in wikipedia.com



'''
    




'''
'''

Q: What's the difference btw TCP and UDP?
Q: What are Docker images and how are they used?
Q: How can web traffic be routed to Docker containers?
Q: How can two AWS VPCs be configured to communicate with each other?
Q: How would you design a web API for bank transactions?


Spark, Hadoop and Design questions for creating a data pipelines.

test plan design 
Some Network security and low level protocol questions

'''





