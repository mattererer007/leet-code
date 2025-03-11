from typing import List


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

So, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y which is 
value - x where value is the input parameter. 

Can we change our array somehow so that this search becomes faster?
"""

class Solution:

#Trial 2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        # Iterate through each value and its correspioding index
        for index, value in enumerate(nums):
            complement = target - value

            # Check if completement is in dictionary
            if complement in hash_table:

                # if it is, return the index of the complement and the index of the current value
                return [hash_table[complement], index]
            
            # If complement not found, add value to hash_table
            hash_table[value] = index

#Trial 1
        # hash_table = {}

        # # input entire list of numbers into hashtable. Order does not matter
        # for index, value in enumerate(nums):
        #     if value in hash_table:
        #         hash_table[value].append(index)
        #     else:
        #         hash_table[value] = [index]


        # # iterate through each value in table and see if another edits
        # for value in hash_table:
        #     other_num = target - value

        #     # For situations where the numbers are duplicate and exist
        #     if other_num == value and len(hash_table[value]) > 1:
        #         value_1 = hash_table[value].pop()
        #         value_2 = hash_table[value].pop()
        #         return [value_1, value_2]
            
        #     # For situation where the numbers are different
        #     elif other_num in hash_table and value != other_num:
        #         value_1 = hash_table[value].pop()
        #         value_2 = hash_table[other_num].pop()
        #         return [value_1,value_2]
    
        # # if no two numbers found, return blank
        # return []
        




if __name__ == "__main__":

    solution = Solution()
    test = [1,2,10,5,-1]
    print(solution.twoSum(test,4))
