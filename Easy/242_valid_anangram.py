"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

ASSSUME s & t consist of lower case english letters

EDGE CASES: 1 string is blank

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if lengths are different then not valid
        if len(s) != len(t):
            return False
        
        # parsing through t
        hash_t = self.createHash(t)


        for x in s:
            if x in hash_t and hash_t[x] > 0:
                hash_t[x] -= 1 # if the value in s is found in t, decrement count so that a value cannot be counted twice
            else:
                return False

        return True              

    # Create a hash map of t such that  O(1) to search and key = letter and value = count
    def createHash(self, t: str):
        hash_string = {}

        for x in t:
            if x not in hash_string:
                hash_string[x] = 1
            else:
                hash_string[x] += 1

        return hash_string
            


if __name__ == "__main__":
    solution = Solution()

    s = "rat"
    t = "car"

    print(solution.isAnagram(s,t))

    # test = solution.createHash(t)
    # print(test)

