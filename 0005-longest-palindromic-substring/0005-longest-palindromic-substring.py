class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        out = s[0]
        for i in range(len(s)-1):
            right = i
            while right <= len(s) - 1 and s[i] == s[right]:
                right += 1
            left = i - 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1> len(out):
                out = s[left + 1: right]
        return out
            