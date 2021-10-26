class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        sub = [nums[0]]
        for i,num in enumerate(nums[1:], start=1):
            sub.append(max(sub[i-1] + num, num))
        return max(sub)