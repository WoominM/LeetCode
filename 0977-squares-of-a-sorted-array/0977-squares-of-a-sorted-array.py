class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] >= 0:
                break
                
        nums1, nums2 = nums[:i][::-1], nums[i:]
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        out = []
        while nums1 or nums2:
            if not nums1:
                out.append(nums2[-1] ** 2)
                nums2.pop()
            elif not nums2:
                out.append(nums1[-1] ** 2)
                nums1.pop()
            elif abs(nums1[-1]) <= abs(nums2[-1]):
                out.append(nums2[-1] ** 2)
                nums2.pop()
            elif abs(nums1[-1]) >= abs(nums2[-1]):
                out.append(nums1[-1] ** 2)
                nums1.pop()
        return out[::-1]
                    