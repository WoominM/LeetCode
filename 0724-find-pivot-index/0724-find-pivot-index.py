class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum, rightsum = 0, sum(nums)
        for i in range(len(nums)):
            if leftsum == rightsum - nums[i]:
                return i
            leftsum += nums[i]
            rightsum -= nums[i]
        return -1