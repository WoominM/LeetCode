class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        offset = [[-1, 0], [1, 0], [0, -1], [0, 1],
                  [-1, -1], [1, 1], [1, -1], [-1, 1]]
        
        from collections import deque
        que = deque([[0, 0]])
        grid[0][0] = -1
        m, n = len(grid), len(grid[0])
        while que:
            # print(grid)
            i, j = que.popleft()
            for x, y in offset:
                i_, j_ = i + x, j + y
                if i_ < 0 or i_ == m or j_ < 0 or j_ == n:
                    continue
                if grid[i_][j_] == 0:
                    grid[i_][j_] = grid[i][j] - 1
                    que.append([i_, j_])
        
        out = grid[-1][-1]
        return abs(out) if out < 0 else -1
        
        
        