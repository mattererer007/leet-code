"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""

from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int: # O(n) solution as the list nums is simply iterated through twice
        count = 0 #set count to 0

        map = {} # Create a hashmap for checls

        for index, i in enumerate(nums): # O(n) where no value is looked at more than once
            if i in map: # O(1) to check if key is present
                map[i] += 1 # count how many times an individual value is found in map
            else: map[i] = 1

        for i in nums: # O(n) as the list is iterated through once
            if k-i in map and i == (k-i) and map[i] >= 2: # if i == k-i, make sure there is enough values to remove
                map[i] -= 2
                count += 1
            elif k-i in map and i != k-i and map[k-i] > 0 and map[i] > 0: # if i != k-i 
                map[i] -= 1
                map[k-i] -= 1
                count += 1

        return count
   


if __name__ == '__main__':
    solution = Solution()

    nums = [3,1,3,4,3]
    print(solution.maxOperations(nums,6))