class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hdict = collections.defaultdict(int)
        for c in s:
            hdict[c] += 1
        for c in t:
            if c not in hdict:
                return False
            hdict[c] -= 1
        return max(list(hdict.values())) == 0