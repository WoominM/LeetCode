class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                pivot = (left + right) // 2
                print(pivot)
                if nums[pivot] == target:
                    return pivot
                elif nums[pivot] < target:
                    left = pivot + 1
                else:
                    right = pivot - 1
            return None
        
        matrix = [num for nums in matrix for num in nums]
        return binary_search(matrix, target) is not None