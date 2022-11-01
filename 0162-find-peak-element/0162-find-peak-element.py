class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            pivot = (left + right) // 2
            if nums[pivot + 1] > nums[pivot]:
                left = pivot + 1
            else:
                right = pivot
        return left