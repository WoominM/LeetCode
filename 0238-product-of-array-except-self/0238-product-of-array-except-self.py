class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            
#         def helper(start, path, value):
#             print(path, value)
#             if path == n - 1:
#                 self.out = [value] + self.out
#                 return
            
#             for i in range(start+1, n-k+path+1):
#                 helper(i, path + 1, value * nums[i])
        
#         self.out = []
#         n = len(nums)
#         k = n - 1
#         for i in range(n-k+1):
#             helper(i, 1, nums[i])
#         return self.out
        
        n = len(nums)
        out = [1] * n
        for i in range(n-1):
            out[i+1] = out[i] * nums[i]
            
        nums.append(1)
        for i in range(n-1, 0, -1):
            nums[i] *= nums[i+1]
            out[i-1] *= nums[i]
        return out
            