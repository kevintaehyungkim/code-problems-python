# -*- coding: utf-8 -*-


###############
### TWO SUM ###
###############
'''
If two different entries in array equals given sum, return true
Provided array is sorted.

ex: [1,2,3,9], sum = 8 -> false
ex: [1,2,4,4,9], sum = 8 -> true

Time: O(N)
Space: O(1)
'''

# if not sorted, use a dictionary -> O(NlogN) time and space

def two_sum(nums, value):
	if not nums:
		return False

	low, high = 0, len(nums)-1

	while low < high: 
		s = nums[low] + nums[high]
		if s > value:
			high -= 1
		elif s < value: 
			low + 1
		else: 
			return True

	return False



#################
### THREE SUM ###
#################
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Difficult: Medium

Solution Notes:
Sort list, then use 2 pointers to cover every combination. See 3_sum_closest for more explanation.

O(n^2) time
O(1) space
'''

# if we are to try every triplet, O(n^3) time -> not good
# instead sort and then run through using indices
# that way time complexity is O(nlogn) + O(n^2) -> O(n^2) time
# sort in place with sort() function yields O(1) space

def three_sum(nums, value):
	res = []
	nums.sort()

	for low in xrange(len(nums)-2):
		mid = low + 1
		high = len(nums) - 1
		while mid < high:
			temp = [nums[low], nums[mid], nums[high]]
			s = sum(temp)
			if s < value:
				mid += 1
			elif s > value:
				high -= 1
			else:
				if temp not in res:
					res.append(temp)
				mid += 1

	return res



#################
### JUMP GAME ###
#################
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
'''
def can_jump(nums):
    m = 0
    for i in xrange(len(nums)):
        if i > m:
            return False
        m = max(m, i+nums[i])
    return True



### DELIVERY TIME - POSTMATES ###
def active_time(input):

    total, num_pickups = 0, 0
    prev_time = input[0][1]

    for d in deliveries: 
        curr_time, action = d[1], d[2]
        if action == 'pickup':
            if num_pickups != 0:
                total += (curr_time - prev_time)
            num_pickups += 1
        else:
            total += (curr_time - prev_time)
            num_pickups -= 1

        prev_time = curr_time

    return total 



###################
### DOMAIN HITS ###
###################
'''
# You are in charge of a display advertising program. 
Your ads are displayed on websites all over the internet. 
You have some CSV input data that counts how many times that users have clicked on an ad 
on each individual domain. Every line consists of a click count and a domain name, like this:

# counts = [ "900,google.com",
#      "60,mail.yahoo.com",
#      "10,mobile.sports.yahoo.com",
#      "40,sports.yahoo.com",
#      "300,yahoo.com",
#      "10,stackoverflow.com",
#      "20,overflow.com",
#      "2,en.wikipedia.org",
#      "1,m.wikipedia.org",
#      "1,mobile.sports",
#      "1,google.co.uk"]

# Write a function that takes this input as a parameter and returns a data structure 
containing the number of clicks that were recorded on each domain AND each subdomain under it. 
For example, a click on "mail.yahoo.com" counts toward the totals for "mail.yahoo.com", "yahoo.com", and "com". 
(Subdomains are added to the left of their parent domain)
'''

def num_hits(counts):
    hits = {}

    for result in counts:
        count_str, domain = result.split(',')
        count = int(count_str)
        split_domain = domain.split('.')

        for i in range(len(split_domain)):
            subdomain = ".".join(split_domain[i:])
            hits[subdomain] = hits.get(subdomain, 0) + count

    return hits



##############################
### FIRST MISSING POSITIVE ###
##############################
'''
Given an unsorted integer array, find the smallest missing positive integer.
Your algorithm should run in O(n) time and uses constant extra space.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
'''

# time: O(nlogn)
# space: O(1)
def firstMissingPositive(nums):
    nums.sort()
    res = 1
    for num in nums:
        if num == res:
            res += 1
    return res

