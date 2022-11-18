class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def helper(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if board[i][j] != 'O':
                return
            else:
                board[i][j] = 'T'
            
            for x, y in offset:
                helper(i + x, j + y)
                
        
        offset = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(board), len(board[0])
        for i in [0, m - 1]:
            for j in range(n):
                helper(i, j)
        for i in range(m):
            for j in [0, n - 1]:
                helper(i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        
                