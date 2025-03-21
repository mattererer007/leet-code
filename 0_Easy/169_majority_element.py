from typing import List

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array. 

Could you solve the problem in linear time and in O(1) space?

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority_element = 0
        table = {}

        # Iterate and gather the count
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1

        
        return
    

if __name__ == "__main__":
    nums = [2,2,2,1,1,1,2]

    solution = Solution()

    print(solution.majorityElement(nums))