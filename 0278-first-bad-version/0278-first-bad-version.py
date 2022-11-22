# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        
        while left < right:
            pivot = (left + right) // 2
            if isBadVersion(pivot):
                right = pivot
            else:
                left = pivot + 1
                
        return left