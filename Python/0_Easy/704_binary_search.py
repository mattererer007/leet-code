"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) -1 # Define out reaches of list

        """
        This function works as it divdes the search area in half in each iteration
        Thus O(log(n)) is achieved as the space is divided in half each time till the target is reached...or not
        """
        # Search until left overlaps with right
        while left <= right:
            mid = (left + right) // 2 

            
            if nums[mid] == target: # If the current mid is the target, return
                return mid
            elif nums[mid] < target: # else, if the mid is LESS than target , set the left to mid + 1 
                left = mid + 1
            elif nums[mid] > target: # else, if the mid is GREATER than target, set the right to mid -1  
                right = mid - 1

        return -1

# Test Case
if __name__ == "__main__":

    solution = Solution()

    test = [-1,0,3,5,9,12]

    print(solution.search(test, 2))

