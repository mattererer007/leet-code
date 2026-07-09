"""
Given two strings s and t, return true if t is an of s, and false otherwise.


Assume all lower case
Assume may be different lengths
Assume may have spaces
"""
# O(n) >> goes through the length of string 1 in each lopp
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Check if both strings the same length
        if len(s) != len(t):
            return False

        # Create a hash variable
        s_hash = {}

        # Track frequency of each character from string 's'
        for char in s:
            if char in s_hash:
                s_hash[char] += 1
            else:
                s_hash[char] = 1

        # Compare characters from string 't' 
        for char in t:
            # if char is NOT in 's' or if no additional chars can be found in 's' frequency...
            # Then not an anagram
            if char in s_hash and s_hash[char] > 0:
                s_hash[char] -= 1
            else:
                return False
            
        return True
       



if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    solution = Solution()

    print(solution.isAnagram(s,t))
