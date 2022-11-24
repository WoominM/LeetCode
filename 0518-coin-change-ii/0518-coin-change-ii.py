class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # @cache
        # def helper(amount, coins):
        #     if amount == 0: 
        #         return 1 
        #     if amount < 0 or len(coins) == 0: 
        #         return 0 
        #     return helper(amount - coins[-1], coins) + helper(amount, coins[:-1])
        # return helper(amount, tuple(coins))
    
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i-coin]
        return dp[-1]
    