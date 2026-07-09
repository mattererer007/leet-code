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

# This solution focuses on sorting the numbers from least to greaatest and then selecting number as the unique number that two other numbers need to 
# counteract to 0 (i.e., if i = 4, x+y == -4)
# Merge Sort is used to sort the list of numbers for a time complexity of O(n * log(n))
# Total time complexity is O(n^2) while with space being O(n^2) assuming all numbers are added multiple times to cover all possible combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = [] # to return a a list of unique triplet values that sum to 0
        used_first_values = set() # In case of duplicate values in nums, this will make sure that unique cases around the

        # Use recursion to sort numbers from least to greatest
        nums = self.mergeSort(nums)

        # Iterate through all numbers in list as the unique number that two other numbers must counteract
        for i in range(len(nums)):
            current = nums[i]

            # Early termination: if current > 0, no valid triplet exists beyond this point
            if current > 0:
                break

            # Skip duplicate fixed elements
            if current in used_first_values:
                continue

            # Set pointers to iterate through list
            # left is always i+1 such that current is never considered in solution
            left, right = i + 1, len(nums) - 1

            # While left and right do no cross....
            while left < right:
                # Determine total
                total = current + nums[left] + nums[right]

                if total == 0:
                    triplets.append([current, nums[left], nums[right]])

                    # Skip duplicates for left to not duplicate a solution
                    prev_left = nums[left]
                    while left < right and nums[left] == prev_left:
                        left += 1

                    # Skip duplicates for right to not duplicate a solution
                    prev_right = nums[right]
                    while left < right and nums[right] == prev_right:
                        right -= 1

                # If total is less than 0 then the left (negative number) needs to be increased
                elif total < 0:
                    left += 1
                # If notal is greater than 0 then the right (positive number) needs to be decreased
                else:
                    right -= 1

            # Add current to set so that duplicates are not considered
            used_first_values.add(current)

        return triplets

    # Merge Sort solves sorting by breaking a problem down to an individual unit
    # As the recursion unwinds, to individual lists of 1 valeu are compared and then sorted
    # This prevents the need to iterate through a list multiple times as swaps are minimized as pre-sorted lists are merged together
    def mergeSort(self, nums: List[int]) -> List[int]:

        # This triggers the end of the splitting and the beginning of the recursion
        if len(nums) <= 1:
            return nums

        # Values need to split up list into smaller components
        mid = len(nums) // 2
        leftHalf = nums[:mid]
        rightHalf = nums[mid:]

        # Recursion calls on increasingly smaller and smaller list of numbers
        sortedLeft = self.mergeSort(leftHalf)
        sortedRight = self.mergeSort(rightHalf)

        # Helper function to take two lists of numbers and to merge them in sorted order
        # This will start at the smallest possible increment of two lists of 1 number each
        def merge(left: List[int], right: List[int]) -> List[int]:
            
            sorted_list = []
            i,j = 0,0 # pointers to iterate through separate lists

            # while i and j are less than the length of their lists...
            while i < len(left) and j < len(right):
                # compare values and add to new list for efficient use of a list and NO swapping needed
                if left[i] < right[j]:
                    sorted_list.append(left[i])
                    i+=1
                else:
                    sorted_list.append(right[j])
                    j += 1

            # Once i or j has reached their end....just add the remaining values as they are greater than anything in sorted list
            sorted_list.extend(left[i:])
            sorted_list.extend(right[j:])

            return sorted_list

        return merge(sortedLeft, sortedRight)  

if __name__ == "__main__":
    test1 = [0,0,0,0]

    solution = Solution()
    print(solution.threeSum(test1))