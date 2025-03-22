"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

# how many ways to divide a number into 1s or 2s
## every step can be 1
## if even every step can be 2

# 1 step (1) >> 1
# 2 step (1,1) (2) >> 2
# 3 step (1,1,1) (2,1) (1,2) >> 3
# 4 step (1,1,1,1) (2,2) (1,1,2) (2,1,1) (1,2,1) >> 5
# 5 step (1,1,1,1,1) (1,1,1,2) (1,1,2,1) (1,2,1,1) (2,1,1,1) (1,2,2) (2,1,2) (2,2,1) >> 8
# 6 step (1,1,1,1,1,1) (1,1,1,1,2) (1,1,1,2,1) (1,1,2,1,1) (1,2,1,1,1) (2,1,1,1,1) (2,2,1,1) (2,1,2,1) (1,2,2,1) (1,2,1,2) (2,1,1,2) (1,1,2,2) (2,2,2) >> 13

# O(n) where n is the number of increments of 1 needed to get to input
# The pattern appears to be the sum of the previous 2 stair options (once past 2)
class Solution:
    def climbStairs(self, n: int) -> int:

        # Set low and high as the count of steps from the last two iterations
        low = 1
        high = 2
        
        # Check if n is 1 or 2 then simple return
        ## if 3 or greater, iterate to n and then return
        if n == 1:
            return 1
        elif n == 2 :
            return 2
        elif n >= 3:
            for x in range(3,n):
                low, high = high, low + high

        return low + high




if __name__ == "__main__":
    
    solution = Solution()
    n = 45

    print(solution.climbStairs(n))
