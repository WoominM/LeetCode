class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if num == 0 else num for num in nums]
        
        from collections import defaultdict
        dic = defaultdict(list)
        sumv = 0
        for i in range(len(nums)):
            sumv += nums[i]
            if sumv == 0:
                dic[sumv].append(-1)
            dic[sumv].append(i)
        
        maxl = 0
        for sumv, idxs in dic.items():
            if len(idxs) > 0:
                l = idxs[-1] - idxs[0]
                if l > maxl:
                    maxl = l
        
        return maxl