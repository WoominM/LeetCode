class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def helper(i, j):
            if i < 0 or i == m or j < 0 or j == n:
                return
            if grid[i][j] == '-1':
                return
            if grid[i][j] == '0':
                return
            
            grid[i][j] = '-1'
            for x, y in offset:
                # print(i, j, x, y)
                helper(i + x, j + y)
            
        
        offset = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    helper(i, j)
                    count += 1
        # print(grid)
        return count