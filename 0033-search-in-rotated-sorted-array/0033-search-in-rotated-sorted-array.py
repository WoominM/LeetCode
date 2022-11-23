class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        left, right = 0, len(nums) - 1
        k = 0
        while nums[left] > nums[right]:
            left -= 1
            right -= 1
            k += 1
            
        left, right = 0, len(nums) - 1
        
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot-k] == target:
                return pivot - k if pivot >= k else len(nums) + (pivot - k) 
            elif nums[pivot-k] < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1