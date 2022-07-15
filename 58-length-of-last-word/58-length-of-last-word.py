class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')[::-1]
        for w in s:
            if len(w) > 0:
                return len(w)
        