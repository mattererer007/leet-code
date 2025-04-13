from typing import List
import copy

"""
Given an integer array nums, find the with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

# COOL Algorithm >> Kadane's Algorithm: 
## (1) iterate through list 
## (2) Have a current_best that compares the given value to the sum of the current_best + value 
### This essentially is checking for whether the series of numbesrs so far is greater than the individual number
### In other words...should we continue to add to a series sum or start the series from the latest value
## (3) Compare current_best to global_best to make sure that greatest sum is tracked across whole set of numbers even with local ups and downs

"""
nums = [-2,1,-3,4,-1,2,1,-5,4]

x = -2 >> curr = 0, global = 0
x = 1 >> curr = 1, global = 1
x = -3 >> curr = -2, global = 1 (so far returning 1 would be the best sum)
x = 4 >> curr = 4, global = 4 ( 4 by itself is the best solution so far)
x = -1 >> curr = 3, global = 4
x = 2 >> curr = 5, global = 5 (4 + -1 + 2 is best solution so far)
x = 1 >> curr = 6, global = 6 (max solution)
x = -5 >> curr = 1, global = 6 (local downturn)
x = 4 >> curr = 5, global = 6 (local upturn)
"""

# O(n) time complexity, O(1) space complexity (just store 2 values)
# With added value of returning array of numbers.... still O(n) time but O(n) space complexity (at worst)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # local best given location in array
        currrent_best = 0

        # overal best given combinations so far explored
        global_best = float('-inf')

        current_array = []
        global_array = []
        # iterate through numbers 1 by 1
        for x in nums:
            currrent_best = max(x, currrent_best + x)

            if currrent_best == x:
                current_array = [x]
            else:
                current_array.append(x)                   

            global_best = max(global_best, currrent_best)

            if global_best == currrent_best:
                global_array = copy.deepcopy(current_array)

        return global_best, global_array
    
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    solution = Solution()
    print(solution.maxSubArray(nums))