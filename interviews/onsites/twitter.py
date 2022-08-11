'''

The big data round was about tracking metrics related to user activity on the twitter app.
Design was big data heavy, streaming data etc, 
not much discussion on which backend DB etc to use, more focus was on partitioning/sharding.


Another was a ML experimentation tracking system to expose APIs to track which user belonged to which experiments in real-time,
discussion was more around using message queues/Spark, how to keep everything in-memory and still be disaster resilient etc.


https://leetcode.com/discuss/interview-question/1204393/Algo-List


https://www.geeksforgeeks.org/twitter-interview-questions-set-2/

https://www.geeksforgeeks.org/twitter-interview-set-1/     ->

- Given a file with certain parameters find the average of streaming values or count.
- Design an image duplicate finder system. How does it scale? 
	How can you insert new features such as image subject recognition?
- lru cache (implement key/value insertion and replaced/updated)
- Find the lowest common ancestor of Binary Tree 
- Clone a graph and analyze the time and space complexity 
	(since DFS based approaches leverage smaller time at the cost of higher memory) 
- Design a bloom filter to remove the duplicates from an unsorted array! 

On-site 

1. (Boggle–like a question) In a 2D array (M x N, in the given ex. 3×3) of numbers, find the strictly increasing path from the specified origin cell (1,0) to the specified destination cell (0, 2). The array may contain duplicates, and the solution should work with the dups. 

2.a. Design a unique hash function for every tweet on Twitter which will be used as part of a service. 
2.b. Find if a directed graph has cycles or not. Write a function with boolean return type for the same. 

3. Casual Lunch interview. 

4. Pattern matching using patterns containing chars (a to z) and ‘*’, ‘?’ and ‘.’ 

5.a. Describe how would you do external sort -> come to a map-reduce kind of solution. Each machine has 10M numbers (total 100M), 10 total machines. Each m/c has 20MB RAM and 50GB memory. 
5.b. N-Queens problem: find and print all possible non-conflicting positions for the Queen. 

6.a. Given an input binary tree and reference to a Node in the tree, find the next in-order successor for the input node. Output null if none. 
6.b. What is the best way to sort a k-sorted array? Optimize for time complexity. 
(My hint: use a priority queue of size k) 

7.a. Hiring manager: Design service for a. Durability b. Consistency 
7.b. Explain C++’s problem with multiple inheritances. 

If you like GeeksforGeeks and would like to contribute, you can also write an article and mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.



square - https://leetcode.com/company/square/

Phone round

Spent 10 mins talking about the project, why changing the company etc.
1 single question. It was hard and av variation of minimum substring question, but I felt it was harder than that.
Discussed with the interviewer to make it simple for the first iteration. Coded it and did a code walk-through. 
This step is very important I felt coding the whole question in 45 mins is impossible.
I think the interviewer wanted the code to be executable, but mine was not. Overall felt satisfactory.


onsite experience


This was a managerial round. There were 2 managers in the interview panel. One actively interviewing and one more passive. Lots of questions on resume, old jobs, positives, negatives, reviews from old managers etc. This round is very important to decide the level I guess.

This was an API design round. Importance is given to discussion, how we design interface, classes etc. The question was related to a wholesale shopping market. Not difficult, but needs real clean design, discussion about all cases, how consumers would use it, testability, and more.
Did well I guess. Did not see any obvious red flags.


Design a twitter feature, with custom requirements.
Emphasis on requirement gathering, identifying all cases, explaining pros and cons of a certain decision, Database and the reason to choose one, etc. I felt I did well. The interviewers were nice and liked the atmosphere.
'''







# twitter tps 2022 #
'''
-----------
find file duplicates from root dir 
-> separate the file traversal code from the duplicate detection code
-> faster by splitting this procedure into multiple threads


-----------
def process_directory(root):

- file_contents = collections.defaultdict(list) 


# def search_directory(path) 
	for file in path: 
		if dir -> search_duplicates(path + file)
		else -> check_file(hash_file()) 

	return file_contents.values() 
	

# def hash_file()

# def check_file() 

-> search_duplicates(root) 
-> return file_contents.values() 


''' 





Problems that have optimal substructure can be solved with greedy algorithms. 
If they also have overlapping subproblems, then they can be solved with dynamic programming algorithms.





TO-DO TODAY: 

https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/ 
https://leetcode.com/problems/rearrange-string-k-distance-apart/
https://leetcode.com/problems/design-search-autocomplete-system/
https://leetcode.com/problems/word-search/solution/
https://leetcode.com/problems/maximal-square/submissions/

LRU cache 

sys design 

'''
Word Search 
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False


    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret




'''
Paint House (Med)

There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. 
The cost of painting each house with a certain color is different. 

You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; 
costs[1][2] is the cost of painting house 1 with color green, and so on...

Return the minimum cost to paint all houses.
'''
# time: O(n)
# space: O(1)
 def minCost(self, costs):
        
        if len(costs) == 0: 
            return 0
        
        for i in range(1,len(costs)):
            costs[i][0] += min(costs[i-1][1],costs[i-1][2])
            costs[i][1] += min(costs[i-1][0],costs[i-1][2])            
            costs[i][2] += min(costs[i-1][1],costs[i-1][0])   
            
        return min(costs[-1])




'''
Maximum Number of Events That Can Be Attended II (Hard) 

You are given an array of events where events[i] = [startDayi, endDayi, valuei]. 
The ith event starts at startDayi and ends at endDayi, and if you attend this event, 
you will receive a value of valuei. 

You are also given an integer k which represents the maximum number of events you can attend.
You can only attend one event at a time. If you choose to attend an event, 
you must attend the entire event. Note that the end day is inclusive: that is, 
you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.
'''


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        # The number of events
        n = len(events)
        # Sort the events in chronological order
        events.sort()
        
        # k is the number of events we can attend
        # end is the last event we attended's END TIME
        # event_index is the current event we are checking
        @lru_cache(None)
        def dp(end: int, event_index: int, k: int):
            
            # No more events left or we have checked all possible events
            if k == 0 or event_index == n:
                return 0
            
            event = events[event_index]
            event_start, event_end, event_value = event
            # Can we attend this event?
            # Does its start time conflict with the previous events end time?
            # If the start time is the same as the end time we cannot end as well (view example 2)
            if event_start <= end:
                # Could not attend, check the next event
                return dp(end, event_index + 1, k)
            
            # We made it here, so we can attend!
            # Two possible options, we either attend (add the value) or do not attend this event
            # Value for attending versus the value for skipping
            attend = event_value + dp(event_end, event_index + 1, k - 1)
            skip = dp(end, event_index + 1, k)
            
            # Get the best option
            return max(attend, skip)
            
        # Clear cache to save memory
        dp.cache_clear()
        return dp(0, 0, k)





### maximal square ###

def maximalSquare(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for x in range(cols)] for y in range(rows)] 
        
        curr_max = 0
        
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])+1
                curr_max = max(curr_max, dp[r][c])
                    

        print dp
                
        return curr_max**2









