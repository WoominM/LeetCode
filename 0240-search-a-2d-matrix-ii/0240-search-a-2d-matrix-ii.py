class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # while matrix:
        #     # for nums in matrix:
        #     #     print(nums)
        #     # print('')
        #     m, n = len(matrix), len(matrix[0])
        #     if m == 0 or n == 0:
        #         return matrix[0] == target
        #     if matrix[m-1][0] == target:
        #         return True
        #     elif matrix[m-1][0] > target:
        #         matrix = matrix[:-1]
        #     else:
        #         matrix = [nums[1:] for nums in matrix]
        # return False
    
        x, y = len(matrix[0]) - 1, 0
        while x >= 0 and y < len(matrix):
            if matrix[y][x] > target:
                x -= 1
            elif matrix[y][x] < target:
                y += 1
            else:
                return True
        return False