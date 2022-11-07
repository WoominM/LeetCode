class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mincosts = [[0]]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: 
                    continue
                elif i == 0:
                    mincost = grid[i][j-1] + mincosts[i][j-1]
                elif j == 0:
                    mincosts.append([grid[i-1][j] + mincosts[i-1][j]])
                    continue
                else:
                    mincost = min(grid[i][j-1] + mincosts[i][j-1], grid[i-1][j] + mincosts[i-1][j])
                mincosts[i].append(mincost)
                # print(i, j)
                # for mn in mincosts:
                #     print(mn)
                # print('')
        
        return mincosts[m-1][n-1] + grid[m-1][n-1]