class Solution:
    def romanToInt(self, s: str) -> int:
        loman = dict({
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        })
        
        out = loman[s[0]]
        for i in range(1, len(s)):
            if loman[s[i]] <= loman[s[i-1]]:
                out += loman[s[i]]
            else:
                out -= loman[s[i-1]]
                out += (loman[s[i]] - loman[s[i-1]])
        return out