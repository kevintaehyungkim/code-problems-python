
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



# jump game

# longet increasing subsequence

# longest common subsequence

# decode ways