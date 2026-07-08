from typing import List


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_dict = {}

        for index, num in enumerate(nums):
            if num in num_dict:
                num_dict[num].append(index)
            else:
                num_dict[num] = [index]

            print(num_dict)

        for index, i in enumerate(nums):
            if target-i in num_dict:
                if target-i == i and len(num_dict[i]) > 1:
                    return num_dict[i]
                if target-i != i:
                    return [num_dict[i][0], num_dict[target-i][0]]
            
        return []


if __name__ == "__main__":
    solution = Solution()
    test = [1,2,2,8,-1]
    print(solution.twoSum(test,4))
