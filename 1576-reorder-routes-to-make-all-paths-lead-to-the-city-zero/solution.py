class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # make adjacency list from graph
        graph = {i: [] for i in range(n)}
        for a,b in connections:
            graph[a].append((b,1)) # reverse road
            graph[b].append((a,0)) # correct road
        v = set()
        c=0
        def dfs(city):
            nonlocal c
            v.add(city)
            for i,nc in graph[city]:
                if i not in v:
                    c+=nc 
                    dfs(i)
        dfs(0)
        return c           

        
