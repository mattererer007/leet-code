"""
Given a string s, find the length of the longest without duplicate characters.

A substring is a contiguous non-empty sequence of characters within a string.


Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
# This solution offers a O(n) time complexity with O(n) with at most each letter stored once
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # For edge case where no string is provided
        if not s:
            return 0

        unique_letters = {}  # Variable to track unique letters and their latest index
        pointer = 0  # variable used to track the index place of the letter after the duplicate for measuring length
        max_count = 0 # Track the max count of the slide

        for index, c in enumerate(s):

            # if a number is not yet in the unique_letters, add it
            if c not in unique_letters:
                unique_letters[c] = index

            # change the pointer to the furthest point along with no duplicates
            # Update the index for the letter found to be a duplicate  
            else:
                pointer = max(pointer, unique_letters[c]+1)
                unique_letters[c] = index
                
            # Take the max_count as either the current max or
            # the current duplicate free range 
            max_count = max(max_count, index - pointer + 1)

        return max_count
                



    
if __name__ == "__main__":
    s = "pww"

    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))

