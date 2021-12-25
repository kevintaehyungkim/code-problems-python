# -*- coding: utf-8 -*-





def max_sum(nums): 

    if not nums:
        return 0
    elif len(nums) <= 2:
        return sum(nums)
  
    return max(max_sum_helper(nums[0],nums[2:]), max_sum_helper(nums[1], nums[3:]), max_sum_helper(nums[0], nums[3:]))
  
  
  


def max_sum_helper(curr, nums):
  
    if not nums: 
        return curr

    if (len(nums) < 3):
        return (max_sum_helper(curr + nums[0], nums[2:]))
    else: 
        return max(max_sum_helper(curr + nums[0], nums[2:]), max_sum_helper(curr + nums[1], nums[3:]), max_sum_helper(curr + nums[0], nums[3:]))
             



print(max_sum([900, 105, 75, 400, 90, 5, 800]))
print(max_sum([75,105,120,75,90,135]))


