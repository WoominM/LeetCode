class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return nums.index(target)
        
        idx = 0
        for i,num in enumerate(nums): 
            if target > num:
                idx = i + 1
            elif target == num:
                return i
        return idx