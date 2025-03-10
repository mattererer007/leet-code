from typing import List
"""
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Assume there is only 1 rotting orange per basket

"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = [] # set up a que to hold nodes....aka oranges in
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0]) # determine the boundaries of the grid
        for r in range(ROWS): # iterate through entier grid O(M+N)
            for c in range(COLS):
                if grid[r][c] == 1: # if a coordinate is 1, add to fresh list
                    fresh += 1
                if grid[r][c] == 2: # if grid is rotten, add to rotten list
                    queue.append([r,c])

        # at this stage the whole graph has been parsed for the relevant items

        directions = [[0,1], [0,-1], [1,0], [-1,0]] # set the 4-directional adjacent paths that can be taken from a nice
        while queue and fresh > 0: # While there are still items 
            for i in range(len(queue)): # iterate layer by layer by segmenting the queue into blocks based on what is pulled in an iteration starting with just the '2's or rotten oranages
                r, c = queue.pop(0) # remove item from queue
                for dr, dc in directions: # iterate through the directions
                    row, col = dr + r, dc + c # set the directions
                    if (row >= 0 and row < ROWS) and (col >= 0 and col < COLS): # make sure that the values are in bounds
                        if grid[row][col] == 1: # check if value is a fresh orange
                            grid[row][col] = 2 # set it to 2 (visited)
                            queue.append([row,col]) # add to queue
                            fresh -= 1 # decrease number of free oranges
            if len(queue) > 0: # if items have been added to queue, proceed to add a minute to the time
                time += 1

            
        if fresh > 0 : # check if any oranges were missed as they were no adjacent to any subsequent rotten orange
            return -1
        else: return time 
    

if __name__ == '__main__':
    
    solution = Solution()
    grid = [[2,1,1],[0,1,1],[1,0,1]]

    print(solution.orangesRotting(grid))


