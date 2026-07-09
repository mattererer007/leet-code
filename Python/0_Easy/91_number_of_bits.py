"""
Given a positive integer n, write a function that returns the number of 1s 

in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits
"""

# This is a nifty feature in Python. You can actually compare to integers as bits using '&'
# The idea would be to compare the given number to the number previous as this is done by removing a single bit and then doing bit-AND operations
## 0 & 1 >> 0
## 0 & 0 >> 0
## 1 & 1 >> 1
# instead for (a) converting an integer to its bit format and then (b) iterating through it bit-by-bit this simply reduces down the number by
# all the 1s used to represent it
### COOL


# Runtime is O(log(n)) as is theory you are not looking at every bit in n but rather by the number of 1s as in each case one 1 is removed
# Space needed is O(1) as nothing is stored other than the count 
class Solution:
    def hammingWeight(self, n: int) -> int:

        # bit_number = int(str(bin(n))[2:])
        count = 0

        while n:
            n = n & (n - 1)
            count += 1

        return count
    
if __name__ == "__main__":
    
    sample1 = 11
    sample2 = 128

    solution = Solution()

    print(solution.hammingWeight(sample2))