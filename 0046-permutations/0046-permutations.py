class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
#         out = []
#         def helper(i, temp):
#             if i == len(nums):
#                 out.append(temp)
#                 return
            
#             subnums = [num for num in nums if num not in temp]
#             for num in subnums:
#                 helper(i + 1, temp + [num])
                
#         helper(0, [])
#         return out


        def dfs(nums, path, out):
            if not nums:
                out.append(path)
                
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], out)
        
        out = []
        dfs(nums, [], out)
        return out
    
