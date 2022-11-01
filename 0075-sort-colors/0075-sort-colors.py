class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        
        idx0, idx2, idx = 0, len(nums) - 1, 0
        
        while idx <= idx2:
            if nums[idx] == 1:
                idx += 1
            elif nums[idx] == 0:
                nums[idx], nums[idx0] = nums[idx0], nums[idx]
                idx += 1
                idx0 += 1
            elif nums[idx] == 2:
                nums[idx], nums[idx2] = nums[idx2], nums[idx]
                idx2 -= 1
                
        return nums
                