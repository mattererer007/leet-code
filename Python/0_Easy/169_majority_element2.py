from typing import List

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Could you solve the problem in linear time and in O(1) space?

(1) Assume list is not sorted
(2) Assume list only contains integers
(3) Assume list has values

O(1) space implies that no additiona; tables are created

"""

#O(nlog(n)) time for sorting and potentially more than O(1) space for creating the sorted list
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:

        # find the midpoints and make sure it is never 0 (i.e, when only 2 values in list)
        midpoint = int(max(len(nums) / 2, 1))

        # sort list
        sorted_nums = sorted(nums)

        # return value at middle
        return sorted_nums[midpoint]
    
#O(n) where every number is reviewed once and no additional memory is needed
# Thank you Boyer and Moore!
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:

        # Count to track the number of times the current candidate number is in a list
        count = 0

        # current candidate
        candidate = 0

        # iterate through the entire list once
        for num in nums:
            # if count is 0, either at beginning of list or the current candidate did not have enough instances
            # in a row to be considered
            if count == 0:
                candidate = num

            # If the cadidate num shows up, + 1
            # Else -1
            if num == candidate:
                count += 1
            else:
                count += -1

        # Return whichever number is last. Simple and Clean
        return candidate


if __name__ == "__main__":

    nums = [2,2,1,2,1,2]
    solution = Solution1()
    print(solution.majorityElement(nums))