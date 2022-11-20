class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        table = {}
        left, right = 0, 0
        while right < len(s):
            if s[right] in table and left <= table[s[right]]:
                left = table[s[right]] + 1
            else:
                max_len = max(max_len, right - left + 1)
            table[s[right]] = right
            right += 1
        return max_len