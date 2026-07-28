

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        word1_dict = {}
        for c in s:
            if c not in word1_dict:
                word1_dict[c] = 1
            else:
                word1_dict[c] += 1

        for c in t:
            if c not in word1_dict:
                return False
            else:
                word1_dict[c] -= 1
                if word1_dict[c] == 0:
                    word1_dict.pop(c)
        
        if word1_dict:
            return False
        else:
            return True
        
        


if __name__ == "__main__":
    s1 = "anagramanagram"
    s2 = "n"

    solution = Solution()
    print(solution.isAnagram(s = s1,t = s2))