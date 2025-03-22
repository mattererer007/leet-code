from typing import List

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""
# O(n) where the function iterates through all numbers in a list
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Use a set as they can only contain 1 unique instance of each integer
        nums_hash = set()

        # Iterate through list, if a number is found to already be in set...return true
        for i in nums:
            if i in nums_hash:
                return True
            else: 
                nums_hash.add(i)

        return False
    


if __name__ == "__main__":

    solution = Solution()
    test = [1,2,3,4]
    print(solution.containsDuplicate(test))