from typing import List

"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
"""
# This solution is O(N) runtime as it iterates through the list once and O(N) space complexity as it at the worst just deplicates, in memory, the list provided
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        new_start, new_end = newInterval[0], newInterval[1]

        return_interval = []

        # First check and see if interval provided is empty
        if not intervals:
            return [newInterval]

        # add first everything with a START < new_start
        N = len(intervals)
        i = 0
        while i < N and intervals[i][0] <= new_start:
            return_interval.append(intervals[i])
            i+= 1

        

        # Once a point is reached where the start > new_start we can see whether to 
        ## Append the newInterval where the new_start is greater than the last item added to 

        # First check if there is anything added yet:
        if not return_interval:
            return_interval.append([new_start, new_end])
        elif return_interval[-1][1] < new_start:
            return_interval.append([new_start, new_end])
        ## new_start falls somewhere between the start and end of the last item added to return_interval
        ### thus just add the larger end value
        else: 
            return_interval[-1][1] = max(new_end, return_interval[-1][1])

        # Now that the newInterval has been added, go ahead and process the rest...picking up right where i left off
        while i < N:
            new_start, new_end = intervals[i][0], intervals[i][1]

            # Essentially repeat for each future interval
            ## Check if the next item can smoothly fit into the return_interval where its start is greater than the previous entries end
            if return_interval[-1][1] < new_start:
                return_interval.append([new_start, new_end])

            ## Else in an iterative fastion, just replace the end with the larger of the two ends and proceed
            else: 
                return_interval[-1][1] = max(new_end, return_interval[-1][1])
            
            i+= 1

        return return_interval


if __name__ == "__main__":
    
    solution = Solution()

    test1 = [[1,5]]
    test1_input = [1,7]

    test2 = [[1,3],[6,9]]
    test2_input = [2,5]

    print(solution.insert(intervals=test1, newInterval=test1_input))