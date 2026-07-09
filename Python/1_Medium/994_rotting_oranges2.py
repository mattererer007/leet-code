from typing import List
from collections import deque

"""
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

"""

# Time complexity is O(m x n) where each cell is visited at most once
# Space complexity is O(m x n) as the queue + visited + batch storage will take in all nodes at one point or another
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # if no oranges able to be counted
        if not grid:
            return -1

        # size of grid
        row_count = len(grid)
        column_count = len(grid[0])

        # queue for tracking rot
        queue = deque() #FIFO
        visited = set() # track cells already visited

        # count total number of fresh oranges for tracking
        fresh_orange_count = 0

        ## iterate through entire graph
        first_batch = [] # initiate a first batch to iterate through of rotten oranges (assume more than 1)
        for r in range(0,row_count):
            for c in range(0, column_count):
                if grid[r][c] == 1:
                    fresh_orange_count += 1
                if grid[r][c] == 2:
                    first_batch.append((r,c))
                    visited.add((r,c))

        queue.append(first_batch)

        # iterate second time looking for rotten orranges to begin tracking
        ## Above, Below, Left, Right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        minutes = 0

        # While there are batches...
        while queue:
            batch = queue.popleft() # grab the next array of rotten oranges

            # instantiate variable for collecting next batch
            next_batch = []

            for r,c in batch: # for each cell from batch....
                for r_dir, c_dir in directions: # iterate through directions of top, bottom, left, right
                    new_row, new_col = r + r_dir, c + c_dir

                    # check if new cell is in range and not already visited
                    if (0 <= new_row < row_count) and (0 <= new_col < column_count) and (new_row, new_col) not in visited:
                        visited.add((new_row, new_col)) # add to visited

                        # if fresh... change to rotten and then add to next batch
                        if grid[new_row][new_col] == 1:
                            fresh_orange_count -= 1
                            grid[new_row][new_col] = 2
                            next_batch.append((new_row, new_col))
            
            # if there are any new fresh oranges... add them
            if next_batch:
                queue.append(next_batch) 
                minutes += 1 # add 1 minute for count
        
        # Once all oranges that can be reached have been reached... check if any fresh oranges have been missed
        if fresh_orange_count > 0:
            return -1
        else:
            return minutes
    


if __name__ == "__main__":
    grid = [[2,1,1],[0,1,1],[1,0,1]]

    solution = Solution()

    print(solution.orangesRotting(grid=grid))

