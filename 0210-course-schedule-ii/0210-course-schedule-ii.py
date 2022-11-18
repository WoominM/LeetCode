class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
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
            out.append(node)
        
        visited = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        
        # print(graph)
        self.loop = False
        out = []
        for node in range(numCourses):
            helper(node)
            
        return out if not self.loop else []