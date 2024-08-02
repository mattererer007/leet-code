from typing import List

"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

- edges have a value that is always less than it
- need to return index
- if array empty, return 0?
- assume there is a peak?
- assume all values are different


"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # find middle of index and see which side has a value greater than it

        # move to that value and see if it has a value grater than it...if not return index

        if nums is None or len(nums) <= 1: # Make sure there is a list to iterate through
            return 0

        x = int(len(nums) / 2) # Go to middle of list

        while x >= 0  and x < len(nums): # While x is still in range
            left = x - 1 # pull left val
            right = x + 1 # pull right val
            if left < 0 and (right >= len(nums) or nums[x] > nums[right]): #check if x is on left edge and thus just needs to greater than right value (if it exists)
                return x
            elif right >= len(nums) and (left < 0 or nums[x] > nums[left]): # check if x is on right edge and thus just needs to be greater than left value
                return x
            elif nums[x] < nums[left]: # iterate left if left is > current x
                x = left
            elif nums[x] < nums[right]: # iterate right if right > current x
                x = right
            else: return x
   


if __name__ == '__main__':
    
    solution = Solution()
    nums = [2,1]
    print(solution.findPeakElement(nums))

    

