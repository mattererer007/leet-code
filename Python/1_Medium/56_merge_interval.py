from typing import List

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


# assume NOT IN sorted order
"""

# iterate through through two sets at a time
## if there is not overlap, add to new list
## if there is overlap, take the least valie, and continue to  iterate till there is a max value 

# O(n^2) courtesy of using isnertion sort. COuld have used the built in sort for O(n * log(n)) but tested my memory
# O(n) with a return list created

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # use insertion sort to order the list from least to greatest to ensure while loop runs correctly
        intervals = self.insertionSort(intervals)

        # Create return lsit as well as two pointers to track the return list and intervals
        return_list = []
        return_list_pointer, intervals_list_pointer = 0,0

        # While there are still ranges to compare in the interval....
        while intervals_list_pointer < len(intervals):
            # grab the min and max value from the range
            curr_min, curr_max = intervals[intervals_list_pointer][0], intervals[intervals_list_pointer][1]

            # If the return lsit has items in it already...
            if len(return_list) > 0:

                # Grab the last values in the return list
                curr_return_min, curr_return_max = return_list[return_list_pointer][0],return_list[return_list_pointer][1]
                
                # Check if th curr max in the return list is greater than the curr min from intervals. If so merge the two lists
                ## increment the intervals pointer but NOT the return_list pointer as the return list is still on the most current item
                if curr_return_max >= curr_min:
                    return_list[return_list_pointer][1] = max(curr_return_max, curr_max)
                    return_list[return_list_pointer][0] = min(curr_return_min, curr_min)
                    intervals_list_pointer += 1

                # if the new range does NOT overlap with what is in the return list, simply append
                else:
                    return_list.append([curr_min, curr_max])
                    return_list_pointer += 1
                    intervals_list_pointer += 1
            else:
                return_list.append([curr_min, curr_max])
                intervals_list_pointer += 1

    
        return return_list
    

    def insertionSort(self, intervals: List[List[int]]) -> List[List[int]]:


        for i in range(1,len(intervals)):
            key = intervals[i]

            j = i - 1
            while j >= 0 and key[0] < intervals[j][0]:
                intervals[j+1] = intervals[j]
                j -= 1
                intervals[j+1] = key

        return intervals    


if __name__ == "__main__":
    intervals = [[1,4],[0,0]]

    solution = Solution()
    print(solution.merge(intervals))