class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = enumerate(nums)
        nums = sorted(nums, key=lambda x: x[1])
        
        output = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i][1] == nums[i-1][1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left][1] + nums[right][1] < -nums[i][1]:
                    left += 1
                elif nums[left][1] + nums[right][1] > -nums[i][1]:
                    right -= 1
                else:
                    output.append([nums[i][1], nums[left][1], nums[right][1]])
                    while left < right and nums[left][1] == nums[left+1][1]:
                        left += 1
                    while left < right and nums[right][1] == nums[right-1][1]:
                        right -= 1
                    left += 1
                    right -= 1
                          
        return output