from typing import List
from collections import deque
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

"""

# O(mn) time complexity where m is the number of rows and n is the number of columns. Each cell in grid is visited only once in loop
# O(mn) space complexity assuming all cells are added to queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Set variable to count number of islands found
        island_count = 0

        # if empty, then return 0
        if not grid:
            return 0

        # find sides of grid
        row_count = len(grid)
        col_count = len(grid[0])

        # Formula to conduct BFS search of grid
        ## Any grid cell adjacent to input that == 1 is added to queue 
        def bfs(row: int, col: int) -> int:

            # Set visited cell that had "1" to "2" so not revisited
            grid[row][col] = "2"
            queue = deque([(row,col)])

            while queue:
                r,c = queue.popleft()

                # top, bottom, right, left
                adjacent = [(r+1, c),(r-1, c),(r, c+1),(r, c-1)]

                # Check that adjacent is actually '1'
                for nr,nc in adjacent: 
                    if (0 <= nr < row_count) and (0 <= nc < col_count) and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        grid[nr][nc] = "2"

        # Iterate through each cell in grid
        for r in range(0, row_count):
            for c in range(0,col_count):
                if grid[r][c] == "1":
                    bfs(r,c)
                    island_count += 1

        return island_count


if __name__ == "__main__":
    test = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]

    solution = Solution()

    print(solution.numIslands(test))