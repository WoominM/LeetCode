class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        from collections import defaultdict
        dic = defaultdict(int)
        for c in words:
            dic[c] += 1
        output = sorted(dic, key=lambda x: dic[x], reverse=True)
        return output[:k]