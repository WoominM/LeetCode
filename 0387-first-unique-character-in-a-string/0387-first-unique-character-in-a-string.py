class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1