class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice, idx = float('inf'), -1
        maxprofit = 0
        for i, price in enumerate(prices):
            if price < minprice:
                minprice, idx = price, i
            else:
                profit = price - minprice
                maxprofit = max(maxprofit, profit)
        return maxprofit
        