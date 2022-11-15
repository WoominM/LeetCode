class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # subset = [[]]
        # for num in nums:
        #     subset += [subnum + [num] for subnum in subset]
        # return subset
    
        subset = [[], nums]
        def helper(nums):
            for i in range(len(nums)):
                subnums = nums[:i] + nums[i+1:]
                if subnums and subnums not in subset:
                    subset.append(subnums)
                    helper(subnums)
        
        helper(nums)
        return subset
    
#     class Solution(object):
#     def subsets(self, nums):
#         ret = []
#         self.dfs(nums, [], ret)
#         return ret
    
#     def dfs(self, nums, path, ret):
#         ret.append(path)
#         for i in range(len(nums)):
#             self.dfs(nums[i+1:], path+[nums[i]], ret)
        
