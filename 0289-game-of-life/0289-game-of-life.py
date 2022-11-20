class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        offset = [
            [-1, 0], [1, 0], [0, -1], [0, 1],
            [-1, -1], [-1, 1], [1, -1], [1, 1]
        ]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                nei = 0
                for x, y in offset:
                    if 0 <= i + x < m and 0 <= j + y < n:
                        nei += int(str(board[i+x][j+y])[0])
                value = int(str(board[i][j])[0])
                if value == 1:
                    if nei < 2 or nei > 3:
                        board[i][j] = '10'
                elif nei == 3:
                    board[i][j] = '01'
        
        for i in range(m):
            for j in range(n):
                board[i][j] = int(str(board[i][j])[-1])