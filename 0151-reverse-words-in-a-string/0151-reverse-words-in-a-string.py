class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        s = [c for c in s if c.isalnum()]
        return ' '.join(s[::-1])