class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def helper(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if (i, j) in visited:
                return
            if image[i][j] != prev_c:
                return
            image[i][j] = color
            visited.add((i, j))
            
            for x, y in offset:
                helper(i + x, j + y)
        
        visited = set()
        offset = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        m, n = len(image), len(image[0])
        prev_c = image[sr][sc]
        helper(sr, sc)
        return image