class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = prices[0]
        for i,price in enumerate(prices[1:], start=1):
            minprice = min(price, minprice)
            profit = price - minprice
            maxprofit = max(0, profit, maxprofit)
        return maxprofit
        