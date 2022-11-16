class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

#         def helper(room):
#             # print(room, visited)
#             if room not in visited: 
#                 visited.add(room)
#                 for key in rooms[room]:
#                     helper(key)
                    
#         visited = set()
#         helper(0)
#         return len(visited) == len(rooms)
        
        from collections import deque
        visited = set()
        visited.add(0)
        que = deque()
        que.append(0)
        while que:
            room = que.popleft()
            print(room)
            for key in rooms[room]:
                if key not in visited:
                    que.append(key)
                    visited.add(key)
        return len(visited) == len(rooms)