from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        if len(prices) <= 1:
            return 0
        
        min_buy = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            if prices[i] < min_buy:
                min_buy = prices[i]

            if prices[i] - min_buy > max_profit:
                max_profit = prices[i] - min_buy

        return max_profit




    


if __name__ == "__main__":
    prices = [2,1,2,1,0,1,2]

    
    print(Solution().maxProfit(prices=prices))