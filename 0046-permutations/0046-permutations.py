class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        def helper(i, temp):
            if i == len(nums):
                out.append(temp)
                return
            
            for num in [num for num in nums if num not in temp]:
                helper(i + 1, temp + [num])
                
        helper(0, [])
        return out