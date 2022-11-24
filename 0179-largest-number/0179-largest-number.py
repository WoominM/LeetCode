class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def cmp_func(x, y):
            """Sorted by value of concatenated string increasingly."""
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1
            
        # Build nums contains all numbers in the String format.
        nums = [str(num) for num in nums]
        
        # Sort nums by cmp_func decreasingly.
        nums.sort(key = cmp_to_key(cmp_func), reverse = True)
        
        # Remove leading 0s, if empty return '0'.
        return ''.join(nums).lstrip('0') or '0'
    
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
    
#     # merge sort        
#     def largestNumber5(self, nums):
#         nums = self.mergeSort(nums, 0, len(nums)-1)
#         return str(int("".join(map(str, nums))))

#     def mergeSort(self, nums, l, r):
#         if l > r:
#             return 
#         if l == r:
#             return [nums[l]]
#         mid = l + (r-l)//2
#         left = self.mergeSort(nums, l, mid)
#         right = self.mergeSort(nums, mid+1, r)
#         return self.merge(left, right)

#     def merge(self, l1, l2):
#         res, i, j = [], 0, 0
#         while i < len(l1) and j < len(l2):
#             if not self.compare(l1[i], l2[j]):
#                 res.append(l2[j])
#                 j += 1
#             else:
#                 res.append(l1[i])
#                 i += 1
#         res.extend(l1[i:] or l2[j:])
#         return res

    # quick sort, in-place
#     def largestNumber(self, nums):
#         self.quickSort(nums, 0, len(nums)-1)
#         return str(int("".join(map(str, nums)))) 

#     def quickSort(self, nums, l, r):
#         if l >= r:
#             return 
#         pos = self.partition(nums, l, r)
#         self.quickSort(nums, l, pos-1)
#         self.quickSort(nums, pos+1, r)

#     def partition(self, nums, l, r):
#         low = l
#         while l < r:
#             if self.compare(nums[l], nums[r]):
#                 nums[l], nums[low] = nums[low], nums[l]
#                 low += 1
#             l += 1
#         nums[low], nums[r] = nums[r], nums[low]
#         return low