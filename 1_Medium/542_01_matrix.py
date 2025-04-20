from typing import List
from collections import deque


"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

Assume always a square or rectangle

Assume there is always 1 0
"""



# Iterate through each cell in grid if 0 skip, if 1 initiate BFS
# BFS to look at cells closest to given cell, expand till hitting edges of grid 
# Dynamic programing >> create dict to track values in each cell that has already been reviewed

# O(mn) run time 
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        row_count = len(mat)
        col_count = len(mat[0])

        #top, bottom, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]


        # Start by enqueuing all 0s with distance 0
        queue = deque()
        for x in range(row_count):
            for y in range(col_count):
                if mat[x][y] == 0:
                    queue.append((x, y))
                # Else mark for review
                else:
                    mat[x][y] = float('inf')  # mark unvisited

        # BFS normally starting with the 0s
        while queue:
            row, col = queue.popleft()
            # for each cell iterate through all four directions
            for direction in directions:
                dr, dc = direction[0], direction[1]
                # ROw and column value for 4 directions
                r, c = row + dr, col + dc

                # if values in range...
                if 0 <= r < row_count and 0 <= c < col_count:

                    # if the the current cell if greater than the cell nect to it.... then set it to the value next to it + 1
                    ## This enables starting from 0 to go to the cell right next to it and add 1 because that is the distance. 
                    ### if a cell is changed to a lower number, it is added back into the queue to then check its neighbors
                    if mat[r][c] > mat[row][col] + 1:
                        mat[r][c] = mat[row][col] + 1
                        queue.append((r, c))

        return mat



        
# This is like O(m^2n^2)
class Solution1:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        #  list of all cells that contain 0
        visited_cells = set()

        col_count = len(mat[0])
        row_count = len(mat)

        #  list of all cells that contain 0
        for x in range(0, row_count):
            for y in range(0, col_count):

                if mat[x][y] == 0:
                    visited_cells.add((x,y))

        # find distance for all cells that are 1
        for x in range(0, row_count):
            for y in range(0, col_count):

                if mat[x][y] == 1:
                    mat[x][y] = self.ClosestZero(mat, (x,y), visited_cells)

        return mat

    def ClosestZero(self, mat: List[List[int]], currentOne: tuple, reference_list: set) -> int:
        row, col = currentOne[0], currentOne[1]

        col_count = len(mat[0])
        row_count = len(mat)

        distance = 1

        top = (row+1, col)
        bottom = (row-1,col)
        right = (row, col+1)
        left = (row, col-1)

        queue = deque()
        queue.append([top, bottom, right, left])
        
        while queue:
            iteration = queue.popleft()

            temp_list = []

            for cell in iteration:
                if cell in reference_list:
                    return distance
                else:
                    row,col = cell[0],cell[1]

                    if row+1 < row_count:
                        temp_list.append((row+1, col))
                    if row-1 >= 0:
                        temp_list.append((row-1, col))
                    if col+1 < col_count:
                        temp_list.append((row, col+1))
                    if col-1 >= 0:
                        temp_list.append((row, col-1))

            queue.append(temp_list)
            distance += 1

            
if __name__ == "__main__":

    mat = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0]]

    solution = Solution()

    print(solution.updateMatrix(mat))