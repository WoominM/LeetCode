class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:        

        sums = [] 
        sumv = 0 
        for num in nums:
            sumv += num
            sums.append(sumv)
            
        from collections import defaultdict
        dic = defaultdict(list)
        dic[0].append(-1)
        
        total_num = 0
        for i, sumv in enumerate(sums):
            if sumv - k in dic:
                total_num += len(dic[sumv - k])
            
            dic[sumv].append(i)
        
        return total_num
                