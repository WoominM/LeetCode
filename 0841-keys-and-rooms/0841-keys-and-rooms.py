class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def helper(room):
            if room not in visited: 
                visited.add(room)
                for key in rooms[room]:
                    helper(key)
                    
        visited = set()
        helper(0)
        return len(visited) == len(rooms)