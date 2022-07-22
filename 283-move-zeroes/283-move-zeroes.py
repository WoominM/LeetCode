class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         zeronum = 0
#         for i in range(len(nums)):
#             if nums[i-zeronum] == 0:
#                 nums.pop(i-zeronum)
#                 zeronum += 1
#         nums += [0] * zeronum
#         return nums 
    
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1