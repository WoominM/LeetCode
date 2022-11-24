class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        while matrix:
            out += list(matrix.pop(0))  
            matrix = [*zip(*matrix)][::-1]
        return out