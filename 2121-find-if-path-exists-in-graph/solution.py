from collections import deque,defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        queue = deque([source])
        while queue:
            c = queue.popleft()
            if c == destination:
                return True
            visited.add(c)
            for neighbor in graph[c]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False                    


        