# time: O(n)
# space: O(n)
def firstMissingPositive(nums):
    nums = set(nums)
    for i in xrange(1,2**31):
        if i not in nums:
            return i

# time: O(n)
# space: O(1)
def firstMissingPositive(nums):
    for i in xrange(len(nums)):
        while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
            tmp = nums[i]-1
            nums[i], nums[tmp] = nums[tmp], nums[i]
    for i in xrange(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1


def firstMissingPositive(self, nums):
    n = len(nums)

    if 1 not in nums:
        return 1
    
    if n == 1:
        return 2
    
    # Replace negative numbers, zeros, and numbers larger than n by 1s.
    # After this convertion nums will contain only positive numbers.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1
    
    # Use index as a hash key and number sign as a presence detector.
    # ex: if nums[1] is negative -  number 1 is present.
    # ex: If nums[2] is positive - number 2 is missing.
    for i in range(n): 
        a = abs(nums[i])
        # If you meet number a in the array - change the sign of a-th element.
        # Be careful with duplicates : do it only once using abs.
        if a == n:
            nums[0] = - abs(nums[0])
        else:
            nums[a] = - abs(nums[a])
        
    # Now the index of the first positive number 
    # is equal to first missing positive.
    for i in range(1, n):
        if nums[i] > 0:
            return i
    
    if nums[0] > 0:
        return n
        
    return n + 1



##########################
### FROG JUMP - TIKTOK ###
##########################
'''
A frog is crossing a river. 
The river is divided into x units and at each unit there may or may not exist a stone. 
The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, 
determine if the frog is able to cross the river by landing on the last stone. 
Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. 
Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
'''

# brute-force runtime is 3^N recursing through all possible scenarios
# key idea: BFS with memoization
# time: O(n^3) - Recursive BFS with memoization
# space: O(n^2) - storing value and jumpsize in visited
def can_cross(stones):
    last_stone = stones[-1]
    stoneSet = set(stones)
    visited = set()
    
    def goFurther(value,k):
        if (value+k not in stoneSet) or ((value,k) in visited):
            return False
        if value+k == last_stone:
            return True
        visited.add((value,k))
        if k > 2:
            return goFurther(value+k,k) or goFurther(value+k,k-1) or goFurther(value+k,k+1)

        return goFurther(value+k,k) or goFurther(value+k,k+1)
    
    return goFurther(stones[0],1)



####################
### K-DIFF PAIRS ###
####################
'''
532. K-diff Pairs in an Array
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and 
their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
'''

def findPairs(nums, k):
    pair_count = 0
    num_count = collections.Counter(nums)

    # num_count = {}
    # for num in nums:
    #     num_count[num] = num_count.get(num,0) + 1

    for num in num_count:
        if k > 0 and num + k in num_count or k == 0 and num_count[num] > 1:
            pair_count += 1
    return pair_count



##################################
### ARRAY PAIRS DIVISIBLE BY K ###
##################################
'''
Given an array of integers arr of even length n and an integer k.
We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return True If you can find a way to do that or False otherwise.
 
Example 1:
    Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
    Output: true
    Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

Example 2:
    Input: arr = [1,2,3,4,5,6], k = 7
    Output: true
    Explanation: Pairs are (1,6),(2,5) and(3,4).
'''
def canArrange(self, arr, k):
    if len(arr) % 2 == 1: 
        return False

    count = 0
    mod_count = {}

    for num in arr:
        mod = num % k
        r = k - mod
        if r in mod_count and mod_count[r] >= 1:
            count += 1
            mod_count[r] -= 1
        else:
            mod_count[mod or k] = mod_count.get(mod, 0) + 1

    return count == len(arr) // 2



####################################
### LONGEST CONSECUTIVE SEQUENCE ###
####################################
'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

def longestConsecutive(self, nums):
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak



###################################
### LONGEST INCREASING SEQUENCE ###
###################################
'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
'''

# time: O(N^2)
# space: O(N)
def lengthOfLIS(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
                
    return max(dp)



##############################
### LARGEST CONTIGUOUS SUM ###
##############################
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, which is more subtle.
'''

# dynamic programming solution
# O(n) time
# O(1) space
def max_subarray(nums):
	if not nums:
		return 0
	for i in xrange(1,len(nums)):
		nums[i] = max(nums[i], nums[i] + nums[i-1])
	return max(nums)



####################################
### MAX LENGTH REPEATED SUBARRAY ###
####################################
'''
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
'''
# time: O(M*N)
# space: O(M*N)
def findLength(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)



#####################################
### NUMBERS AT MOST N - DIGIT SET ###
#####################################
'''
Given an array of digits which is sorted in non-decreasing order. 
You can write numbers using each digits[i] as many times as we want. 
For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.
Return the number of positive integers that can be generated that are less than or equal to a given integer n.

All the values in digits are unique.
Digits are sorted in non-decreasing order.

Example 1:
Input: digits = ["1","3","5","7"], n = 100
Output: 20
- The 20 numbers that can be written are:
    1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

Example 2:
Input: digits = ["1","4","9"], n = 1000000000
Output: 29523

Example 3:
Input: digits = ["7"], n = 8
Output: 1
'''
# time: 
# space:



######################################
### PATTERN MATCHING - AMAZON 2016 ###
######################################
'''
Dictionary of words. Pattern. We need to find all the words in the dictionary that match the given pattern.

Dictionary: [‘ABC’ , ‘AMM’, ‘MNN’, ‘AQA’]
Pattern: 'ABB'
pattern mnm
ABC => [0 1 2] [A, B, C]

AQA = 121
ABB = 122
MNM = 121
'''

def find_pattern (my_dict, pattern):
    if len(pattern) == 0: 
        return False

    result = []

    pattern_array = []
    num_letters = 0
    letter_dict = {}

    for letter in pattern:
        if letter in letter_dict.keys():
            pattern_array.append(letter_dict[letter])
        else:
            pattern_array.append(num_letters)
            letter_dict[letter] = num_letters
            num_letters += 1

    for entry in my_dict:
        if len(entry) != len(pattern):
            continue
        entry_array = []
        letters_used = 0
        entry_dict = {}
        for letter in entry:
            if letter in entry_dict.keys():
                entry_array.append(entry_dict[letter])
            else:
                entry_array.append(letters_used)
                entry_dict[letter] = letters_used
                letters_used += 1
        if pattern_array == entry_array:
            result.append(entry)
            
    return result


############################
### CONTAINER MOST WATER ###
############################
'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

# two pointer solution
# time: O(n)
# space: O(1)
def maxArea(height):
    left, right = 0, len(height)-1
    max_area = 0
    
    while left < right: 
        curr_water = min(height[left], height[right])*(right-left)
        max_area = max(max_area, curr_water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area



###########################
### TRAPPING RAIN WATER ###
###########################
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

# two pointer solution
# time: O(n)
# space: O(1)
def trap(height):
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        total = 0
        
        while left < right:
            left_height = height[left]
            right_height = height[right]
            
            if left_height < right_height:
                if left_height > left_max:
                    left_max = left_height
                else:
                    total += (left_max-left_height)
                left += 1
            else:
                if right_height > right_max:
                    right_max = right_height
                else:
                    total += (right_max-right_height)
                right -= 1
                
        return total



##############################################
### REVERSE SUBSTRINGS BETWEEN PARENTHESES ###
##############################################
'''
You are given a string s that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
'''
def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append(i)
            elif c == ')':
                left, right = stack.pop(), i
                s = s[0:left+1] + s[left+1:right][::-1] + s[right:]
                
        new_s = ""
        for c in s:
            if c not in set(['(', ')']):
                new_s += c
                
        return new_s



##########################
### SLIDING WINDOW MAX ###
##########################
'''

Given an array nums, there is a sliding window of size k which is moving from the very left 
of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position. 
Return the max sliding window and solve it in linear time.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 '''

 # time: O(N)
 # space: O(N)
import collections
def maxSlidingWindow(self, nums, k):
    d = collections.deque()
    res = []
    for i, n in enumerate(nums):
        # Popped from d because d has elements and nums[d.top] < curr element
        while d and nums[d[-1]] < n:
            d.pop()
        d.append(i)
        # Popped left from d because it's outside the window's leftmost (i-k)
        if d[0] == i - k:
            d.popleft()
        # Append nums[d[0]] = {} to out
        if i>=k-1:
            res.append(nums[d[0]])
    return res



#######################
### SKYLINE PROBLEM ###
#######################
'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city 
when viewed from a distance. Now suppose you are given the locations and height of all the buildings 
as shown on a cityscape photo,write a program to output the skyline formed by these buildings collectively.

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], 
where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, 
and Hi is its height.
'''

# time: O(NlogN)
# space: O(N)
def get_skyline(buildings):
    # `position` stores all coordinates where the largest height may change
    # `alive` stores all buildings whose ranges cover the current coordinate
    positions = sorted(set([b[0] for b in buildings] + [b[1] for b in buildings]))

    ptr, prev_height = 0, 0
    alive, res = [], []
    
    for curr_pos in positions:
        # pop buildings that end at or before `curPos` out of the priority queue
        # they are no longer "alive"
        while alive and alive[0][1] <= curr_pos:
            heappop(alive)
        
        # push [negative_height, end_point] of all buildings that start before `curPos` onto the priority queue
        # they are candidates for the current highest building
        while ptr < len(buildings) and buildings[ptr][0] <= curr_pos:
            heappush(alive, [-buildings[ptr][2], buildings[ptr][1]])
            ptr += 1
        
        # now alive[0] must be the largest height at the current position
        if alive:
            curr_height = -alive[0][0]
            if curr_height != prev_height:
                res.append([curr_pos, curr_height])
                prev_height = curr_height
        else:  # no building -> horizon
            res.append([curr_pos, 0])
            
    return res



##########################
### TEXT JUSTIFICATION ###
##########################
'''
Given an array of words and a width maxWidth, format the text such that 
each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.
'''

def full_justify(words, maxWidth):
    res = []
    char_count, curr_words = 0, []
    
    for word in words:
        curr_len = char_count + max(0,len(curr_words))
        if curr_len + len(word) <= maxWidth:
            char_count += len(word)
            curr_words.append(word)    
        else:
            temp = ""
            space_count = maxWidth - char_count  
            num_spaces = len(curr_words) - 1
            space_size = space_count // num_spaces if num_spaces > 0 else space_count
            first_space = space_size + (space_count % num_spaces) if num_spaces > 0 else space_count

            temp = curr_words[0] + ' '*first_space

            for i in range(1, len(curr_words)):
                if i == len(curr_words)-1:
                    temp += curr_words[i]
                else:
                    temp += curr_words[i] + ' '*space_size

            res.append(temp)
            char_count, curr_words = len(word), [word] 
        
    last_line = " ".join(curr_words)
    last_line += ' '*(maxWidth-len(last_line))
    res.append(last_line)

    return res
                


###################################
### MERGE OVERLAPPING INTERVALS ###
###################################
'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]

Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

# time: O(nlogn)
# space: O(1)
def merge_interval(intervals):
	intervals.sort()
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
                intervals.pop(i+1)
            else:
                i+= 1
        return intervals



###########################
### PRODUCT EXCEPT SELF ###
###########################
'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal 
to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of 
the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)
'''

def product_except_self(nums):
    answer = [1]*len(nums)
    answer[0] = 1
    for i in range(1, len(nums)):
        answer[i] = answer[i-1] * nums[i-1]
    rightProduct = 1
    for i in range(len(nums)-1, -1, -1):
        answer[i] = answer[i] * rightProduct
        rightProduct *= nums[i]
    return answer



'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
'''


def search(nums):
    start = 0
    end = len(nums) - 1
    while(start<=end):
        mid = (start+end)//2
        if(nums[mid] == target):
            return mid
        elif(target < nums[mid]):
            if(target < nums[start] and nums[start] <= nums[mid]):
                start = mid + 1
            else:
                end = mid - 1
        elif(target > nums[mid]):
            if(target > nums[end] and nums[end] > nums[mid]):
                end = mid - 1
            else:
                start = mid + 1
    return -1


'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:
    Input: [3,4,5,1,2] 
    Output: 1

Example 2:
    Input: [4,5,6,7,0,1,2]
    Output: 0
'''

    def findMin(nums):
        if len(nums) == 1:  return nums[0]
        if nums[-1] > nums[0]:           # when the array is not rotated
            return nums[0]
        
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            # ans found
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:         # indicates no rotation
                lo = mid + 1
            else:                           # search in rotated part
                hi = mid - 1



'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

def group_anagrams(strs):
	if not strs:
		return []

	key_dict = {}
	
	for s in strs:
		char_key = tuple(sorted(s))
		if char_key in key_dict:
			key_dict[char_key].append(s)
		else:
			key_dict[char_key] = [s]

	return key_dict.values()



######################
### FACEBOOK TPS 1 ###
######################
'''
Write a function that takes an input string and an alphabet, 
and returns the shortest substring of the input which contains every letter of the alphabet at least once.

Example:
Input:  "aaccbc"
Alphabet: "abc"
Output:  "accb"
'''

output_arr = []

def pangram_solver(input_str, alphabet):
    pangram_helper(input_str,alphabet)
    shortest_word = output_arr[0]
    for word in output_arr:
        if len(word) < shortest_word:
            shortest_word = word
    return shortest_word

    
def pangram_helper(input_str, alphabet):
    if not input_str:
        return None
    
    alpha_dict = {}
    for i in range(0, len(input_str)):
        a = input_str[i] 
        if a in alphabet:
            if a in alpha_dict.keys():
                alpha_dict[a] += 1
            else:
                alpha_dict[a] = 1
    if len(alpha_dict.keys()) == len(alphabet):
        output_arr.append(input_str)
    
        pangram_helper(input_str[1:], alphabet)
        pangram_helper(input_str[:-1], alphabet)

if __name__ == '__main__':
    print pangram_solver("aaccbc", "abc")



######################
### FLEXPORT TPS 1 ###
######################

DICT = {
    '1': ['a', 'b'],
    '2': ['c', 'd'],
    '12': ['x'],
    '22': ['y']
}

# get_words('1', DICT) => ['a', 'b']
# get_words('12', DICT) => ['ac', 'ad', 'bc', 'bd', 'x']
# get_words('122', DICT) => ['acc', 'adc', 'bcc', 'bdc', 'acd', 'add', 'bcd', 'bdd', 'xc', 'xd', 'ay', 'by']


def get_words(num_string, char_dict):
    if not num_string or not char_dict:
        return []

    return get_words_helper(num_string, char_dict, [])


def get_words_helper(curr_string, char_dict, curr_seq):
    if not curr_string and curr_seq:
        return curr_seq

    sequences = []

    for i in range(len(curr_string)+1): 
        curr_num = curr_string[:i]
        if curr_string[:i] in char_dict.keys():
            sequences += get_words_helper(curr_string[i:], char_dict, find_combinations(curr_seq, char_dict[curr_num]))

    return sequences


def find_combinations(curr_seq, next_vals):
    if not curr_seq:
        return next_vals

    next_seq = []
    for s in curr_seq:
        for t in next_vals:
            next_seq.append(s+t)

    return next_seq

# print(get_words('12', DICT))
# print(get_words('122', DICT))
# print(get_words('1222', DICT))
