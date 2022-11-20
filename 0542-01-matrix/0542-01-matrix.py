class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         offset = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#         m, n = len(mat), len(mat[0])
#         out = [[0] * n for _ in range(m)]
#         for cx in range(m):
#             for cy in range(n):
#                 print(cx, cy)
#                 if mat[cx][cy] == 1:
#                     visited = set()
#                     que = collections.deque([[cx, cy, 0]])
#                     while que:
#                         i, j, dis = que.popleft()
#                         if mat[i][j] == 0:
#                             out[cx][cy] = dis
#                             break
                            
#                         visited.add((i, j))
#                         for x, y in offset:
#                             i_, j_ = i + x, j + y
#                             if 0 <= i_ < m and 0 <= j_ < n and (i_, j_) not in visited:
#                                 que.append([i_, j_, dis+1])
#         return out  
        
        offset = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        que = collections.deque()
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    que.append((i, j))
                else:
                    mat[i][j] = -1

        while que:
            i, j = que.popleft()
            for x, y in offset:
                newi, newj = i + x, j + y
                if 0 <= newi < m and 0 <= newj < n and mat[newi][newj] == -1:
                    mat[newi][newj] = mat[i][j] + 1
                    que.append((newi, newj))
        return mat