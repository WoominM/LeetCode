class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            nums.pop(nums.index(num))
            if num not in nums:
                return num
            else:
                nums.insert(i, num)