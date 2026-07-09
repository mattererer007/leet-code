from typing import List
from heapq import heappush, heappop

"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""


class Solution:

    # kClosest uses a heap to sort the resulting euclid distances from least to greatest >> default of using heapq is min heap
    # In order to sort elements, The heappush operation maintains the heap property with time complexity O(log n) for each point insertion thus O(n log(n))
    # while the retrieval is O(k log(n)) where k is the number of items that need to be popped while popping takes O(log (n))
    # As k will always be <= to n the runtime is O(n log(n)) with a space complexity of O(n) for the heap created with all points

    ## a cool alternative would be max heap where the runtime would be O(n log (k))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:        

        # list to store k-min points 
        result = []
        
        # Create an empty heap (default min)
        heap = []

        # iterate through list of points
        for index, coordinate in enumerate(points):

            # calculate euclid distance from center (0,0)
            # While euclid formula is √(x1 - x2)^2 + (y1 - y2)^2) (x2, y2) == (0,0) and thus can be simplified
            x,y = coordinate[0], coordinate[1]
            euclid_distance = x*x + y*y

            # Push to heap which will auto be sorted
            heappush(heap, (euclid_distance, [x,y]))

        # Pull k elements 
        while k > 0:
            element = heappop(heap)
            result.append(element[1])
            k -= 1

        return result        
    
    # kClosest2 skips using heap entirely and instead sorts the points based on a formula (lambda) given
    # Sorting takes the standard min sorting runtime of O(n log(n)) with a space complexity of O(1) given no new lists generated
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort points based on given formula
        points.sort(key=lambda point: point[0]**2 + point[1]**2)
        return points[:k]


    

if __name__ == "__main__":

    points = [[3,3],[5,-1],[-2,4]]
    k = 2

    solution = Solution()

    print(solution.kClosest(points,k))
    print(solution.kClosest2(points,k))


