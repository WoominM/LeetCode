class Solution:
    def canPartition(self, nums: List[int]) -> bool:
#         @cache
#         def helper(i, value):
#             if i == n:
#                 return value * 2 == target
#             if helper(i + 1, value + nums[i]):
#                 return True
#             if helper(i + 1, value):
#                 return True
            
#         n = len(nums)
#         target = sum(nums)
#         return False if target == 1 else helper(0, 0)
    
        @cache
        def subsetSum(s, i):
            if s == 0: return True
            if i >= len(nums) or s < 0: return False
            return subsetSum(s-nums[i], i+1) or subsetSum(s, i+1)
        total_sum = sum(nums)
        return total_sum & 1 == 0 and subsetSum(total_sum // 2, 0)
        