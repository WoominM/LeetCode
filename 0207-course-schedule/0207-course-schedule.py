class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        if not prerequisites:
            return True
        
        def helper(node):
            if self.loop:
                return
            if visited[node] == -1:
                self.loop = True
                return
            if visited[node] == 1:
                return
            
            visited[node] = -1
            for nei in graph[node]:
                helper(nei)
            visited[node] = 1    
                
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a] += [b]
        
        self.loop = False
        visited = [0] * numCourses
        for course in range(numCourses):
            helper(course)

        return not self.loop