class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def helper(board, path):
            # print(board, path)
            y_ = len(path)
            if y_ >= n:
                board_ = [''.join(item[:]) for item in board]
                out.append(board_)
                return
            for i in range(n):
                dup = False
                for y, x in path:
                    # print(y_, i, y, x)
                    if i == x:
                        dup = True
                        break
                    if abs((y_ - y) / (i - x)) == 1:
                        dup = True
                if not dup:
                    board_ = [item[:] for item in board]
                    board_[len(path)][i] = 'Q'
                    helper(board_, path + [[len(path), i]])
            
        out = []
        for i in range(n):
            board_ = [['.'] * n for _ in range(n)]
            board_[0][i] = 'Q'
            helper(board_, [[0, i]])
        return out
                
                