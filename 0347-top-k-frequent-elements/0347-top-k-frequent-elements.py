class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        return sorted(dic, key=lambda x: dic[x], reverse=True)[:k]