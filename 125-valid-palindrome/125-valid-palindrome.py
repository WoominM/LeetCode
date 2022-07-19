class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '').lower()
        sr = ''
        for c in s:
            if not c.isalnum():
                s = s.replace(c, '')
            else:
                sr += c
        return s == sr[::-1]