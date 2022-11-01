class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        def find_min_max(left, right):
            local_min = float('inf')
            local_max = float('-inf')
            for i in range(left, right+1):
                if i == len(nums):
                    break
                local_min = min(local_min, nums[i])
                local_max = max(local_max, nums[i])
                
            return local_min, local_max
                
        if len(nums) < 2: 
            return 0
        
        left, right = 0, len(nums) - 1
        while left < len(nums) - 1 and nums[left] <= nums[left+1]:
            left += 1
        while right > 0 and nums[right] >= nums[right-1]:
            right -= 1
            
        if left > right:
            return 0
            
        lmin, lmax = find_min_max(left, right+1) 
        while left > 0 and lmin < nums[left-1]:
            left -= 1
        while right < len(nums) - 1 and lmax > nums[right+1]:
            right += 1
            
        return right - left + 1