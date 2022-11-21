class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
#         def helper(path, value):
#             print(value, path)
#             if value == 0:
#                 if not self.out:
#                     self.out = path
#                 elif len(path) < len(self.out):
#                     self.out = path
#             if value < 0:
#                 return
#             for coin in coins:
#                 helper(path + [coin], value - coin)
        
#         self.out = []
#         helper([], amount)
#         return len(self.out) if self.out else -1

        dp = [-1] * (amount + 1)
        for i in range(1, amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                elif i == coin:
                    dp[i] = 1
                elif dp[i-coin] == -1:
                    continue
                elif dp[i] == -1:
                    dp[i] = dp[i-coin] + 1
                else:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        print(dp)
        return dp[-1]