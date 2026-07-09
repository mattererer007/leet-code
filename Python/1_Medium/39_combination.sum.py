from typing import List

"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Assume all numbers candidates are positive
can't assume that candidates are in correct order
"""

# Need to track unique answer sets to ensure that no duplicate sets are created (sort?)
# need to iterate through each number starting as smalest to see

# first trye will submit a list with the lowest possible variable with the only option to go up so that there are no duplicates

# having a little trouble calculating the recursion. Will come back to this  
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        if not candidates:
            return []
        
        # ensure candidates are listed from least to greatest 
        candidates.sort()

        # Class viarables
        self.result = []
        self.target = target
        self.options = candidates

    
        def backtracking(path: List[int], current_sum, starting_index):

            # base case is that if pathway discovered then no need to continue...add and move on
            if current_sum == self.target:
                self.result.append(path[:])
                return 

            # Curtail pathways that are not out of range
            if current_sum > self.target:
                return
            
            # Iterate through each option using 'starting_index' to make sure that duplicate answers are not made (i.e., find that 2+2+3 == 8 but when on 3 find that 3+2+2 == 8)
            for i in range(starting_index, len(self.options)):
                path.append(self.options[i]) # select an option
                backtracking(path, current_sum + self.options[i], i) # try said option (will result in either the pathway being added to results and then closed out or pathway not considered viable and terminated)
                path.pop() # remove the most recent try so that a different pathway recursion can begin 


        backtracking([], 0,0)

        return self.result

            


    

if __name__ == "__main__":
    candidates = [2,3,5]
    target = 8

    solution = Solution()

    print(solution.combinationSum(candidates, target))