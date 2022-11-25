class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
        
#         while left < right:
#             pivot = (left + right) // 2
#             if nums[pivot + 1] > nums[pivot]:
#                 left = pivot + 1
#             else:
#                 right = pivot
#         return left
    
        left = 0
        right = len(nums)-1

        # handle condition 3
        while left < right-1:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        #handle condition 1 and 2
        return left if nums[left] >= nums[right] else right