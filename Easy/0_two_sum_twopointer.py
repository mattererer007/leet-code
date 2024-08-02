"""
TWO SUM
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order

Assumptions:
    Assume that the list is not ordered
    Assume that the list may not have a solution
    Assume that if there is a solution there would be EXACTLY ONE
    Assume duplicate values

Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # First sort list from least to greatest
        sorted_nums = self.quickSort(nums)

        # O(n) as every number is only tested once.
        index1 = 0
        index2 = len(sorted_nums) -1
        while (index1 < index2):
            if (sorted_nums[index2] + sorted_nums[index1] < target):
                index1+= 1
            elif (sorted_nums[index2] + sorted_nums[index1] > target):
                index2-= 1
            else:
                break  

        if sorted_nums[index1] + sorted_nums[index2] != target:
            return [-1, -1]
        
        else: 
            for i in range(0, len(nums)):
                if nums[i] == sorted_nums[index1]:
                    index1 = i
                    break

            for i in range(0, len(nums)):
                if nums[i] == sorted_nums[index2] and i != index1:
                    index2 = i
                    break            
            
            return [index1, index2]

    # Iterate through list of numbers and sort. 
    # Assuming that number is middle of the array is an optimal pivot O(n * log(n))
    # If in worst case where pivot is at the edge of the list O(n^2)
    def quickSort(self, nums):
        """
        :type nums: List[int]
        """
        # Check if list needs sorting
        if len(nums) <= 1:
            return nums
        
        # Select the middle array and divide
        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        # Continue to iterate till each arary is length of 1 and then return
        return self.quickSort(left) + middle + self.quickSort(right) 
    
    def altTwoSum(self, nums, target):

        hash = {}
        for index, x in enumerate(nums):
            if x in hash:
                hash[x].append(index)
            else: hash[x] = [index]

        for x in nums:
            other_nmbr = target - x
            if other_nmbr in hash and other_nmbr != x:
                return [hash[x][0], hash[target-x][0]]
            elif other_nmbr in hash and other_nmbr == x:
                if len(hash[x]) > 1:
                    return [hash[x][0], hash[x][1]]
        return [-1,-1]




# Test case
if __name__ == "__main__":
    solution = Solution()
    nums = [-3,4,3, 90, 90]
    target = 0
    result = solution.altTwoSum(nums, target)
    print (result)
    # print("Indices of the two numbers are:", result) 


