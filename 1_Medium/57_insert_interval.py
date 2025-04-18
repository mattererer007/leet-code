from typing import List

"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        new_start = newInterval[0]
        new_end = newInterval [1]

        return_interval = []

        # placing the new_start integer
        for x in range(0, len(intervals)):
            start = intervals[x][0]
            end = intervals[x][1]

            # too low in the range
            if new_start > end:
                continue

            elif new_start > start and new_start < end:
                break




            # new_start in between start and end
            elif new_start >= start and new_start <= end:
                # end within start and end
                if new_end <= end:
                    return intervals
                # end greater than end but equal than new start
                elif new_end > end and x+1 < len(intervals) and new_end == intervals[x+1][0]:
                    return intervals
                # end greater than end
                elif x+1 < len(intervals):
                     for y in range(x+1, len(intervals)):
                         if new_end 

        return return_interval


if __name__ == "__main__":
    
    solution = Solution()

    test1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    test1_input = [4,8]

    test2 = [[1,3],[6,9]]
    test2_input = [2,5]

    solution.insert(intervals=test1, newInterval=test1_input)