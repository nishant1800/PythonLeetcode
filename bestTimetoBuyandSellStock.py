# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            currProfit = prices[i] - minPrice
            if currProfit > profit:
                profit = currProfit

            minPrice = min(minPrice, prices[i])
        
        return profit