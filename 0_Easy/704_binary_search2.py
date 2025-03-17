from typing import List

"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""



# This is more of an O(n) solution as in the worst case, I will enter the while loop n times if I get stuck between two numbers
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Set point to middle of sorted list
        pointer = int(len(nums)/ 2)
        
        count = len(nums)

        while pointer > -1 and pointer < len(nums) and count > 0:
            if target - nums[pointer] < 0:
                pointer -= 1
            elif target - nums[pointer] > 0:
                pointer += 1
            else: 
                return pointer
            
            count -= 1
            
        return -1
    
# O(n) but shorter since doing half the list?
class Solution2:
    def search2(self, nums: List[int], target: int) -> int:

        m = int(len(nums)/ 2)
        l = 0
        h = len(nums) -1 

        if target > nums[m]:
            l = m
        elif target < nums[m]: 
            h = m
        else: return m

        for i in range(l, h+1):
            if nums[i] == target:
                return i

        return -1

# TRUE O(logn) solution
# In each iteration the set of numbers to be explored is decreased by half
class Solution3:
    def search3(self, nums: List[int], target: int) -> int:
        # Call the recursive function
        return self.binarySearch(nums, target, 0, len(nums) - 1)  

    # function to parse through list
    # will take the middle index and divdie to the upper or lower half depending on 
    # what the target is in relation tot he value found at the middle index
    def binarySearch(self, nums: List[int], target: int, l: int, h: int) -> int:

        # Make sure the pointers have not hit an edge (lower or higher)
        if l > h:
            return -1
        
        # Find middle
        m = (l + h) // 2

        # Make sure the middle does not go out of bounds if l and h hits upper limit
        if m >= len(nums):
            return - 1

        # recurse based on if target > or < nums[m]
        # Always set the upper or lower bound to 1 greater or lower than current middle index
        if target == nums[m]:
            return m
        elif target > nums[m]:
            return self.binarySearch(nums, target, m+1, h)
        else: 
            return self.binarySearch(nums, target, l, m-1)


        


if __name__ == "__main__":
    
    solution = Solution3()

    nums = [-1,0,3,5,9,12]
    target = 13

    print(solution.search3(nums, target))