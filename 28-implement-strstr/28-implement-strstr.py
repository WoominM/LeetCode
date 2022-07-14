class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenh, lenn = len(haystack), len(needle)
        for i in range(lenh-lenn+1):
            if haystack[i:i+lenn] == needle:
                return i
        return -1 if haystack != needle else 0
            