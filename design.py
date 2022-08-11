
####################################
### FIND MEDIAN FROM DATA STREAM ###
####################################
'''
Median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
'''

# space: O(n)
from heapq import *

def __init__(self):
    self.small = []  # the smaller half of the list, max heap (invert min-heap)
    self.large = []  # the larger half of the list, min heap

def addNum(self, num):
    if len(self.small) == len(self.large):
        heappush(self.large, -heappushpop(self.small, -num))
    else:
        heappush(self.small, -heappushpop(self.large, num))

def findMedian(self):
    if len(self.small) == len(self.large):
        return float(self.large[0] - self.small[0]) / 2.0
    else:
        return float(self.large[0])



##################################
###  INSERT DELETE RANDOM O(1) ###
##################################
'''
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements.
'''

from random import choice

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.nums_dict = {}
    self.nums_list = []

def insert(self, val):
    """
    Inserts a value to the set. 
    Returns true if the set did not already contain the specified element.
    """
    if val in self.nums_dict.keys():
        return False

    self.nums_dict[val] = len(self.nums_list)
    self.nums_list.append(val)
    return True

def remove(self, val):
    """
    Removes a value from the set. 
    Returns true if the set contained the specified element.
    """
    if val in self.nums_dict.keys():
        self.nums_list.pop(self.nums_dict[val])
        del self.nums_dict[val]
        return True
    
    return False

def getRandom(self):
    """
    Get a random element from the set.
    """
    return choice(self.nums_list)



##########################
### LOG STORAGE SYSTEM ###
##########################
'''
You are given several logs that each log contains a unique id and timestamp. 
Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.
int[] Retrieve(String start, String end, String granularity): 
	Return the id of logs whose timestamps are within the range from start to end. 
	Start and end all have the same format as timestamp. 

Example 1:
put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3]
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2]
'''

def __init__(self):
    self.logs = []
    self.index = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

    
def put(self, id, timestamp):
    self.logs.append([id, timestamp])


def retrieve(self, s, e, gra):
    res = []
    g = self.index[gra]
    
    for log in self.logs:
        timestamp = log[1][:g]
        if timestamp >= s[:g] and timestamp <= e[:g]:
            res.append(log[0])
            
    return res  



#################
### LRU CACHE ###
#################
# evicts least recently used object if cache full
# get(key) and put(key, value) in O(1) time

# Ordered Dictionary -> remembers the order that key was first inserted (uses hashmap and linked list)
# In the beginning, we will have least recently used and in the end, most recently used.

# Otherwise, doubly linked list and hashmap
# head contains recent (always new elements go head.next) and tail contains least recent (pop tail when cache full)
# hashmap values point to the node within the doubly linked list

from collections import OrderedDict
class LRUCache(object):
    def __init__(self, size):
        self.size = size
        self.cache = OrderedDict()

    def get(self, key):
        value = self.cache.pop(key, None)
        if value is None:
            return -1
        self.cache[key] = value
        return value
    
    def put(self, key, value):     
        if not self.cache.pop(key, None) and self.size == len(self.cache):
            self.cache.popitem(last=False)
        self.cache[key] = value



# HashMap + Linked List
class DLinkedNode(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
            
class LRUCache():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)

        if not node: 
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)



#####################
### MY CALENDAR I ###
#####################
'''
Implement a MyCalendar class to store your events. 
A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). 
Formally, this represents a booking on the half open interval [start, end), 
the range of real numbers x such that start <= x < end.
'''

# time: O(NlogN)
# space: O(N)
class TreeNode():
	def __init__(self, s, e):
		self.s = s
		self.e = e
		self.left = None
		self.right = None

class MyCalendar(object):

    def __init__(self):
	    self.root = None

    def book(self, start, end):
		if not self.root:
			self.root = TreeNode(start, end)
			return True
		else:
			return self.insert(start, end, self.root)
                
                
    def insert(self, s, e, node):
        if s >= node.e: 
            if node.right:
                return self.insert(s, e, node.right)
            else:
                node.right = TreeNode(s, e)
                return True
        elif e <= node.s: 
            if node.left:
                return self.insert(s, e, node.left)
            else:
                node.left = TreeNode(s, e)
                return True
        else:
            return False


##################################
### SEARCH AUTOCOMPLETE SYSTEM ###
##################################
'''
Design a search autocomplete system for a search engine. 
Users may input a sentence (at least one word and end with a special character '#'). 
For each character they type except '#', you need to return the top 3 historical hot sentences 
that have prefix the same as the part of sentence already typed. 

Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])

The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times

Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]

Operation: input(' ')
Output: ["i love you","i love leetcode"]

Operation: input('a')
Output: []

Operation: input('#')
Output: []
'''
def __init__(self, sentences, times):
    self.partial = []           # previously seen chars of current sentence
    self.matches = []           # matching sentences in decreasing frequency order
    
    self.counts  = defaultdict(int)     # map from sentence to its frequency
    for sentence, count in zip(sentences, times):
        self.counts[sentence] = count

def input(self, c):
    if c == "#":
        sentence = "".join(self.partial)
        self.counts[sentence] += 1
        self.partial = []       # reset partial and matches
        self.matches = []
        return []
    
    if not self.partial:        # first char of sentence
        self.matches = [(-count, sentence) for sentence, count in self.counts.items() if sentence[0] == c]
        self.matches.sort()
        self.matches = [sentence for _, sentence in self.matches]   # drop the counts
    else:
        i = len(self.partial)   # filter matches for c
        self.matches = [sentence for sentence in self.matches if len(sentence) > i and sentence[i] == c]
        
    self.partial.append(c)
    return self.matches[:3]


