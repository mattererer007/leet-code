from typing import List
from collections import deque

"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. 

You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

    Begin with the starting pixel and change its color to color.
    Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) 
    and shares the same color as the starting pixel.
    Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
    The process stops when there are no more adjacent pixels of the original color to update.

Return the modified image after performing the flood fill.

Assume starting spot is valid location within graph

"""
# BFS Solution to flood fill - FIFO
#O(mn) total number of edges and nodes
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        
        queue = deque([(sr, sc)]) # initiate the queue of tuples 
        starting_color = image[sr][sc] # Set the color that will need to be switched to the given color
        visited = set() # Create a set for easy reference for what has already been looked at

        horizontal_max = len(image[0]) # Set the max number of columns
        vertical_max = len(image) # Set the max number of rows

        # Check if the starting item is already at color...then nothing to do
        if starting_color == color:
            return image

        # iterate while there are cells to visit
        while queue:
            row, col = queue.popleft()

            # Set the cell to the new color
            image[row][col] = color
            visited.add((row, col))

            # left horizonal 
            if col-1 >= 0 and image[row][col-1] ==  starting_color and (row, col-1) not in visited:
                queue.append((row, col-1))

            # right horizontal
            if col+1 < horizontal_max and image[row][col+1] ==  starting_color and (row, col+1) not in visited:
                queue.append((row, col+1))

            # top vertical
            if row-1 >= 0 and image[row-1][col] == starting_color and (row-1,col) not in visited:
                queue.append((row-1,col))

            # bottom vertical
            if row+1 < vertical_max and image[row+1][col] == starting_color and (row+1, col) not in visited:
                queue.append((row+1, col))
        
        return image       


    
if __name__ == "__main__":
    solution = Solution()

    sample = [[1,1,1],[1,1,0],[1,0,1]]

    print(solution.floodFill(image = sample, sr = 1, sc = 1, color = 2))

    # test = deque()
    # test.append((3,1))
    # test.append((2,2))
    # print(test)
    # sample, row = test.popleft()
    # print(sample, row)

