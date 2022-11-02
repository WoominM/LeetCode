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
    
        x, y = 0, len(matrix) - 1
        while x < len(matrix[0]) and y >= 0:
            if matrix[y][x] < target:
                x += 1
            elif matrix[y][x] > target:
                y -= 1
            else:
                return True
        if x == len(matrix) and y >= 0:
            return matrix[y][x-1] == target
        return