"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Try to create an O(n)

Assume there are at LEAST two pointers to utilize 

hHave two pointers that attempt to determine the best size without repeating any indices

0 1 2 3 4 5 (r- l + 1) (width)
height = value at list location 

Assume there will be duplicate numbers in list
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        if len(height) < 2: # check if there are enough heights to hodl water
            return 0

        l, r = 0, len(height) -1 # set the limits of the list provided
        max_area = 0 # create variable to hold maximum area calculated

        while l < r: # as l and r iterate towards each other....
            area = self.area(l, r, height) # find area
            if  area > max_area: # check if newly found area is greater than current
                max_area = area
            
            if height[l] <= height[r]: # iterate one way or another towards each other
                l += 1
            else: r -= 1
        
        return max_area

        
    def area(self, l: int, r:int, height: List[int]) -> int:
        area = min(height[l], height[r]) * (r-l) 
        # HEIGHT use the min of the two heights as water would otherwise spill over edge,
        # WIDTH  subtract the index l and r and add 1 to account for the whole distance
        return area



if __name__ == '__main__':
    solution = Solution()

    height = [1,1]

    print(solution.maxArea(height))
