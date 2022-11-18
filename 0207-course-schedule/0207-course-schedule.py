class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        
        def helper(node):
            if visit[node] == -1:
                return False
            if visit[node] == 1:
                return True
            visit[node] = -1
            for j in graph[node]:
                if not helper(j):
                    return False
            visit[node] = 1
            return True
        
        graph = [[] for _ in range(numCourses)]
        visit = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            
        for node in range(numCourses):
            if not helper(node):
                return False
            
        return True