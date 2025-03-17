from typing import List

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

- assume all profitable prices 
- must as difference between lower index on list vs. higher
- there is at least 1 input
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        # Check length
        if len(prices) <= 1:
            return max_profit

        # Set initial buy price at highest possible value
        min_buy = float('inf')

        # iterate from first index to second to last index
        for i in range(0, len(prices) - 1):

            # If there is a price lower than current, set buying price to that            
            if prices[i] < min_buy:
                min_buy = prices[i]

            # Check and see if any prices after that are high enough to merit sale
            if prices[i+1] - min_buy > max_profit:
                max_profit = prices[i+1] - min_buy

        return max_profit



if __name__ == "__main__":
    solution = Solution()

    test = [7,1,5,3,6,4]

    print(solution.maxProfit(prices = test))
