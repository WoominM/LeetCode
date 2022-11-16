class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        
        colored = [0] * len(graph)
        for i in range(len(graph)):
            if colored[i] == 0:
                colored[i] = -1
                que = deque([i])
                while que:
                    idx = que.popleft()
                    for node in graph[idx]:
                        if colored[node] == colored[idx]:
                            return False
                        if colored[node] == 0:
                            colored[node] = -1 * colored[idx]
                            que.append(node)
        # print(colored)            
        return True