###############
### RECIPES ###
###############
'''
design a system for
a set of recipes
and a set of ingredients
and the recipes could be made up of raw ingredients and also of compound ingredients
and yeah I made some objects and did some tree shit
and basically had to return what could be made and so forth
and then the follow up was like adding stock to each ingredient


idea: tree structure 

- convert recipes into tree structure 
- iterate through each recipe -> compound ingredient
- check if compound -> check children 

- pantry class: dictionary with ingredient/count, methods to calcualte possible recipes
- recipe class: tree structure 

'''


########################
### RESTAURANT QUEUE ###
########################
'''
Current Restaurant Seating
- # available 
- tables for 8
- tables of 4 
- tables of 2

Reservation
- name
- phone number
- party size 


Process Class 
- queue for each table sizing 
- if available then remove from queue

- check if party size less than table size
- if queue for 4/8 empty, size below, then adjust to 2/4
'''



###############################
### INTUIT - SHARED COURSES ###
###############################
'''
You are a developer for a university. 
Your current project is to develop a system for students to find courses they share with friends. 
The university has a system for querying courses students are enrolled in, 
returned as a list of (ID, course) pairs.

Write a function that takes in a list of (student ID, course name) pairs and returns, 
for every pair of students, a list of all courses they share.

Sample Input:
student_course_pairs = [
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"]
]

Sample Output (pseudocode, in any order)

find_pairs(student_course_pairs) =>
{
    [58, 17]: ["Software Design", "Linear Algebra"]
    [58, 94]: ["Economics"]
    [17, 94]: []
}  
'''

# key idea:
# 1st iteration - keep track of student pairs and course student ids
# 2nd iteration - add to student pairs shared courses

# time: O(C*S)
# space: O(C+S)
def find_pairs(student_course_pairs):
	sids = set()
	sid_pairs = {} # tuple of every student id pair
	course_sids = {} # key - course id, value - set of sids

	# add student pairs and course/student map
	for p in student_course_pairs:
		sid, course = int(p[0]), p[1]

		# add student id to course
		if course in course_sids:
			course_sids[course].add(sid)
		else:
			course_sids[course] = {sid}

		# add student to student ids
		if sid not in sids:
			for sid2 in list(sids):
				s1, s2 = min(sid, sid2), max(sid,sid2)
				sid_pairs[(s1,s2)] = []
			sids.add(sid)

	# process student pairs
	for p in sid_pairs:
		sid1, sid2 = p[0], p[1]
		for c,s in course_sids.items():
			if sid1 in s and sid2 in s:
				sid_pairs[p].append(c)

	return sid_pairs



### INTUIT - PARKING LOT ###
'''
Implement a parking lot as a class. What functions would it need? How would you implement spaces/rows/storage?  

# class constants #
- parking_fee = 5 (constant int - per hour)
- total_spaces (constant int)

# class variables #
- lots
	{"level":
		{"row":
			{"number":
				...
			}
		}
	}

- free_spaces (int)
- parking_tickets (array)
- total_fees (int)

# subclass #
parking ticket
- tid
- time_start
- time_end
- total_price

# functions #
- update_lot(lot=(level, row, number)) -> either car enters or leaves
- assign_ticket()
- process_ticket()
'''



# Let's implement an in-memory filesystem with the following interface:

# mkdir(path:string)
# write_file(path:string, data:string)
# read_file(path:string) -> string

# The filesystem structure and all data should be stored in the program’s memory.

# /foo/bar
# /foo/bar/file1.txt
# /foo/file2.txt

# /foo/bar/baz/....

# d = {
#     "foo": {
#         "bar"
#     }
# }



'''
Hashmap - Explain hashcode() and equals(). What happens if both are overridden. Can objects be stored in Hashmaps  
Answer Question

Given a mathematical expression as a string, return an int computing the value of the expression. EX: 1+3-6 = -2  

Given a matrix of 1s and 0s with 0s representing a rectangle, find its coordinates and dimentions.  
Find the common ancestor for given two nodes  

Find the longest common subarray between two arrays of strings.  

Give a series of meeting times, find the time slot that is available to everyone
'''

'''
What do you know about Intuit

Design the sql schema for a ride share company

tell me a time when you work with a team and have challenge/conflicts 

0 Answers
Implement a parking lot as a class. What functions would it need? How would you implement spaces/rows/storage?
in-depth questions such as what is OOP

Text Justification with modifications. 


Full stack application that requires hitting an old Yahoo API and visualize the data. In 45 minutes. With the font 3x the size you're comfortable with.  

A team of people may ask you questions may be some engineers and manager.Some times VP of Eng may also be involved.
Nothing specific they ask you questions like:
Why did you do something only this way?
what are other wasy you could have done?
Pros and cons about some specific implementations etc.

1. Find the Median in two sorted arrays.
2. OS questions
– questions related to memory management and allocation.
– Fragmentation.
3. Design Question
– Bus Seat booking System.


3. Given an Alien Language , with all sorted words , find the order of alphabets.
'''



