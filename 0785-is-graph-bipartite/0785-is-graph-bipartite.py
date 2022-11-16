class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # from collections import deque
        # colored = [0] * len(graph)
        # for i in range(len(graph)):
        #     if colored[i] == 0:
        #         colored[i] = -1
        #         que = deque([i])
        #         while que:
        #             idx = que.popleft()
        #             for node in graph[idx]:
        #                 if colored[node] == colored[idx]:
        #                     return False
        #                 if colored[node] == 0:
        #                     colored[node] = -1 * colored[idx]
        #                     que.append(node)            
        # return True
    
        def helper(i, c):
            if not self.out:
                return
            if colored[i] == 0:
                colored[i] = -c
                
            for node in graph[i]:
                if colored[node] == colored[i]:
                    self.out = False
                    return
                if colored[node] == 0:
                    helper(node, colored[i])
        
        self.out = True
        colored = [0] * len(graph)
        for i in range(len(graph)):
            if colored[i] == 0:
                helper(i, 1)
        # print(colored)
        return self.out
        