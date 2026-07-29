from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        pointer = len(nums)//2

        high_bound = len(nums) - 1
        low_bound = 0

        while low_bound <= high_bound:
            if nums[pointer] == target:
                return pointer
            elif nums[pointer] < target:
                low_bound = pointer +1
                pointer = ((high_bound + low_bound) // 2)
            elif nums[pointer] > target:
                high_bound = pointer - 1
                pointer = ((high_bound + low_bound) // 2)

            print(low_bound, pointer, high_bound)

        return  -1 


if __name__ == "__main__":

    nums = [-1,0,2,3,5,9,12]
    target = 2

    solution = Solution()

    print(solution.search(nums, target))
