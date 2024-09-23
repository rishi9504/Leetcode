class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        v = set()
        def dfs(r):
            v.add(r)
            for k in rooms[r]:
                if k not in v:
                    dfs(k)
        dfs(0)
        return len(v) == len(rooms)            
        
