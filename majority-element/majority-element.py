class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        def major(nums):
            dic = {}
            maxfrq = 0
            maxnum = None
            for num in nums:
                if num not in dic.keys():
                    dic[num] = 1
                else:
                    dic[num] += 1
                    
                if dic[num] > maxfrq:
                    maxfrq = dic[num]
                    maxnum = num
                    
            return maxnum
        
        return major(nums)
        
        
        