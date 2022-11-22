class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        common = nums[0]
        count = 1
        for num in nums:
            if num == common:
                count += 1
            else:
                count -= 1
            if count == 0:
                common = num
                count = 1
        return common