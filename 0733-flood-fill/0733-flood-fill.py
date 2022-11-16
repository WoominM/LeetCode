class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def helper(i, j, c):
            if i < 0 or i == m or j < 0 or j == n:
                return
            if image[i][j] != c:
                return
            if visited[i][j] == 1:
                return
            visited[i][j] = 1
            image[i][j] = color
            for x, y in offset:
                helper(i + x, j + y, c)
                
        offset = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(image), len(image[0])
        visited = [[0] * n for _ in range(m)]
        helper(sr, sc, image[sr][sc])
        return image
        