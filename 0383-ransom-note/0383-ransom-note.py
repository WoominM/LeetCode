class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hdic = collections.defaultdict(int)
        for c in magazine:
            hdic[c] += 1
        for c in ransomNote:
            hdic[c] -= 1
        for value in list(hdic.values()):
            if value < 0:
                return False
        return True