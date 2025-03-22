"""
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

1010
1011
______
10101

11
01
___
100
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        solution = ""

        max_len = max(len(a), len(b))
        a = self.evenLength(a, max_len)
        b = self.evenLength(b, max_len)

        extra = 0

        for x in range(max_len-1,-1,-1):
                char_a, char_b = a[x], b[x]
                print(char_a, char_b)
                if int(char_a) + int(char_b) + int(extra) == 0:
                    solution = "0" + solution
                    extra = 0
                elif int(char_a) + int(char_b) + int(extra) == 1:
                    solution = "1" + solution
                    extra = 0
                elif int(char_a) + int(char_b) + int(extra) == 2:
                    solution = "0" + solution
                    extra = 1
                elif int(char_a) + int(char_b) + int(extra) == 3:
                    solution = "1" + solution
                    extra = 1

        if extra == 1:
            solution = "1" + solution

        return solution
    
    def evenLength(self, input: str, length: int) -> str:

        extra_length_needed = abs(len(input) - length)

        for i in range(0, extra_length_needed):
            input = "0" + input

        return list(input)

    

if __name__ == "__main__":

    solution = Solution()
    a = "1010"
    b = "1011"
    print(solution.addBinary(a,b))
    

