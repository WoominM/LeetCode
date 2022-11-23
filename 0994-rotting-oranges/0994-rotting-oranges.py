class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def helper(i, j):
            visited = set()
            que = collections.deque()
            que.append((i, j, 0))
            while que:
                i, j, dis = que.popleft()
                if grid[i][j] == 1:
                    grid[i][j] = -dis
                else:
                    grid[i][j] = -min(abs(grid[i][j]), dis)
                visited.add((i, j))
                # print(i, j)
                # for row in grid:
                #     print(row)
                
                for x, y in offset:
                    newi, newj = i + x, j + y
                    if 0 <= newi < m and 0 <= newj < n and\
                        grid[newi][newj] != 0 and grid[newi][newj] != 2 and\
                        (newi, newj) not in visited:
                        que.append((newi, newj, dis + 1))
        
        offset = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    helper(i, j)
        
        out = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                out = min(out, grid[i][j])
        return abs(out)