from typing import List
import queue

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        has_visited = set()
        fifo = queue.Queue()
        fifo.put((sr,sc))

        designated_color_change = image[sr][sc]

        y_length = len(image)
        x_length = len(image[0])

        while not fifo.empty(): 
            y_l, x_l = fifo.get()

            if (0 <= y_l < y_length) and (0 <= x_l < x_length):

                if image[y_l][x_l] == designated_color_change:
                    image[y_l][x_l] = color
                    has_visited.add((y_l, x_l))

                    # up, down, right, left
                    next_set = [(y_l-1, x_l),(y_l+1, x_l),(y_l, x_l-1),(y_l, x_l+1)]

                    for item in next_set:
                        if item not in has_visited:
                            fifo.put(item)


        return image




if __name__ == "__main__":
    input = [[1,1,1],[1,1,0],[1,0,1],[0,0,0]]
    sr,sc,color = 1,1,2

    solution = Solution()
    print(solution.floodFill(image=input,sr=sr,sc=sc,color=color))