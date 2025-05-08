from typing import List

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

ASSUMPTIONS
- at least 3 numbers
- numbers can be negative or positive or 0
- anticipate duplicates
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = []
        already_viewed = set()
        already_found = set()

        sorted_nums = self.mergeSort(nums)

        for i in range(0, len(sorted_nums)):

            if sorted_nums[i] > 0:
                break

            if sorted_nums[i] in already_viewed:
                continue

            else:
                lo,hi = 0, len(sorted_nums)-1

                while lo < hi:

                    if lo == i:
                        lo += 1

                    elif hi == i:
                        hi -= 1

                    elif sorted_nums[lo] + sorted_nums[i] + sorted_nums[hi] == 0:

                        triplets.append([sorted_nums[lo], sorted_nums[i], sorted_nums[hi]])
                        already_viewed.add(sorted_nums[i])

                    elif sorted_nums[lo] + sorted_nums[i] + sorted_nums[hi] < 0:
                        lo += 1

                    else:
                        hi -= 1

        return triplets
    
    def mergeSort(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        leftHalf = nums[:mid]
        rightHalf = nums[mid:]

        sortedLeft = self.mergeSort(leftHalf)
        sortedRight = self.mergeSort(rightHalf)

        def merge(left: List[int], right: List[int]) -> List[int]:
            
            sorted_list = []
            i,j = 0,0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_list.append(left[i])
                    i+=1
                else:
                    sorted_list.append(right[j])
                    j += 1

            sorted_list.extend(left[i:])
            sorted_list.extend(right[j:])

            return sorted_list

        return merge(sortedLeft, sortedRight)  

if __name__ == "__main__":
    test1 = [1,0,-1]

    solution = Solution()
    print(solution.threeSum(test1))