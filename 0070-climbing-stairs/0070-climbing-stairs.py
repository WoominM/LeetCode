class Solution:
    def climbStairs(self, n: int) -> int:
        
#         def helper(n, count):
#             if n < 0:
#                 return
#             if n == 0:
#                 self.out += 1
#                 return
                
#             helper(n-1, count + 1)
#             helper(n-2, count + 1)
        
#         self.out = 0
#         helper(n, 0)
#         return self.out
        
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]
        