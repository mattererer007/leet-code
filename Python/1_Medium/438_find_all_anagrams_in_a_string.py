from typing import List
from collections import Counter
import copy

"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

# feels like a two pointer problem
# Increment on the length of the anagram, break it down into a hash table and ensure that there is only one of each letter


class Solution:

    # O(n) solution where no character is looked at more than once
    # O(1) space complexity as both counters would only hold up to 26 unique characters at most
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_count = Counter(p)
        s_count = {}
        left = 0

        for right in range(len(s)):
            # Grab the first value and proceed
            s_count[s[right]] = s_count.get(s[right], 0) + 1

            # if the range is larger than p, then remove the left most value
            if right - left + 1 > len(p):
                s_count[s[left]] -= 1 # decrement the left most value
                if s_count[s[left]] == 0: # celete variable if no count
                    del s_count[s[left]]
                left += 1 # shift window to right

            # If right - left + 1 has reached the length of p, then check if it is a match
            if right - left + 1 == len(p) and s_count == p_count:
                result.append(left)

        return result

    # In the right direction but still a bit much work
    def findAnagrams2(self,s: str, p: str) -> List[int]:

        result = []

        anagram_hash = {}
        for char in p:
            if char not in anagram_hash:
                anagram_hash[char] = 1
            else:
                anagram_hash[char] += 1

        i = 0
        while i <= len(s) - len(p):
            if s[i] not in anagram_hash:
                i +=1
            else:
                substring_hash = {}
                substring_hash[s[i]] = 1
                for j in range(i+1, i + len(p)):
                    if s[j] not in anagram_hash:
                        i = j + 1
                        break
                    else:
                        if s[j] not in substring_hash:
                            substring_hash[s[j]] = 1
                        else:
                            substring_hash[s[j]] += 1

                match = True

                for key, val in substring_hash.items():
                    if val != anagram_hash[key]:
                        match = False
                        i += 1
                        break

                if match:
                    result.append(i)
                    i += 1

        return result

    # Incredibly slow solution where sorting n *log(n) and then joining takes n so that alone is n^2 * log(n) with n being the length of the string....overall not a good solution
    def findAnagrams3(self, s: str, p: str) -> List[int]:

        result = []

        p = ''.join(sorted(p))

        for i in range(0, len(s) - len(p)+1):
            substring = ''.join(sorted(s[i:i+len(p)]))
            if substring == p:
                result.append(i)

        return result
    
if __name__ == "__main__":

    s = "cbaebabacd"
    p = "abc"

    solution = Solution()
    print(solution.findAnagrams(s,p))

