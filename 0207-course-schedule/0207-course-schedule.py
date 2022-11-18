class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        
        def helper(node):
            # print(node, self.loop, visited)
            if self.loop:
                return
            if visited[node] == -1:
                self.loop = True
                return
            if visited[node] == 1:
                return
            
            visited[node] = -1
            for nextnode in graph[node]:
                helper(nextnode)
                
            visited[node] = 1
        
        visited = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
        
        # print(graph)
        self.loop = False
        for node in range(numCourses):
            helper(node)
            
        return not self.loop