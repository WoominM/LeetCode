class Solution:
    def longestPalindrome(self, s: str) -> int:
        hdic = collections.Counter(s)
        values = list(hdic.values())
        
        out, odd_num = 0, 0
        for value in values:
            if value % 2 != 0:
                odd_num += 1
            out += value
            
        return out - odd_num + 1 if odd_num > 0 else out