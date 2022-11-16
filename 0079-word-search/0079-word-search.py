class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:     
        def helper(idx, i, j, path):
            # print(i, j, path)
            # for v in visited:
            #     print(v)
            # print('')
            if out:
                return
            if idx == lenw:
                out.append(path)
                return
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if visited[i][j] == 1:
                return
            if board[i][j] != word[idx]:
                return
            
            visited[i][j] = 1
            for x, y in offset:
                helper(idx + 1, i + x, j + y, path + [[i, j]])
            visited[i][j] = 0
        
        m, n = len(board), len(board[0])
        lenw = len(word)
        visited = [[0] * n for _ in range(m)]
        
        offset = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        out = []
        for i in range(m):
            for j in range(n):
                helper(0, i, j, [])
                visited[i][j] = 0
                
        # print(out)
        return out
    
    
#         def dfs(ind, i, j):
#             if self.Found: return        #early stop if word is found

#             if ind == k:
#                 self.Found = True                #for early stopping
#                 return 

#             if i < 0 or i >= m or j < 0 or j >= n: return 
#             tmp = board[i][j]
#             if tmp != word[ind]: return

#             board[i][j] = "#"
#             for x, y in [[0,-1], [0,1], [1,0], [-1,0]]:
#                 dfs(ind + 1, i+x, j+y)
#             board[i][j] = tmp
        
#         self.Found = False
#         m, n, k = len(board), len(board[0]), len(word)
        
#         for i, j in product(range(m), range(n)):
#             if self.Found: return True          #early stop if word is found
#             dfs(0, i, j)
#         return self.Found