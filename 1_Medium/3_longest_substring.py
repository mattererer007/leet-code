"""
Given a string s, find the length of the longest substring without repeating characters.

Note a substring is any portion of the string.... so how do you that without repeatedly going through the length of the string (aka brute FORCE)

consists of English letters, digits, symbols and spaces.
"""


class Solution:


    def lengthOfLongestSubstring(self, s: str) -> int: # (O(n)) where no number is reviewed more than once
        char_index_map = {}
        max_len = 0
        start = 0  # Left pointer of the sliding window

        for end, char in enumerate(s): # iterate through the string with the index (end) and char
            if char in char_index_map and char_index_map[char] >= start: # Check if the character has already been visited
                # Move the start pointer to the right of the previous duplicate character
                start = char_index_map[char] + 1 # set the left pointer to the right of the last instance
            
            # Update the last seen index of the current character 
            char_index_map[char] = end
            
            # Calculate the length of the current substring and update max_len if it's the largest found
            max_len = max(max_len, end - start + 1)
        
        return max_len

    def inneficient_lengthOfLongestSubstring(self, s: str) -> int: # (O(n^2))   

        # For tracking the length of the longest unique substring
        maxLen = 0
        count = 0

        # Convert string into a list of characters for easier iteration (O(n))
        s_list = list(s)
        l, r = 0, len(s_list)

        # Track instances of a char
        map = {}

        # Create a set() to track uniwue instances when finding longest substring
        unique_letters = set()

        # we look through list till a duplicate is foudn then start at the letter to the right of prior instance of duplicate (O(n^2)) >> as at most letter can be reviewed 2x each
        while l < r:
            char = s_list[l]
            if char in unique_letters:
                # Reset the count
                unique_letters.clear() # rest to continue adding letters and seeing if they are present
                maxLen = max (maxLen, count) #Compare the max length 
                count = 0 # reset count 

                # initiate the next count at the last instance of the letter that double counted
                l = max(map[char]) + 1
            else:
                unique_letters.add(char) # add letter to set() to check later for duplicates       
                count += 1 #increase count

                if char in map: # if char already in dictionary then to proceed to add its index
                    map[char].append(l)
                else: map[char] = [l] # Else add first instance of it

                l += 1 # Incease left pointer 

        maxLen = max(maxLen, count) # determine what the max length is between the last count and maxLen
        return maxLen
    

if __name__ == '__main__':
    solution = Solution()

    s = "dvdf"

    print(solution.lengthOfLongestSubstring(s))