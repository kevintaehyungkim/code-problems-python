
###################
### COIN CHANGE ###
###################
'''
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Time: O(S∗n). 
Space: O(S). We use extra space for the memoization table.
'''

# bottom-up dp: update if we can find larger coin denomination to replace previously needed #coins
def coin_change(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0

    for i in xrange(1, amount+1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i-c] + 1)

    if dp[amount] == amount+1:
        return -1

    return dp[amount]


#####################
### COIN CHANGE 2 ###
#####################
'''
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
'''
def coin_change(amount, coins)
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]


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


#################################################
### LARGEST NON-ADJACENT SUM [HOUSE ROBBER I] ### 
#################################################
'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses 
have security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
'''

# dynamic programming solution
# O(n) time
# O(1) space if using nums instead of dp - however not preferred to change input

def rob(nums):
	length = len(nums)
    if length == 0:
        return 0

    if length == 1:
        return nums[0]

    if length == 2:
        return max(nums)
		
    dp = [0]*length # assign dp array
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    
    for i in range(2, length):
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])
    
    return dp[-1]


### REGEX ESPRESSION MATCHING ###
'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

# key idea: top-down DP and cache intermediate results
# time: O(TP)
# space: O(TP)
def isMatch(self, text, pattern):
        memo = {}
        
        def dp(i, j):
            if (i, j) not in memo:

                # if both reaches the end 
                if j == len(pattern):
                    if i == len(text): 
                    ans = i == len(text)

                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans

            return memo[i, j]

        return dp(0, 0)



'''
Cracking the Coding Interview
8.11: Given an infinite number of quarters, dimes, nickels, and pennies, write 
code to calculate the number of ways of representing n cents.
'''
# Memoization
def coins(n):
    memo_arr = [None]*(n+1)
    return find_ways(n, memo_arr)

def find_ways(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n]:
        return memo[n]
    else:
        memo[n] = find_ways(n-1, memo) + find_ways(n-5, memo) + find_ways(n-10, memo) + find_ways (n-25, memo)
        return memo[n]


if __name__ == '__main__':
  print coins(300)





# jump game

# longet increasing subsequence

# longest common subsequence

# decode ways