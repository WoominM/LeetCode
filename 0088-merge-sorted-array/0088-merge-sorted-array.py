class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums2:
            return nums1
        pm, pn, p = m - 1, n - 1, m + n - 1
        
        while pn >= 0 and pm >= 0:
            if nums2[pn] >= nums1[pm]:
                nums1[p] = nums2[pn]
                p -= 1
                pn -= 1
            else:
                nums1[p] = nums1[pm]
                p -= 1
                pm -= 1
        if pn >= 0:
            nums1[:p+1] = nums2[:p+1]
        return nums1