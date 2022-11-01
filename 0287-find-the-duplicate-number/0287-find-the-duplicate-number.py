class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # #Sol1 -> Time: O(nlogn), Space: O(1)
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]
        
        #Sol2 -> O(n), Space: O(n)
        table = [0] * len(nums)
        for num in nums:
            table[num] += 1
            if table[num] == 2:
                return num
        
        