class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeronum = 0
        for i in range(len(nums)):
            if nums[i-zeronum] == 0:
                nums.pop(i-zeronum)
                zeronum += 1
        nums += [0 for _ in range(zeronum)]
        return nums 