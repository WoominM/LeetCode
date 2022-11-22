class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(char) for char in strs])
        out = ''
        for i in range(min_len):
            hset = set()
            for char in strs:
                hset.add(char[i])
            if len(hset) == 1:
                out += str(list(hset)[0])
            else:
                break
        return out