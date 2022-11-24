class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#         subset = [[]]
#         for num in nums:
#             subset += [subnum + [num] for subnum in subset]
#         return subset
    
#         subset = [[], nums]
#         def helper(nums):
#             for i in range(len(nums)):
#                 subnums = nums[:i] + nums[i+1:]
#                 if subnums and subnums not in subset:
#                     subset.append(subnums)
#                     helper(subnums)
        
#         helper(nums)
#         return subset
        
        @cache
        def helper(i, subnums):
            if i == len(nums):
                subset.append(tuple(subnums))
                return
            
            helper(i + 1, subnums) #[[]]
            helper(i + 1, subnums + tuple([nums[i]]))#[[1]]
        
        subset = []
        helper(0, tuple([]))
        return subset
        
