from typing import Optional
import math
from typing import List

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

# Grab any value as the value to solve for (i.e, 2)
# Take the complement of the value (i.e., -2)
# Grab 1 value (x) for list
# Iterate through list to see if any value (y) + x  + complement == 0



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        solutions = []

        nums_hash = {}

        while nums:

            target_value = abs(nums.pop(0))

            for value in nums:

            
    

if __name__ == "__main__":
    
    nums = [-1,0,1,2,-1,-4]

    solution = Solution()
    print(solution.threeSum(nums))