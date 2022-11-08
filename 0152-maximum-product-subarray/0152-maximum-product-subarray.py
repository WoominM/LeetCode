class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpmin = [nums[0]]
        dpmax = [nums[0]]
        for i in range(1, len(nums)):
            dpmin.append(min(dpmin[i-1] * nums[i], dpmax[i-1] * nums[i], nums[i]))
            dpmax.append(max(dpmin[i-1] * nums[i], dpmax[i-1] * nums[i], nums[i]))
        return max(dpmax)