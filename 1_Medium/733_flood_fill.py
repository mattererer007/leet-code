from typing import List

"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Assume that location exists


"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        m = len(image)
        n = len(image[0])

        if m < 1 or n < 1:
            return None

        pixel_color = image[sr][sc]

        # Early exit if the color is already the same
        if pixel_color == color:
            return image
             
        def dfs(x,y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != pixel_color:
                return
            else:
                image[x][y] = color
                dfs(x, y+1)
                dfs(x, y-1)
                dfs(x-1, y)
                dfs(x+1, y)

        dfs(sr, sc)

        return image
        



if __name__ == '__main__':
    
    solution = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]

    print(solution.floodFill(image, 1, 1, 2))