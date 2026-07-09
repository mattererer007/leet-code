from typing import List

"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

"""

# Time complexity is O(n) as each element is only looked at once
# O(1) space complexity as list is adjust in-space rather than creating a whole new list
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # use two pointers at the ends of the list
        curr_zero_place = 0
        curr_twos_place = len(nums) - 1

        pointer = 0

        # As 0s and 2s are sent to either the beginning or the end of the list, the pace that needs to get explored continues to shrink
        while pointer <= curr_twos_place:

            # If 2, move to the end and then bring in 2s pointer thus shrinking number of values to consider
            # Keep pointer where it is to check value swapped with
            if nums[pointer] == 2:
                nums[pointer], nums[curr_twos_place] = nums[curr_twos_place], nums[pointer]
                curr_twos_place -= 1

            # If 1, move to the beginning and bring in pointer to be closer to middle
            # Move pointer +1 to consider the next number as the swap is most likely with a 0
            elif nums[pointer] == 0:
                nums[pointer], nums[curr_zero_place] = nums[curr_zero_place], nums[pointer]
                curr_zero_place += 1
                pointer += 1

            # increment counter +1 if value is 1
            else:
                pointer += 1

if __name__ == "__main__": 
    nums = [2,0,2,1,1,0]

    solution = Solution()
    solution.sortColors(nums)

    print(nums)