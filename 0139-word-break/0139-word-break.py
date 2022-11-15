class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [1] + [-1] * len(s)
        s = '1' + s
        for i in range(1, len(s)):
            for j in range(i):
                if dp[i] == 1:
                    continue
                if dp[j] == 1 and s[j+1: i+1] in wordDict:
                    dp[i] = 1
                # print(i, j, s[j+1: i+1], dp)
        return True if dp[-1] == 1 else False 