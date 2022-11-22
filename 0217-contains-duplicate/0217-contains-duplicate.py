class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hdic = collections.defaultdict(int)
        for num in nums:
            hdic[num] += 1
            if hdic[num] > 1:
                return True
        return False