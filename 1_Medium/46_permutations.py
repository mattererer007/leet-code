from typing import List
import copy

"""
Given an array nums of distinct integers, return all the possible

. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

# O(n! * n) time complexity wtib n! permutations that each take n time to construct
# O(n) space complexity as recursions tack holds each variable once
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.perms = []

        # case of a single number in list
        if len(nums) == 1:
            return [nums]
        

        def backtrack(curr: List[int], used: set):

            # if all numbers have been added to list then add to perms
            if len(curr) == len(nums):
                self.perms.append(curr[:])  # shallow copy
                return
            
            # iterate through each number in list 
            ## if not used then add to curr
            for num in nums:
                if num not in used:
                    ## backtracking occurs from trying an iteration
                    curr.append(num)
                    used.add(num)

                    ## Performing recursion on iteration
                    backtrack(curr, used)

                    # removing try to test out another variable in its place
                    curr.pop()
                    used.remove(num)

        # call recursion
        backtrack([], set())
        return self.perms



    
if __name__ == "__main__":
    nums = [1,2,3]

    solution = Solution()

    print(solution.permute(nums))