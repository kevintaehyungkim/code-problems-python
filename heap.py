import heapq


###############################
### K MOST FREQUENT ELEMENTS ###
###############################
'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''

'''
Heap: smallest element is always at the root

heappush - push value item onto the heap
heappop - pop and return smallest item from the heap

'''
def top_k_frequent(nums, k):

	num_count = {}
	for num in k:
		num_count.get(num,0) + 1

	heap = []
    
    for k in num_count:
    	heapq.heappush(heap, (k, num_count[k]))
    	if len(heap) > k:
    		heapq.heappop(heap)

    return [i[1] for i in heap]



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


########################
# merge k sorted lists #
########################



