"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

#O(n + m) where n is the length of ransomNote and m is the length of magazine
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(magazine) < len(ransomNote):
            return False
        
        magazine_hash = self.createHash(magazine)

        for char in ransomNote:
            if char in magazine_hash and magazine_hash[char] > 0:
                magazine_hash[char] -=1
            else:
                return False
        
        return True
    
    def createHash(self, input: str) -> dict:

        output = {}

        for char in input:
            if char in output:
                output[char] += 1
            else:
                output[char] = 1

        return output
    
if __name__ == "__main__":
    
    solution = Solution()

    ransomNote = "aa"
    magazine = "aab"

    print(solution.canConstruct(ransomNote,magazine))